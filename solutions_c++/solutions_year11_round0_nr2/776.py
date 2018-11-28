#include <cstdio>
#include <cstring>
using namespace std;

const int MAXN = 105;

int C;
char c[MAXN][3 + 1];
int D;
char d[MAXN][2 + 1];
int N;
char s[MAXN];
int R;
char res[MAXN];

bool combine() {
    int i;

    for (i = 0; i < C; i++) {
        if (c[i][0] == res[R - 1] && c[i][1] == res[R - 2]) break;
        if (c[i][0] == res[R - 2] && c[i][1] == res[R - 1]) break;
    }
    if (i == C) return false;
    R -= 2;
    res[R++] = c[i][2];
    return true;
}

void opposed() {
    int i, j;

    for (i = 0; i < R - 1; i++) {
        for (j = 0; j < D; j++) {
            if ((d[j][0] == res[R - 1] && d[j][1] == res[i]) || (d[j][1] == res[R - 1] && d[j][0] == res[i])) {
                R = 0;
                return;
            }
        }
    }
}

int main() {
    int t, casN = 0;
    int i;

    scanf("%d", &t);
    while (t-- > 0) {
        scanf("%d", &C);
        for (i = 0; i < C; i++) {
            scanf("%s", c[i]);
        }
        scanf("%d", &D);
        for (i = 0; i < D; i++) {
            scanf("%s", d[i]);
        }
        scanf("%d", &N);
        scanf("%s", s);
        R = 0;
        for (i = 0; i < N; i++) {
            res[R++] = s[i];
            if (combine()) continue;
            opposed();
        }
        printf("Case #%d: [", ++casN);
        for (i = 0; i < R; i++) {
            printf("%s%c", (i > 0) ? ", " : "", res[i]);
        }
        puts("]");
    }

    return 0;
}

