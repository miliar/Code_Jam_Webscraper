#include <cstdio>

const int mod = 100003;
const int max_n = 502;
int n;

int result[501];
int DP[max_n + 2][max_n + 1];
int C[max_n + 1][max_n + 1];

void preprocess ()
{
    result[2] = 1;

    DP[2][0] = 0;
    DP[2][1] = 1;
    DP[2][2] = 0;
    C[0][0] = C[1][0] = C[1][1] = 1;
    for (int i = 2; i <= max_n; ++i)
    {
        C[i][i] = C[i][0] = 1;
        for (int j = 1; j < i; ++j)
            C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % mod;
    }

    for (int i = 3; i <= max_n; ++i)
    {
        DP[i][0] = DP[i][i] = 0;
        for (int j = 1; j <= i - 1; ++j)
            for (int k = 1; k < j; ++k)
                DP[i][j] = (DP[i][j] + (DP[j][k] * (long long)(C[i - j - 1][j - k - 1]))) % mod;

        result[i] = 0;
        for (int j = 0; j <= i; ++j)
            result[i] = (result[i] + DP[i][j]) % mod;
    }
}

void gogo (int test)
{
    scanf ("%d", &n);
    printf ("Case #%d: %d\n", test, result[n + 1]);
}

int main ()
{
    preprocess ();
    int tests;
    scanf ("%d", &tests);
    for (int i = 1; i <= tests; ++i) gogo (i);
    return 0;
}