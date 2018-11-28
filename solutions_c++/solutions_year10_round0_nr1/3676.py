#include <cstdio>

int main ()
{
    int tests;
    scanf ("%d", &tests);
    for (int i = 1; i <= tests; ++i)
    {
        int n, k;
        scanf ("%d %d", &n, &k);
        printf ("Case #%d: %s\n", i, ((k + 1) % (1<<n) == 0) ? "ON" : "OFF");
    }
    return 0;
}