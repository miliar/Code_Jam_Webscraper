#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

const int MAXN = 505, MOD = 100003;

int TC = 1, T, N, binom [MAXN][MAXN], dp [MAXN][MAXN];

int main ()
{
    freopen ("C-large.in", "r", stdin);
    freopen ("C-large.out", "w", stdout);
    
    for (int i = 0; i < MAXN; i++)
    {
        binom [0][i] = 0;
        binom [i][0] = 1;
    }
    
    for (int i = 1; i < MAXN; i++)
        for (int j = 1; j < MAXN; j++)
            binom [i][j] = (binom [i - 1][j] + binom [i - 1][j - 1]) % MOD;
    
    memset (dp, 0, sizeof (dp));
    
    for (int n = 2; n < MAXN; n++)
        dp [n][1] = 1;
    
    for (int n = 2; n < MAXN; n++)
        for (int k = 2; k < n; k++)
            for (int p = 1; p < k; p++)
                dp [n][k] = (dp [n][k] + (long long) binom [n - k - 1][k - p - 1] * dp [k][p]) % MOD;
    
    for (scanf ("%d", &T); TC <= T; TC++)
    {
        scanf ("%d", &N);
        int sum = 0;
        
        for (int k = 1; k < N; k++)
            sum = (sum + dp [N][k]) % MOD;
        
        printf ("Case #%d: %d\n", TC, sum);
    }
    
    //system ("pause");
}
