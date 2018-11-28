#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 10005;

int T, N, V, gate [MAXN], change [MAXN], dp [MAXN][2];

inline void solve (int num)
{
    if (2 * num > N)
    {
        dp [num][gate [num]] = 0;
        dp [num][gate [num] ^ 1] = MAXN;
    }
    else
    {
        dp [num][0] = dp [num][1] = MAXN;

        for (int i = 0; i < 2; i++)
            for (int j = 0; j < 2; j++)
                if (gate [num] == 1)
                    dp [num][i & j] = min (dp [num][i & j], dp [2 * num][i] + dp [2 * num + 1][j]);
                else if (gate [num] == 0)
                    dp [num][i | j] = min (dp [num][i | j], dp [2 * num][i] + dp [2 * num + 1][j]);

        if (change [num] == 0)
            return;

        for (int i = 0; i < 2; i++)
            for (int j = 0; j < 2; j++)
                if (gate [num] == 0)
                    dp [num][i & j] = min (dp [num][i & j], dp [2 * num][i] + dp [2 * num + 1][j] + 1);
                else if (gate [num] == 1)
                    dp [num][i | j] = min (dp [num][i | j], dp [2 * num][i] + dp [2 * num + 1][j] + 1);
    }
}

int main ()
{
    scanf ("%d", &T);

    for (int t = 1; t <= T; t++)
    {
        scanf ("%d %d", &N, &V);

        for (int i = 1; i <= N; i++)
        {
            scanf ("%d", gate + i);

            if (2 * i <= N)
                scanf ("%d", change + i);
            else
                change [i] = 0;
        }

        for (int i = N; i > 0; i--)
            solve (i);

        printf ("Case #%d: ", t);

        if (dp [1][V] < MAXN)
            printf ("%d\n", dp [1][V]);
        else
            printf ("IMPOSSIBLE\n");
    }

    return 0;
}
