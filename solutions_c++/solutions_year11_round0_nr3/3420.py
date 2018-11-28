#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 1005, INF = 1000000005;

int T, N, C [MAXN];

char *solve ()
{
    scanf ("%d", &N);
    int sum = 0, xor_val = 0, least = INF;

    for (int num, i = 0; i < N; i++)
    {
        scanf ("%d", &num);
        sum += num;
        xor_val ^= num;
        least = min (least, num);
    }

    if (xor_val != 0)
        return (char *) "NO";

    char *buf = new char [10];
    sprintf (buf, "%d", sum - least);
    return buf;
}

int main ()
{
    scanf ("%d", &T);

    for (int tc = 1; tc <= T; tc++)
        printf ("Case #%d: %s\n", tc, solve ());

    return 0;
}
