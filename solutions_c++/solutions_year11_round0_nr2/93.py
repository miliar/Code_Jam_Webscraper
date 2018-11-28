#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
    int cases, C, D, n;
    char tmp[1992], a[1994], f[256][256], g[256][256];
    scanf("%d", &cases);
    for (int T = 1; T <= cases; T++) {
        memset(f, 0, sizeof(f));
        memset(g, 0, sizeof(g));
        for (scanf("%d", &n); n--; ) {
            scanf("%s", tmp);
            f[tmp[0]][tmp[1]] = f[tmp[1]][tmp[0]] = tmp[2];
        }
        for (scanf("%d", &n); n--; ) {
            scanf("%s", tmp);
            g[tmp[0]][tmp[1]] = g[tmp[1]][tmp[0]] = true;
        }
        scanf("%d%s", &n, tmp);
        int size = 0;
        for (char *p = tmp; *p; p++) {
            if (size && f[a[size-1]][*p])
                a[size-1] = f[a[size-1]][*p];
            else
                a[size++] = *p;
            for (int i = 0; i < size-1; i++)
                if (g[a[i]][a[size-1]])
                    size = 0;
        }
        printf("Case #%d: [", T);
        for (int i = 0; i < size; i++) {
            if (i) printf(", ");
            putchar(a[i]);
        }
        puts("]");
    }
}
