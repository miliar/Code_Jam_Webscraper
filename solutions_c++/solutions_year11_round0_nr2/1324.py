#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define N 256

int p[N][N], in[N];
char q[105];
bool op[N][N];
char s[105];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t, cas = 0;
    scanf("%d", &t);
    while (t--) {
        int c;

        scanf("%d", &c);
        memset(p, -1, sizeof(p));
        while (c--) {
            char ss[5];
            scanf("%s", ss);
            p[ ss[0] ][ ss[1] ] = ss[2];
            p[ ss[1] ][ ss[0] ] = ss[2];
        }

        int d;
        scanf("%d", &d);
        memset(op, 0, sizeof(op));
        while (d--) {
            char ss[5];
            scanf("%s", ss);
            op[ ss[0] ][ ss[1] ] = 1;
            op[ ss[1] ][ ss[0] ] = 1;
        }

        int n;
        scanf("%d", &n);
        scanf("%s", s);
        int l = 0, r = 0;
        memset(in, 0, sizeof(in));
        for (int i = 0; i < n; ++i) {
            q[r++] = s[i];
            ++in[ s[i] ];
            while (r-l >= 2) {
                if (p[ q[r-1] ][ q[r-2] ] != -1) {
                    char x = p[ q[r-1] ][ q[r-2] ];
                    --in[ q[r-1] ]; --in[ q[r-2] ];
                    r -= 2;
                    q[r++] = x;
                    ++in[x];
                } else
                    break;
            }
            if (r-l >= 2) {
                bool ok = 0;
                for (int i = 0; i < N; ++i) if (in[i])
                    if (op[i][ q[r-1] ]) {
                        ok = 1;
                        break;
                    }
                if (ok) {
                    l = 0; r = 0;
                    memset(in, 0, sizeof(in));
                }
            }
        }

        printf("Case #%d: [", ++cas);
        if (l < r) {
            printf("%c", q[l]);
            for (int i = l+1; i < r; ++i)
                printf(", %c", q[i]);
        }
        puts("]");
    }
    return 0;
}
