#include<iostream>
#include<sstream>
#include<cstdio>
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

#define BET(a,i,b) (((a)<=(i))&&((i)<(b)))
#define FOR(i,n)  for(int i=0;i<(int)(n);i++)
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define MP make_pair
typedef long long ll_t;
typedef long double ld_t;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef complex<int> xy_t;
ll_t memo[(1<<10)+10][101];
vector<string> dat;
int M , N ; 
int NG[101];
int dfs(int used=0 , int pos=0)
{
  if(pos>=M) return 0;
  used &= (1<<N)-1;
  ll_t& ret = memo[used][pos];
  if(ret != -1) return ret;
  ll_t val = 0 ;
  FOR(choise , (1<<N))
    {
      if(NG[pos] & choise) continue;
      if(choise & used) continue;
      bool ok = true;
      {
        int x = choise;
        while(x){
          if(x%4==3){
            ok = false;
            //cout << x << " " << "N" << endl;
            break;
          }
          x>>=1;
        }
        if(!ok) continue;
      }
      int a = __builtin_popcount(choise) ;
      int nused = (choise<<1) | (choise>>1);
      val >?= dfs(nused , pos+1) + a;
    }
  return ret = val;
}

void solve()
{
  ll_t ans = 0;
  cin>>M>>N;
  dat.clear();
  memset(memo , -1 , sizeof(memo));
  memset(NG , 0 , sizeof(NG));
  FOR(i,M){
    string line;
    cin>>line;
    dat.push_back(line);
    FOR(j,SZ(line)){
      if(line[j]=='x'){
        NG[i] |= (1<<j);
      }
    }
  }
  ans = dfs();
  cout << ans << endl;
}

int main()
{
  int t; 
  cin>>t;
  FOR(case_no,t)
    {
      printf("Case #%d: " , case_no + 1 );
      solve();
    }
  return 0 ;
}
