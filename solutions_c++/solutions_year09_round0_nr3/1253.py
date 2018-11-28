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

char txt[10000];
const char *pat = "welcome to code jam";
int n, m;
int t[1000][100];

int main(){
  fgets(txt, 9999, stdin);
  int te; sscanf(txt, "%d", &te);
  m = strlen(pat);
  REP(iii, te){
    fgets(txt, 9999, stdin);
    n = strlen(txt);
    REP(i, n+2) REP(j, m+2) t[i][j] = 0;
    REP(i, n+1) t[i][0] = 1;
    REP(i, n)
      REP(j, m){
        t[i+1][j+1] = t[i][j+1];
        if (pat[j] == txt[i]){
          t[i+1][j+1] += t[i][j];
          t[i+1][j+1] %= 10000;
        }
      }
    printf("Case #%d: %04d\n", iii+1, t[n][m]);
  }
  return 0;
}
