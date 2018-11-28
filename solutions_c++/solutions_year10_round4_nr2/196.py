#include <cstdio>

const int P = 11;
const int MAX = (1<<P);
const int INF = 1<<29;

int e;
int M[MAX];
int f[MAX][P];

int main()
{
//    freopen("in.txt","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t, p, ticket, m, cas = 0;
    scanf("%d", &t);
    while (t--){
        scanf("%d", &p);
        int size = 1<<p;
        for (int i = 0; i < size; ++i){
            scanf("%d", &M[i]);
            for (int j = 0; j <= M[i]; ++j) f[i][j] = 0;
            for (int j = M[i]+1; j <= p; ++j) f[i][j] = INF;
        }
        for (int k = p-1; k >= 0; --k){
            int g[MAX][P]={};
            size = 1<<k;
            for (int i = 0; i < size; ++i){
                scanf("%d", &ticket);
                for (int j = 0; j <= p; ++j) g[i][j] = INF;
                for (int x = 0; x <= p; ++x){
                    if (f[i*2][x] == INF) continue;
                    for (int y = 0; y <= p; ++y){
                        if (f[i*2+1][y] == INF) continue;
                        m = x < y ? x : y;
                        if (g[i][m] > f[i*2][x]+f[i*2+1][y]+ticket) g[i][m] = f[i*2][x]+f[i*2+1][y]+ticket;
                        if (m && g[i][m-1] > f[i*2][x]+f[i*2+1][y]) g[i][m-1] = f[i*2][x]+f[i*2+1][y];
                    }
                }
            }
            for (int i = 0; i < size; ++i)
                for (int j = 0; j <= p; ++j)
                    f[i][j] = g[i][j];
        }
//        int ans = INF;
//        for (int i = 0; i <= p; ++i)
//            if (ans > f[0][i]) ans = f[0][i];
        printf("Case #%d: %d\n", ++cas, f[0][0]);
    }
    return 0;
}
