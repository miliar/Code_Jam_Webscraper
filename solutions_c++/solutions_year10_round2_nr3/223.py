#include <cstdio>
#include <string>
int M = 100003;
const int maxn = 1000;
int f[maxn][maxn];
int C[maxn][maxn];

int find(int i,int j)
{
    if (f[i][j] != -1)
        return f[i][j];
    if (j == 1)
    {
        f[i][j] = 1;
        return 1;
    }
    if (i <= j)
    {
        f[i][j] = 0; 
        return 0;
    }
    f[i][j] = 0;
    for (int k = 1; k < j; ++k)
        if (i - j >= j - k)
        {
            long long tmp = ((long long)find(j,k) * (long long) C[i-j-1][j-k-1]) % (long long)M;
            f[i][j] = (f[i][j] + (long long)tmp) % M;
        }
    return f[i][j];
}


int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int Test; 
    scanf("%d",&Test);
    int n = 500;
    memset(f,-1,sizeof(f));
    C[0][0] = 1;
    for (int i = 1; i <= 500; ++i)
    {
        C[i][0] = 1;
        for (int j = 1; j <= i; ++j)
        {
            C[i][j] = (C[i-1][j-1] + C[i-1][j]) % M;
       // printf("%d %d %d\n",i,j,C[i][j]);
        }
    }
            
    for (int i = 1; i <= 500; ++i)
        for (int j = 1; j <= i; ++j)
            f[i][j] = find(i,j);
    for (int T = 1; T <= Test; ++T)
    {
        scanf("%d",&n);
        int ans = 0;
        for (int i = 1; i < n; ++i)
            ans = (ans + f[n][i]) % M;
        
        printf("Case #%d: %d\n",T,ans);
    }
    return 0;
}
