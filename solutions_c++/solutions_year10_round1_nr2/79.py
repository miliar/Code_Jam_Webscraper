#include<iostream>
#include<algorithm>
using namespace std;
int A[128];
int D, I, N, M;
int f[128][256];
void CMIN(int & a, int b)
{
     if(b < a) a = b;
}
int Abs(int a)
{
    return a < 0 ? -a : a;
}
int main()
{
    int t, cs = 0;
    int i, j, k, tmp, mi;
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d%d%d", &D, &I, &M, &N); 
        for(i = 1; i <= N; ++i)
            scanf("%d", &A[i]);
        memset(f, 63, sizeof(f));
        for(i = 0; i < 256; ++i)
           f[0][i] = 0;
        for(i = 1; i <= N; ++i)
        {
            for(j = M; j < 256; ++j)
            {
                mi = f[i-1][j];
                for(k = j - 1; k >= j - M; --k)
                   CMIN(mi, f[i-1][k]);
                CMIN(f[i-1][j], mi + I);
            }
            for(j = 255 - M; j >= 0; --j)
            {
                mi = f[i-1][j];
                for(k = j + 1; k <= j + M; ++k)
                   CMIN(mi, f[i-1][k]);
                CMIN(f[i-1][j], mi + I);
            }
            
            for(j = 0; j < 256; ++j)
            {
                  CMIN(f[i][j], f[i-1][j] + D);
                  
                  for(k = 0; k <= 256; ++k)
                  {
                        if(Abs(j - k) <= M)
                        {
                            CMIN(f[i][j], f[i-1][k] + Abs(j - A[i]));
                        }
                  }
                  
                  //printf("%d %d %d\n", i, j, f[i][j]);
            }
        }
        
        int res = 1 << 30;
        for(i = 0; i < 256; ++i)
           if(f[N][i] < res) res = f[N][i];
        printf("Case #%d: %d\n", ++cs, res);
    }
}
