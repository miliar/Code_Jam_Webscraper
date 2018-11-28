#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 1005, MAXK = 20;

int T, N, K, best, perm [MAXK];
char str [MAXN], temp [MAXN];

int main ()
{
    scanf ("%d", &T);

    for (int t = 1; t <= T; t++)
    {
        scanf ("%d %s", &K, str);
        N = strlen (str);

        for (int i = 0; i < K; i++)
            perm [i] = i;

        memcpy (temp, str, sizeof (str));
        best = MAXN;

        do
        {
            for (int i = 0; i < N; i += K)
                for (int j = 0; j < K; j++)
                    str [i + j] = temp [i + perm [j]];

            int count = 0;
            char last = '.';

            for (int i = 0; i < N; i++)
                if (str [i] != last)
                {
                    count++;
                    last = str [i];
                }

            best = min (best, count);

            memcpy (str, temp, sizeof (str));
        }
        while (next_permutation (perm, perm + K));

        printf ("Case #%d: %d\n", t, best);
    }

    return 0;
}
