#include <cstdio>

#define abs(x) ((x >= 0) ? (x) : (-(x)))
#define min(x, y) (((x) < (y)) ? (x) : (y))

int main (void)
{
    int tasks[100];
    int blue[100];
    int orange[100];
    int T, N;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        int bn = 0, on = 0;
        scanf("%d", &N);
        getchar();
        for (int i = 0; i < N; i++) {
            int position;
            char player;
            scanf("%c %d", &player, &position);
            getchar();
//            printf("%c %d", player, position);
            tasks[i] = player;
            if (player == 'B') {
                blue[bn++] = position;
            } else {
                orange[on++] = position;
            }
        }
        int blue_next, orange_next;
        int blue_cur = 1, orange_cur = 1;
        int min_steps = 0;
        int bi = 0, oi = 0;
        if (bn > 0)
            blue_next = blue[0];
        if (on > 0)
            orange_next = orange[0];
        for (int i = 0; i < N; i++) {
//            printf(" %d %d\n", blue_next, orange_next);
            if (tasks[i] == 'B') {
                min_steps += (abs(blue_next - blue_cur) + 1);
                if (oi < on) {
                    if (abs(orange_next - orange_cur) <= abs(blue_next - blue_cur) + 1) {
                        orange_cur = orange_next;
                    } else {
                        if (orange_cur < orange_next) {
                            orange_cur += (abs(blue_next - blue_cur) + 1);
                        } else {
                            orange_cur -= (abs(blue_next - blue_cur) + 1);
                        }
                    }
                }
                blue_cur = blue_next;
                if (++bi < bn)
                    blue_next = blue[bi];
            } else {
                min_steps += (abs(orange_next - orange_cur) + 1);
                if (bi < bn) {
                    if (abs(blue_next - blue_cur) <= abs(orange_next - orange_cur)) {
                        blue_cur = blue_next;
                    } else {
                        if (blue_cur < blue_next) {
                            blue_cur += (abs(orange_next - orange_cur) + 1);
                        } else {
                            blue_cur -= (abs(orange_next - orange_cur) + 1);
                        }
                    }
                }
                orange_cur = orange_next;
                if (++oi < on)
                    orange_next = orange[oi];
            }
//            printf("%d %d\n", blue_cur, orange_cur);
        }
        printf("Case #%d: %d\n", t, min_steps);
    }
    return 0;
}


