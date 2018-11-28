#include <algorithm>
#include <cctype>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <bitset>
#include <cmath>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <valarray>
#include <vector>

#define REP(i,a,b) for((i)=(a);(i)<(int)(b);(i)++)
#define rep(i,b)   REP(i,0,b)
#define FOR(i,c)   for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c)     (c).begin(), (c).end()

using namespace std;
typedef long long ll;
const double eps = 1e-10;
const int inf = 1<<25;

int in() { int x; scanf("%d", &x); return x; }

int main() {
  int i, j, k, tcc;
  int tc = in();
  for (tcc = 1; tc--; tcc++) {
    int n =in(), pd = in(), pg = in();
    bool ok = 1;
    if (pg == 100 and pd != 100) ok = 0;
    if (pg == 0 and pd) ok = 0;
    k = pd;
    if (k % 100) {
      int n2 = 0, n5 = 0;
      if (k % 2 == 0) n2 = 1;
      if (k % 4 == 0) n2 = 2;
      if (k % 5 == 0) n5 = 1;
      if (k % 25 == 0) n5 = 2;
      if (n2 == 0 and n5 == 0 and n < 100) ok = 0;
      if (n2 == 1 and n5 == 0 and n < 50) ok = 0;
      if (n2 == 0 and n5 == 1 and n < 20) ok = 0;
      if (n2 == 1 and n5 == 1 and n < 10) ok = 0;

      if (n2 == 2 and n5 == 0 and n < 25) ok = 0;
      if (n2 == 0 and n5 == 2 and n < 4) ok = 0;
      if (n2 == 1 and n5 == 2 and n < 2) ok = 0;
      if (n2 == 2 and n5 == 1 and n < 5) ok = 0;
    } else {
    }
    printf("Case #%d: ", tcc);
    if (ok) puts("Possible"); else puts("Broken");
  }
  return 0;
}













