#include <cstdio>
#include <cstring>
using namespace std;

const int MAXL = 505, MOD = 10000;
const char *WELCOME = "welcome to code jam";

int N, L, dp [MAXL][20];
char str [MAXL];

int solve (int n, int w)
{
    if (w == 19)
        return 1;

    if (n == L)
        return 0;

    if (dp [n][w] != -1)
        return dp [n][w];

    dp [n][w] = solve (n + 1, w);

    if (str [n] == WELCOME [w])
        dp [n][w] = (dp [n][w] + solve (n + 1, w + 1)) % MOD;

    return dp [n][w];
}

int main ()
{
    scanf ("%d", &N);

    for (int n = 1; n <= N; n++)
    {
        do
            gets (str);
        while (strlen (str) == 0);

        L = strlen (str);
        memset (dp, -1, sizeof (dp));
        printf ("Case #%d: %04d\n", n, solve (0, 0));
    }

    return 0;
}
