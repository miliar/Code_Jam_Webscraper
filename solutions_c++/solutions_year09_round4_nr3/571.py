#include<stdio.h>
#include<string.h>
#include<stdlib.h>

const int maxn = 105;
int T, N, K, pr[maxn][30], used[maxn], cas, ans;
int g[maxn][maxn];

void input()
{
    int i, j, k; 
    scanf("%d%d", &N, &K);
    memset(g, 0, sizeof(g));
    for (i=0;i<N;i++){
       for (j=0;j<K;j++) scanf("%d", &pr[i][j]);
       for (j=0;j<i;j++){
          for (k=0;k<K;k++)
             if (pr[i][k] == pr[j][k]) g[i][j] = g[j][i] = 1;
          for (k=1;k<K;k++)
             if (pr[i][k-1] >= pr[j][k-1] && pr[i][k] <= pr[j][k] ||
                 pr[i][k-1] <= pr[j][k-1] && pr[i][k] >= pr[j][k])
                 g[i][j] = g[j][i] = 1;
       }
    }
    for (i=0;i<N;i++)
      for (j=0;j<N;j++) g[i][j] = 1-g[i][j];
}

int v[20][20], vn[20];

void search(int nd, int dp)
{
    int i, j, k;
    if (dp >= ans) return ;
    if (nd >= N){
        if (dp < ans) ans = dp;
    }
    for (i = 0; i < dp; i++ ){
        for (j=0;j<vn[i];j++)
           if (!g[nd][v[i][j]]) break;
        if (j>=vn[i]){
           v[i][vn[i]++] = nd;
           search(nd+1, dp);
           vn[i] --;
        }
    }
    vn[dp] = 1;
    v[dp][0] = nd;
    search(nd+1, dp+1);
}

void work()
{
    int i;
    memset(v, 0, sizeof(v));
    memset(vn, 0, sizeof(vn));
    vn[0] = 1;
    v[0][0] = 0;
    ans = maxn;
    search(1, 1);
}

int main()
{
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
    scanf("%d", &T);
    for (cas = 1; cas <= T; cas ++){
        input();
        work();
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
