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

int main(){
  int te;
  scanf("%d", &te);
  FOR(iii, 1, te){
    int n; scanf("%d", &n);
    int p[2], t[2]; p[0] = p[1] = 1; t[0] = t[1] = 0;
    REP(i, n){
      int x; char str[10]; scanf("%s %d", str, &x);
      int a = (str[0]=='O'?0:1);
      int t1 = max(t[a] + max(x-p[a],p[a]-x), t[1-a]);
      t[a] = t1+1;
      p[a] = x;
    }
    printf("Case #%d: %d\n", iii, max(t[0], t[1]));
  }
  return 0;
}
