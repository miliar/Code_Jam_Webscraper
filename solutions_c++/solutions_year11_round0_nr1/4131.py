#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
using namespace std;
typedef long long i64;

int main() {
  int T;
  scanf("%d", &T);
  for (int Ti = 1; Ti <= T; ++Ti) {
    fprintf(stderr, "Case #%d of %d...\n", Ti, T);
    // solve
    int pos[2] = {1, 1};
    int idle[2] = {0, 0};
    int cur = 0;
    int tick = 0;
    int dist = 0;
    //
    int n;
    char color[2];
    int button;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
      scanf("%s %d", color, &button);
      //fprintf(stderr, "color=%s, button=%d\n", color, button);
      // make a push
      cur = (color[0] == 'O') ? 0 : 1;
      dist = abs(pos[cur] - button);
      // cur could start moving while the other was buzy
      if (idle[cur] > 0) {
        dist -= min(dist, idle[cur]);
        idle[cur] = 0;
      }
      // still dist steps to go... and one tick for pushing the button
      tick += dist + 1;
      pos[cur] = button;
      // the other is free to do anything in the meantime
      idle[1 - cur] += dist + 1;
    }
    //
    printf("Case #%d: %d\n", Ti, tick);
  }
  return 0;
}
