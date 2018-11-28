#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>

using namespace std;

#define LET(x,a) typeof(a) x(a)
#define FOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define REP(i,n) FOR(i,0,n)
#define EACH(x,v) FOR(x,(v).begin(),(v).end())
#define sz size()
#define pb push_back
#define DBG(x) cerr<< #x << " --> "<< x << "\t"
#define DBE(x) cerr<< #x << " --> "<< x << "\n"
#define GI ({int t; scanf(" %d", &t); t;})
typedef pair<int,int> PII;
typedef long long LL;

using namespace std;

map<PII, bool> M;

bool wins(int a, int b) {
  if (a > b) return wins(b,a);
  if (a == b) return 0;
  if (M.find(PII(a,b)) != M.end())
    return M[PII(a,b)];
  //DBG(a), DBE(b);
  if (b%a == 0)
    return M[PII(a,b)] = 1;
  bool lose = true;
  int B = b - a;
  while (B > 0) {
    if (!wins(a,B)) {
      lose = false;
      break;
    }
    B -= a;
  }
  return M[PII(a,b)] = !lose;
}

int main() {
  int T = GI;
  REP(kase, T) {
    int A1 = GI, A2 = GI, B1 = GI, B2 = GI;
    int ans = 0;
    fprintf(stderr, "Case #%d\n", kase+1);
    FOR(a, A1, A2+1) FOR(b, B1, B2+1) {
      if (wins(a,b)) ans++;
    }
    printf("Case #%d: %d\n", kase+1, ans);
  }
  return 0;
}
