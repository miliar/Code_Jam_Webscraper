#include <cstdio>
#include <cstdlib>

#define max(a, b) ((a) > (b) ? (a) : (b))

int main() {
    int t, n, i, p, c = 1;
    int ot, bt, op, bp;
    char cl;
    scanf("%d", &t);
    while (t--) {
          scanf("%d ", &n);
          op = bp = 1; ot = bt = 0;
          while (n--) {
                scanf("%c %d ", &cl, &p);
                // We will update the current time of the bot to the time of last button push
                if (cl == 'O') ot = max(ot + abs(p - op), bt) + 1, op = p;
                else bt = max(bt + abs(p - bp), ot) + 1, bp = p;
                // printf("%d %d %d %d\n", ot, bt, op, bp);
          }
          // printf("\n");
          printf("Case #%d: %d\n", c++, max(ot, bt));
    }
    return 0;
}
