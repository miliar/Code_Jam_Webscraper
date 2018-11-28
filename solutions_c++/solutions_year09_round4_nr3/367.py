// compile with "g++ XXX.cc -mno-cygwin -O2" in Cygwin

#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
#include<vector>
#include<cmath>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<numeric>
#include<functional>
#include<complex>

using namespace std;
#define BET(a,b,c) ((a)<=(b)&&(b)<(c))
#define FOR(i,n) for(int i=0,i##_end=(int(n));i<i##_end;i++)
#define SZ(x) (int)(x.size())
#define ALL(x) (x).begin(),(x).end()
#define MP make_pair
#define CLS(x,val) memset((x) , val , sizeof(x)) 
typedef long long ll_t;
typedef long double ld_t;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef complex<int> xy_t;

const double PI = 4.0*atan(1.0);

int compare(VI& p1 , VI& p2)
{
  int k = SZ(p1);
  FOR(i,k){
    if(p1[i]==p2[i]) return 0;
    if(i+1<k){
      if(p1[i]>p2[i] && p1[i+1]<p2[i+1]) return 0;
      if(p1[i]<p2[i] && p1[i+1]>p2[i+1]) return 0;
    }
  }
  return p1[0] < p2[0] ? -1 : +1;
}
vector<int> topological_sort(const vector<vector<int> >& adj)
{
  int n = SZ(adj);
  vector<int> deg(n) , ret;
  FOR(i,SZ(adj)) FOR(j,SZ(adj[i])) deg[adj[i][j]]++;

  FOR(_,n){
    int pos=-1;
    FOR(i,n) {
      if(deg[i]==0){
        pos = i ; 
      }
    }
    if(pos==-1) return vector<int>();
    ret.push_back(pos);
    deg[pos]--;    
    FOR(i,SZ(adj[pos])){
      deg[adj[pos][i]]--;
    }
  }
  return ret;
}

bool ok[17][17];
int memo[1<<16][16][17];
int n,k;
int dfs(VI& perm , int pos_idx = 0 , int used=0 , int pre = -1)
{
  if(pos_idx==n){
    if(used==(1<<n)-1){
      return 1 ; 
    }
    return dfs(perm , 0 , used , -1) + 1;
  }
  int pos = perm[pos_idx];
  //cout << pos_idx << " " << used << " " << pre << endl;
  int& ret = memo[used][pos_idx][pre+1];
  if(ret != -1) return ret;
  int val = 1<<28;

  //if((used&(1<<pos))||pre!=-1)
  if(!((used&(1<<pos))==0 && pre==-1)){
    val = min(val , dfs(perm , pos_idx + 1 , used , pre));
  }

  if((used&(1<<pos))==0){
    if(pre==-1 || ok[pre][pos]){
      val = min(val , dfs(perm , pos_idx + 1 , used|(1<<pos) , pos));
    }
  }

  return ret = val;
}

int main() {
  int t,case_no=1;
  cin>>t;
  while(t--){
    int ans = -1 ;
    cin>>n>>k;
    VVI graphs(n);
    FOR(i,n){
      FOR(j,k){
        int x;
        cin>>x;
        graphs[i].push_back(x);
      }
    }
    VVI adj(n);
    CLS(ok , 0);
    FOR(i,n) FOR(j,i){
      int c = compare(graphs[i] , graphs[j]);
      if(c!=0){
        if(c==1) adj[i].push_back(j);
        else     adj[j].push_back(i);
        ok[i][j]=ok[j][i]=true;
      }
      //cout << c << " ok " << " " << i << " " << j << endl;
    }
    VI perm = topological_sort(adj);
    //FOR(i,n) cout << " " << perm[i] << endl;
    CLS(memo , -1);
    ans = dfs(perm) ; 

    printf("Case #%d: %d\n" , case_no++ , ans);
  }
  return 0 ;
}
