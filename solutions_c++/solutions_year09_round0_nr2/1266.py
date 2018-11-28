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

int h, w, T;
int alt[111][111];
char lit[111][111];

int dirh[4] = {-1, 0, 0, 1};
int dirw[4] = {0, -1, 1, 0};
char le;

char znajdzszefa(int a, int b){
  if (lit[a][b]) return lit[a][b];
  int hei = alt[a][b];
  int kier = -1;
  REP(k, 4){
    int na = a + dirh[k];
    int nb = b + dirw[k];
    if (hei > alt[na][nb]){
      hei = alt[na][nb];
      kier = k;
    }
  }
  if (hei == alt[a][b])
    return lit[a][b] = le++;
  else
    return lit[a][b] = znajdzszefa(a + dirh[kier], b + dirw[kier]);
}

int main(){
  scanf("%d", &T);
  REP(iii, T){
    printf("Case #%d:\n", iii+1);
    le = 'a';
    scanf("%d%d", &h, &w);
    REP(i, h+2) REP(j, w+2) alt[i][j] = 10100;
    REP(i, h) REP(j, w) scanf("%d", &alt[i+1][j+1]);
    REP(i, h) REP(j, w) { lit[i+1][j+1] = 0; }
    REP(i, h) REP(j, w)
      znajdzszefa(i+1, j+1);
    REP(i, h){
      REP(j, w) printf("%c ", lit[i+1][j+1]);
      printf("\n");
    }
  }
  return 0;
}
