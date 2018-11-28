#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 45;

int T, N, len [MAXN];
char str [MAXN];

int main ()
{
    scanf ("%d", &T);

    for (int tc = 1; tc <= T; tc++)
    {
        scanf ("%d", &N);

        for (int i = 0; i < N; i++)
        {
            scanf ("%s", str);
            len [i] = 0;

            for (int j = 0; j < N; j++)
                if (str [j] == '1')
                    len [i] = j;
        }

        int total = 0;

        for (int i = 0; i < N; i++)
            for (int j = i; j < N; j++)
                if (len [j] <= i)
                {
                    total += j - i;

                    while (j > i)
                    {
                        swap (len [j], len [j - 1]);
                        j--;
                    }

                    break;
                }

        printf ("Case #%d: %d\n", tc, total);
    }

    return 0;
}
