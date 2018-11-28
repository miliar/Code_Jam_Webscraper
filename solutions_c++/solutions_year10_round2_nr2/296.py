#include <cstdio>

int b, t, k, n;
int speeds[100];
int positions[100];

void gogo (int test)
{
    scanf ("%d %d %d %d", &n, &k, &b, &t);
    for (int i = 0; i < n; ++i) scanf ("%d", &positions[i]);
    for (int i = 0; i < n; ++i) scanf ("%d", &speeds[i]);

    printf ("Case #%d: ", test);

    int answer = 0;
    int howmany = 0;
    int count = 0;

    for (int i = 0; i < n; ++i)
        if ((b - positions[i]) <= t * speeds[i]) ++count;

    if (count < k) 
    {
        printf ("IMPOSSIBLE\n");
        return;
    }

    count = 0;
    for (int i = n - 1; i >= 0; --i)
    {
        if ((b - positions[i]) <= t * speeds[i]) howmany++, answer += count;
        else ++count;
        if (howmany >= k) break;
    }

    printf ("%d\n", answer);
}

int main ()
{
    int tests;
    scanf ("%d", &tests);

    for (int i = 1; i <= tests; ++i) gogo (i);
    return 0;
}