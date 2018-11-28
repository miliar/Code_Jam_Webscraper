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

char dat[20][20];

int dx[]={0,1,0,-1};
int dy[]={1,0,-1,0};

struct DisjointSet {
  vector<int> group ;
  DisjointSet(int n) : group(n, -1) { ; }
  bool unionSet(int x, int y) {
    x = root(x); y = root(y);
    if (x != y) {
      if (group[y] < group[x]) swap(x, y);
      group[x] += group[y]; 
      group[y] = x;
    }
    return x != y;
  }
  bool is_sameSet(int x, int y) { return root(x) == root(y); }
  int root(int x) { return group[x] < 0 ? x : group[x] = root(group[x]); }
  int size(int x) { return -group[root(x)]; }
};

bool connected(vector<pair<int,int> >& box)
{
  DisjointSet ds(SZ(box));
  FOR(i,SZ(box)) FOR(j,i){
    int dx = box[i].first - box[j].first;
    int dy = box[i].second - box[j].second;
    if(abs(dx)+abs(dy)==1){
      ds.unionSet(i,j);
    }
  }
  int g=0;
  FOR(i,SZ(box)){
    if(ds.root(i)==i) g++;
  }
  return g==1;
}

int main() {
  int t,case_no=1;
  cin>>t;
  while(t--){
    int ans = -1 ;
    int R,C;
    cin>>R>>C;
    vector<pair<int,int> > box,goal;
    FOR(i,R) FOR(j,C) {
      cin>>dat[i][j];
      char c=dat[i][j];
      if(c=='w' || c=='o'){
        box.push_back(MP(i,j));
      }
      if(c=='w' || c=='x'){
        goal.push_back(MP(i,j));
      }
      if(c=='w'){
        dat[i][j]='x';
      }
    }

    queue<vector<pair<int,int> > >qu_list[2];

    int step = 0 ;
    
    sort(ALL(box));

    qu_list[0].push(box);

    set<vector<pair<int,int> > > memo;

    if(connected(goal))
    while(!qu_list[0].empty() || !qu_list[1].empty()){
      queue<vector<pair<int,int> > >&qu=qu_list[0];
      while(!qu.empty()){
        vector<pair<int,int> > now = qu.front(); qu.pop();
        if(memo.count(now)) continue;
        memo.insert(now);
        if(now==goal){
          ans = step;
          break;
        }

        bool danger = !connected(now);

        FOR(i,SZ(now)){
          pair<int,int> pos = now[i];
          FOR(j,4){
            int nr = pos.first + dy[j];
            int nc = pos.second + dx[j];
            int mr = pos.first + dy[(j+2)%4];
            int mc = pos.second + dx[(j+2)%4];
            if(BET(0,nr,R) && BET(0,nc,C) && dat[nr][nc]!='#' &&
               BET(0,mr,R) && BET(0,mc,C) && dat[mr][mc]!='#'
               ){
              if(binary_search(ALL(now) , MP(nr,nc))) continue;
              if(binary_search(ALL(now) , MP(mr,mc))) continue;
              vector<pair<int,int> > new_stat(now);
              new_stat[i] = MP(mr,mc);
              sort(ALL(new_stat));

              if(danger){
                if(!connected(new_stat)) continue;
              }
              qu_list[1].push(new_stat);
            }
          }
        }
      }
      if(ans>=0) break;
      swap(qu_list[0],qu_list[1]);
      step++;
    }

    printf("Case #%d: %d\n" , case_no++ , ans);
  }
  return 0 ;
}
