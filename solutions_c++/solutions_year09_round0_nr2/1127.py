#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <vector>
#include <cmath>
#include <list>
#include <sstream>
#include <algorithm>

using namespace std;

typedef pair<int,int> PII;
typedef long long LL;
typedef vector<int> VI;
typedef pair<LL,LL> PLL;
typedef vector<pair<int,int> > VPII;
typedef vector<LL> VLL;
typedef vector<vector<int> > VVI;
typedef vector<string> VS;

#define PI 3.14159265358979323
#define EE 2.71828182845
#define EPS 10e-11
#define INF 1000000

inline LL MAX(LL a, LL b){ return a < b ? b : a;}
inline LL MIN(LL a, LL b){ return a < b ? a : b;}

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)

#define MP make_pair
#define PB push_back

PII G[550][550];
PII T[550][500];
int V[550][550];
char O[550][550];

int dx[4] = {-1,0,0,1};
int dy[4] = {0,-1,1,0};
int H,W;

void determine(int x, int y){
  int best = -1;
  int bestv = V[x][y];

  FOR(i,4){
    int tx = x + dx[i]; int ty = y + dy[i];
    if (tx < 0 || tx >= H)continue;
    if (ty < 0 || ty >= W)continue;
    if (V[tx][ty] < bestv){
      bestv = V[tx][ty];
      best = i;
    }
  }

  if (best == -1){ G[x][y] = MP(x,y); return;}

  G[x][y] = MP(x + dx[best], y + dy[best] );
  return; 
}

PII target(int x, int y){
  if (G[x][y].first == x && G[x][y].second == y){
    return MP(x,y);
  }
  return target( G[x][y].first, G[x][y].second );
}

map<PII, char> M;

int main(){

  int TT;
  scanf("%d ",&TT);
  FOR(tt,TT){

    M.clear();

    scanf("%d %d ",&H,&W);
    FOR(i,H)FOR(j,W) scanf("%d ",&V[i][j]);
    FOR(i,H)FOR(j,W) determine(i,j);
    FOR(i,H)FOR(j,W) T[i][j] = target(i,j);

    int let=0;
    FOR(i,H)FOR(j,W){
      if (M.find( T[i][j] ) != M.end())continue;
      M[T[i][j]] = (char)((int)'a' + let);
      let++;
    }

    printf("Case #%d:\n",tt+1);

    FOR(i,H){
      FOR(j,W){
        if (j) printf(" ");
        printf("%c", M[T[i][j]] );
      }
      printf("\n");
    }


  }

  return 0;
}
