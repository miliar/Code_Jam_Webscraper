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

int l, d, n;
char dict[5001][100];
char txt[1000*2000];
int pat[100][30];

int main(){
  scanf("%d%d%d", &l, &d, &n);
  REP(i, d)
    scanf("%s", dict[i]);
  REP(i, n){
    scanf("%s", txt);
    int j = 0;
    REP(k, l){
      REP(a, 30) pat[k][a] = 0;
      if (txt[j] == '('){
        j++;
        while (txt[j] != ')')
          pat[k][txt[j++]-'a'] = 1;
        ++j;
      } else
        pat[k][txt[j++]-'a'] = 1;
    }
    int cnt = 0;
    REP(a, d){
      bool ok = true;
      REP(k, l)
        if (!pat[k][dict[a][k]-'a']){
          ok = false; break;
        }
      if (ok) cnt++;
    }
    printf("Case #%d: %d\n", i+1, cnt);
  }
  return 0;
}
