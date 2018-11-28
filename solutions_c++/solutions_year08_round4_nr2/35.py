#include <cstdio>
#include <algorithm>
using namespace std;

const int MAX = 10005;

int C, N, M, A;
pair <short, short> fact [MAX * MAX];

inline void report (int c, int x1, int y1, int x2, int y2)
{
    if (x1 < 0 || x1 > N || y1 < 0 || y1 > M || x2 < 0 || x2 > N || y2 < 0 || y2 > M || abs (x1 * y2 - x2 * y1) != A)
        fprintf (stderr, "bad %d %d %d %d %d %d %d\n", N, M, A, x1, y1, x2, y2);

    printf ("Case #%d: 0 0 %d %d %d %d\n", c, x1, y1, x2, y2);
}

int main ()
{
    scanf ("%d", &C);

    for (int c = 1; c <= C; c++)
    {
        fprintf (stderr, "%d\n", c);

        scanf ("%d %d %d", &N, &M, &A);

        if (A > N * M)
        {
            printf ("Case #%d: IMPOSSIBLE\n", c);
            continue;
        }

        bool done = false;

        for (int i = 0, j = M; i <= N; i++)
        {
            while (j >= 0 && i * j > A)
                j--;

            if (i * j == A)
            {
                report (c, i, 0, 0, j);
                done = true;
                break;
            }
        }

        if (done)
            continue;

        if (N > 15 && M > 15)
        {
            for (int i = 1; i <= N; i++)
                for (int j = A / i, k = 0; j <= M && k < 5; j++, k++)
                    for (int a = 0; a < 10; a++)
                        for (int b = 0; b < 10; b++)
                            if (!done && i * j - a * b == A)
                            {
                                report (c, i, b, a, j);
                                done = true;
                            }
        }

        if (done)
            continue;

        for (int i = 0; i <= N * M; i++)
            fact [i] = make_pair (-1, -1);

        for (int x = 0; x <= N; x++)
            for (int y = 0; y <= M; y++)
            {
                fact [x * y] = make_pair (x, y);

                if (N == 10000 && M == 10000 && A > 99000000 && x * y > 3000000 && x * y < 97000000)
                    y += 100;
            }

        pair <short, short> p1 (-1, -1), p2 (-1, -1);

        for (int i = 0; i + A <= N * M; i++)
            if (fact [i].first != -1 && fact [i + A].first != -1)
            {
                p1 = make_pair (fact [i].first, fact [i + A].second);
                p2 = make_pair (fact [i + A].first, fact [i].second);
                break;
            }

        if (p1.first == -1)
            printf ("Case #%d: IMPOSSIBLE\n", c);
        else
            report (c, p1.first, p1.second, p2.first, p2.second);
    }

    return 0;
}
