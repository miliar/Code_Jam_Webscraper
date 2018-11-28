#include <stdio.h>

typedef long long LL;

LL comb(LL n, LL k)
{
   LL res = 1, i;
   if (n < k)
      return 0;
   for (i = n - k + 1; i <= n; i++)
       res *= i;
   //for (i = 1; i <= k; i++)
   //    res /= i;
   return res;
}

int main(void)
{
    int tests, t;
    
    freopen("a2.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    scanf("%d", &tests);
    for (t = 1; t <= tests; t++)
    {
        LL CC[3][3], N, A, B, C, D, X, Y, M, cnt = 0LL;
        int i, j, k, l, m, n;
        
        for (i = 0; i < 3; i++)
            for (j = 0; j < 3; j++)
                CC[i][j] = 0;
                
        scanf("%lld %lld %lld %lld %lld %lld %lld %lld", &N, &A, &B, &C, &D, &X, &Y, &M);
        for (i = 0; i < N; i++)
        {
            CC[X % 3][Y % 3]++;
            X = (A * X + B) % M;
            Y = (C * Y + D) % M;
        }
        
        for (i = 0; i < 3; i++)
            for (j = 0; j < 3; j++)
                for (k = 0; k < 3; k++)
                    for (l = 0; l < 3; l++)
                        for (m = 0; m < 3; m++)
                            for (n = 0; n < 3; n++)
                                if (((i + j + k) % 3) == 0 && ((l + m + n) % 3) == 0)
                                   if (i == j && j == k && l == m && m == n)
                                      cnt += comb(CC[i][l], 3);
                                   else if (i == j && l == m)
                                        cnt += comb(CC[i][l], 2) * CC[k][n];
                                   else if (j == k && m == n)
                                        cnt += CC[i][l] * comb(CC[j][m], 2);
                                   else if (i == k && l == n)
                                        cnt += comb(CC[i][l], 2) * CC[j][m];
                                   else cnt += CC[i][l] * CC[j][m] * CC[k][n];
                                   
        printf("Case #%d: %lld\n", t, cnt / 6);
    }
    
    return 0;
}
