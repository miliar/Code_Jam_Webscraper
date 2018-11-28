#include <cstdio>
#include <cstring>

#define L 600
#define MOD 10000

const char a[] = "welcome to code jam";
const int N = 19;

char s[L];
int f[N][L];    //f[i][j]:前j个s含i个a的个数

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int t, cas;
    scanf("%d", &cas);
    gets(s);
    for (t = 1; t <= cas; ++t)
    {
        int i, j, n;
        gets(s);
        n = strlen(s);
        f[0][0] = (s[0] == a[0]);
        for (j = 1; j < n; ++j)
            f[0][j] = f[0][j-1] + (s[j] == a[0]);
        for (i = 1; i < N; ++i)
        {
            f[i][i] = f[i-1][i] * (s[i] == a[i]);
            for (j = i + 1; j < n; ++j)
                f[i][j] = (f[i][j-1] + f[i-1][j] * (s[j] == a[i])) % MOD;
        }
        printf("Case #%d: %04d\n", t, f[N-1][n-1]);
    }
    return 0;
}
