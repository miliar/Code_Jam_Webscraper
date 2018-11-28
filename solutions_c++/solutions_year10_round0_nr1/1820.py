#include <stdio.h>
#include <string.h>

int n, k;

int main()
{
    int i, j, csnum, cs;
    freopen("A-large.in", "r", stdin);
    freopen("1.out", "w", stdout);
    scanf ("%d", &csnum);

    for (cs = 1; cs <= csnum; cs++)
    {
        scanf ("%d %d", &n, &k);

        k = k % (1<<n);
        printf ("Case #%d: ", cs);
        if (k == (1<<n) - 1)
            printf ("ON\n");
        else
            printf ("OFF\n");
    }
}
