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

int t[1011][111];
int s, q;
string nazwy[111];

char txt[100000];
string wezstring(void){
  int i;
  fgets(txt, 99999, stdin);
  for (i = 0; txt[i] != '\n' && txt[i]; ++i) ;
  txt[i] = 0;
  return string(txt);
}

int wezint(void){
  fgets(txt, 99999, stdin);
  int x;
  sscanf(txt, "%d", &x);
  return x;
}

const int INF = 1111*1000;

int main(){
  int te;
  te = wezint();
  for(int tt = 1; tt <= te; ++tt){
    s = wezint();
    REP(i, s) nazwy[i] = wezstring();
    q = wezint();
    REP(j, q+1) REP(i, s) t[j][i] = INF;
    REP(i, s) t[0][i] = 0;
    FOR(j, 1, q){
      string x = wezstring();
      REP(i, s){        
        if (x != nazwy[i])
          t[j][i] = min(t[j][i], t[j-1][i]);
        else
          REP(k, s)
            if (i != k)
              t[j][k] = min(t[j][k], t[j-1][i] + 1);
      }
    }
    int w = INF;
    REP(i, s)
      w = min(w, t[q][i]);
    printf("Case #%d: %d\n", tt, w);
  }
	return 0;
}
