#include <cstdio>
#include <cstring>

char G[60][60], R[60][60];
int r[60][60], u[60][60], f1[60][60], f2[60][60];
int n, m;

int Check(char col, int K) {
    for(int i = 0; i < n; i ++)
        for(int j = 0; j < n; j ++) if(R[i][j] == col)
            if(r[i][j] >= K || u[i][j] >= K || f1[i][j] >= K || f2[i][j] >= K)
                return 1;
    return 0;
}
int main() {
    freopen("A-large.in", "r", stdin);
    int T, test = 1;

    for(scanf("%d", &T); T; T --) {
        scanf("%d%d", &n, &m);
        for(int i = 0; i < n; i ++)
            scanf("%s", G[i]);
        memcpy(R, G, sizeof(R));
        for(int i = 0; i < n; i ++)
            for(int j = 0; j < n; j ++)
                G[j][n - 1 - i] = R[i][j];
        memset(R, '.', sizeof(R));
        for(int j = 0; j < n; j ++) {
            int k = n - 1;
            for(int i = n - 1; i >= 0; i --)
                if(G[i][j] != '.')
                    R[k --][j] = G[i][j]; 
        }

        for(int i = 0; i < n; i ++)
            for(int j = 0; j < n; j ++) {
                if(j && R[i][j - 1] == R[i][j])
                    r[i][j] = r[i][j - 1] + 1;
                else
                    r[i][j] = 1;

                if(i && R[i - 1][j] == R[i][j])
                    u[i][j] = u[i - 1][j] + 1;
                else
                    u[i][j] = 1;
            }

        for(int i = 0; i < n; i ++)
            for(int j = 0; j < n; j ++) {
                if(i && j && R[i - 1][j - 1] == R[i][j])
                    f1[i][j] = f1[i - 1][j - 1] + 1;
                else
                    f1[i][j] = 1;

                if(i && j + 1 < n && R[i - 1][j + 1] == R[i][j])
                    f2[i][j] = f2[i - 1][j + 1] + 1;
                else
                    f2[i][j] = 1;
            }
        int g1 = Check('R', m);
        int g2 = Check('B', m);
        
        printf("Case #%d: ", test ++);

        if(g1 || g2) {
            if(g1 && g2)
                printf("Both\n");
            else if(g1)
                printf("Red\n");
            else
                printf("Blue\n");
        } else
            printf("Neither\n");
    }
    return 0;
}

