#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
#include <cassert>
using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(var,pocz,koniec) for (int var=(pocz); var<=(koniec); ++var)
#define FORD(var,pocz,koniec) for (int var=(pocz); var>=(koniec); --var)
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) (int)x.size()

const int N = 110;
int mapa[N][N];
int vis[N][N];
int n,m;
int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};
int numery = 0;

int between(int x,int a,int b){
  return x >= a && x <= b;
}

char dfs(int i,int j){
  if (vis[i][j] != -1) return 'a' + vis[i][j];
  int wys = mapa[i][j];
  REP(ruch,4){
    int ni = i + dx[ruch];
    int nj = j + dy[ruch];
    if (between(ni,0,n-1) && between(nj,0,m-1)) wys = min(wys,mapa[ni][nj]);
  }
  if (wys == mapa[i][j]){
    vis[i][j] = numery++;
    return 'a' + vis[i][j];
  } else {
    REP(ruch,4){
      int ni = i + dx[ruch];
      int nj = j + dy[ruch];
      if (between(ni,0,n-1) && between(nj,0,m-1) && wys == mapa[ni][nj]){
        char c = dfs(ni,nj);
        vis[i][j] = c-'a';
        return c;
      }
    }
  }
  assert(0);
  return '-';
}

int main(){
  int testy;
  scanf("%d",&testy);
  int numer=0;
  while (testy--){
    printf("Case #%d:\n",++numer);
    scanf("%d %d",&n,&m);
    REP(i,n) REP(j,m) scanf("%d",mapa[i]+j);
    REP(i,n) REP(j,m) vis[i][j] = -1;
    numery = 0;
    REP(i,n){
      REP(j,m) printf("%c ",dfs(i,j));
      puts("");
    }
  }
  return 0;
}
