#include <stdio.h>
#include <algorithm>
using namespace std;
int T, N, ans, timeO, timeB, pos, posO, posB;
char buf[10], pre;
FILE *fin = fopen("input.in", "r");
FILE *fout = fopen("output.out", "w");

int main() {
    fscanf(fin, "%d", &T);
    for(int t = 0; t < T; t++) {
        fscanf(fin, "%d", &N);
        ans = timeO = timeB = 0;
        posO = posB = 1;
        pre = 0;
        for(int i = 0; i < N; i++) {
            fscanf(fin, "%s%d", &buf, &pos);
            if (buf[0] == 'O') {
                int need = abs(pos - posO);
                posO = pos;
                if (pre == 'O') {
                    timeB += need + 1;
                    ans += need + 1;
                }
                else {
                    if (timeO >= need) {
                        ans++;
                        timeB = 1;
                    }
                    else {
                        ans += need - timeO + 1;
                        timeB = need - timeO + 1;
                    }
                }
                timeO = 0;
            }
            else {
                int need = abs(pos - posB);
                posB = pos;
                if (pre == 'B') {
                    timeO += need + 1;
                    ans += need + 1;
                }
                else {
                    if (timeB >= need) {
                        ans++;
                        timeO = 1;
                    }
                    else {
                        ans += need - timeB + 1;
                        timeO = need - timeB + 1;
                    }
                }
                timeB = 0;
            }
            pre = buf[0];
        }
        fprintf(fout, "Case #%d: %d\n", t + 1, ans);
    }
}
