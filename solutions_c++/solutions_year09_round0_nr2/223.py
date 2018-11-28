#include <stdio.h>

const int maxn = 100 + 10;
const int di[] = {-1, 0, 0, 1};
const int dj[] = {0, -1, 1, 0};

char mk[maxn*maxn];
int hight[maxn][maxn], f[maxn*maxn], N, M;

int get(int k)
{
    if (f[k] != k) f[k] = get(f[k]);
    return f[k];
}

int main(void)
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int tot, cas = 0;
    scanf("%d", &tot);
    while (tot--) {
        ++cas;
        scanf("%d%d", &N, &M);
        for (int i = 0; i < N; ++i)
        for (int j = 0; j < M; ++j)
            scanf("%d", &hight[i][j]);
        
        for (int k = 0; k < N*M; ++k) f[k] = k, mk[k] = '\0';
        
        for (int i = 0; i < N; ++i)
        for (int j = 0; j < M; ++j) {
            int mh = -1, u, v;
            for (int k = 0; k < 4; ++k) {
                int x = i + di[k];
                int y = j + dj[k];
                if (x<0 || x>=N) continue;
                if (y<0 || y>=M) continue;
                if (mh==-1 || hight[x][y]<mh) {
                    mh = hight[x][y];
                    u = x;
                    v = y;
                }
            }
            if (mh < hight[i][j]) {
                int ra = get(i*M+j), rb = get(u*M+v);
                f[ra] = rb;
            }
        }
        
        printf("Case #%d:\n", cas);
        char cnt = 'a';
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                int ra = get(i*M+j);
                if (mk[ra] == 0) mk[ra] = cnt++;
                printf("%c", mk[ra]);
                if (j+1 < M) printf(" ");
            }
            printf("\n");
        }
    }
    return 0;
}
