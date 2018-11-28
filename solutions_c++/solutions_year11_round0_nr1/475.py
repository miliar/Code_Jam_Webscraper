#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <climits>
#include <cctype>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>

#define FOR(i, m, n) for (int i=m; i<n; i++)

using namespace std;

int N;
int OT, OP, BT, BP;

int main() {
  int vstupy; scanf("%d", &vstupy);
  FOR (qq, 0, vstupy) {
    scanf("%d", &N);
    char c; int d; OT = 0; BT = 0; OP = 1; BP = 1;
    FOR (i, 0, N) {
      scanf(" %c%d", &c, &d);
      if (c=='O') {
        OT += abs(OP-d)+1;
        OT = (OT<=BT)?(BT+1):OT;
        OP = d;
      }
      else if (c=='B') {
        BT += abs(BP-d)+1;
        BT = (BT<=OT)?(OT+1):BT;
        BP = d;
      }
    }
    printf("Case #%d: %d\n", qq+1, max(OT, BT));
  }
  return 0;
}
