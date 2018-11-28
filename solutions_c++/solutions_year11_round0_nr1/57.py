#include <stdio.h>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
  int tests; scanf("%d",&tests);
  for (int tt=1;tt<=tests;++tt) {
    int n; scanf("%d",&n);
    int ot, op, bt, bp, t;
    ot = bt = t = 0;
    op = bp = 1;
    while (n--) {
      char c[2]; int p; scanf("%s %d",c,&p);
      int *st = &ot;
      int *sp = &op;
      if (c[0]=='B') {st=&bt;sp=&bp;}
      *st = t = max(t, *st + abs(*sp - p)) + 1;
      *sp = p;
    }
    printf("Case #%d: %d\n", tt, t);
  }
}
