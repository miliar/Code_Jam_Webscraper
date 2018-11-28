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

char zmien[30][30];
vector<pair<char, char> > zabij;
char t[1000];
vector<char> v;
int s[30];

int main(){
  int te; scanf("%d", &te);
  FOR(iii, 1, te){
    printf("Case #%d: [", iii);
    REP(i, 30) REP(j, 30) zmien[i][j] = 0;
    zabij.clear(); v.clear();
    REP(i, 30) s[i] = 0;
    int n;
    scanf("%d", &n);
    REP(i, n){
      scanf("%s", t);
      zmien[t[0]-'A'][t[1]-'A'] = zmien[t[1]-'A'][t[0]-'A'] = t[2];
    }
    scanf("%d", &n);
    REP(i, n){
      scanf("%s", t);
      zabij.PB(MP(t[0], t[1]));
    }
    scanf("%d %s", &n, t);
    REP(i, n){
      v.PB(t[i]);
      s[t[i]-'A']++;
      int m = SIZE(v);
      while(m >= 2 && zmien[v[m-1]-'A'][v[m-2]-'A']){
        s[v[m-1]-'A']--;
        s[v[m-2]-'A']--;
        v[m-2] = zmien[v[m-1]-'A'][v[m-2]-'A'];
        s[v[m-2]-'A']++;
        v.pop_back();
      }
      FOREACH(it, zabij)
        if (s[it->ST-'A'] > 0 && s[it->ND -'A'] > 0){
          v.clear();
          REP(j, 30) s[j] = 0;
          break;
        }
    }
    int m = SIZE(v);
    REP(i, m){
      if (i) printf(", ");
      printf("%c", v[i]);
    }
    printf("]\n");
  }
  return 0;
}
