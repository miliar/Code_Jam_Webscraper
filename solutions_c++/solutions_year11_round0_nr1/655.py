#include <cstdio>
#include <cstring>
using namespace std;

int N;
int O_pos, B_pos, O_time, B_time, cur_time;
char ch; int p;

int ABS(int x) {
    return x > 0 ? x : -x;
}
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ti=1;ti<=T;ti++) {
        printf("Case #%d: ", ti);
        scanf("%d", &N);
        O_pos = 1; B_pos = 1;
        O_time = 0; B_time = 0;
        cur_time = 0;
        for (int i=1;i<=N;i++) {
            scanf(" %c%d", &ch, &p);
            if (ch=='O') {
                B_time += ABS(B_pos - p) + 1;
                B_pos = p;
                if (B_time <= cur_time) B_time = cur_time + 1;
                cur_time = B_time;
            } else {
                O_time += ABS(O_pos - p) + 1;
                O_pos = p;
                if (O_time <= cur_time) O_time = cur_time + 1;
                cur_time = O_time;
            }
        }
        printf("%d\n", cur_time);
    }
    return 0;
}
