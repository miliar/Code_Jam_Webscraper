#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
//#include <cmath>
using namespace std;
 
#define all(c) ((c).begin()), ((c).end()) 
#define iter(c) __typeof((c).begin())
#define present(c, e) ((c).find((e)) != (c).end()) 
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)
 
typedef long long ll;
 
int main() {
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; t++) {
    int W, H, A;
    scanf("%d%d%d", &W, &H, &A);
    
    printf("Case #%d: ", t);
    
    for (int x1 = -W; x1 <= W; x1++) {
      for (int y1 = -H; y1 <= H; y1++) {
        for (int x2 = max(-W, x1 - W); x2 <= W; x2++) {
          if (abs(x1 - x2) > W) break;

          for (int y2 = max(-H, y1 - H); y2 <= H; y2++) {
            if (abs(y1 - y2) > H) break;

            if (abs(x1 * y2 - y1 * x2) == A) {
              int xmin = min(0, min(x1, x2));
              int ymin = min(0, min(y1, y2));

              printf("%d %d %d %d %d %d\n", -xmin, -ymin, x1 - xmin, y1 - ymin, 
                     x2 - xmin, y2 - ymin);
              goto done;
            }
          }
        }
      }
    }

    puts("IMPOSSIBLE");
    continue;

  done:
    ;
  }
}
