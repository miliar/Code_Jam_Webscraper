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
#include <cstring>
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

char s[100];
int c[10];
int n;

bool upg(int m){
  int d = s[m-1]-'0';
  c[d]++;
  int e = d + 1;
  while (e < 10){
    if (c[e] > 0)
      break;
    e++;
  }
  if (e == 10) return false;
  c[e]--;
  s[m-1] = '0' + e;
  FORD(i, m-2, 0){
    REP(j, 10) if (c[j]){
      c[j]--;
      s[i] = '0' + j;
      break;
    }
  }
  s[n] = 0;
  return true;
}
int main(){
  int te;
  scanf("%d", &te);
  FOR(iii, 1, te){
    REP(i, 10) c[i] = 0;
    scanf("%s", s);
    n = strlen(s);
    reverse(s, s+n);
    bool ok = false;
    c[s[0]-'0']++;
    FOR(i, 2, n)
      if (upg(i)){
        ok = true;
        break;
      }
    if (!ok){
      ++n; c[0]++;
      int e = 1; while (c[e] == 0) ++e;
      c[e]--;
      s[n] = 0;
      s[n-1] = '0' + e;
      FORD(i, n-2, 0){
        REP(j, 10) if (c[j]){
          c[j]--;
          s[i] = '0' + j;
          break;
        }
      }
    }
    reverse(s, s+n);
    printf("Case #%d: %s\n", iii, s);
  }
  return 0;
}
