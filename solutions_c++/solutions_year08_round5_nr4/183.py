#include <stdio.h>
#include <string.h>

#define MAX_N 100
#define MOD 10007

int X[MAX_N][MAX_N];

int main(void)
{
    int test, tests;
    
    freopen("d.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    scanf("%d", &tests);
    for (test = 1; test <= tests; test++)
    {
        int i, j, H, W, R;

        scanf("%d%d%d", &H, &W, &R);
        memset(X, 0, sizeof(X));
        while (R--)
        {
              scanf("%d%d", &i, &j);
              X[i - 1][j - 1] = -1;
        }
        
        if (!X[0][0])
           X[0][0] = 1;
           
        for (i = 1; i < H; i++)
            for (j = 0; j < W; j++)
                if (!X[i][j])
                {
                   if ((i - 2) >= 0 && (j - 1) >= 0 && X[i - 2][j - 1] >= 0)
                      X[i][j] = X[i - 2][j - 1];
                   if ((i - 1) >= 0 && (j - 2) >= 0 && X[i - 1][j - 2] >= 0)
                      X[i][j] = (X[i][j] + X[i - 1][j - 2]) % MOD;
                }
        if (X[H - 1][W - 1] < 0)
           X[H - 1][W - 1] = 0;
           
        printf("Case #%d: %d\n", test, X[H - 1][W - 1]);
    }
    
    return 0;
}
