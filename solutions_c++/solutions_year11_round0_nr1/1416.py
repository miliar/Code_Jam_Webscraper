#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int idiff(int x, int y) { return x < y ? y - x : x - y; }

int main() {
  int T; scanf("%d", &T);
  for(int t = 1; t <= T; t++) {
    int N; scanf("%d", &N);
    int tcur = 0;
    int tb = 0;
    int to = 0;
    int pb = 0;
    int po = 0;
    for(int i = 0; i < N; i++) {
      char cmd[2];
      int pos;
      scanf("%s %d", cmd, &pos); pos--;
      if(*cmd == 'B') {
        tcur = tb = max(tcur + 1, 1 + tb + idiff(pb, pos));
        pb = pos;
      } else {
        tcur = to = max(tcur + 1, 1 + to + idiff(po, pos));
        po = pos;
      }
    }
    printf("Case #%d: %d\n", t, tcur);
  }
}
