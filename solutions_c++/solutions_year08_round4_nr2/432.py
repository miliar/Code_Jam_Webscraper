#include <stdio.h>

FILE *inf, *outf;
int c, n, m, a;
int x1, y1, x2, y2;

/*
bool sub()
{
    printf("%d %d %d\n", n, m, a);
    printf("%d\n",x1);
    for (x1 = 0; x1 <= n; x1++)
    {
	printf("//");
	for (y1 = 0; y1 <= x1 && y1 <= m; y1++)
	{
	    printf ("a");
	    for (x2 = int(a / y1); x2 <= n; x2++)
	    {
		y2 = int((x2 * y1 + a) / x1);
		if (x1 * y2 - x2 * y1 == a)
		    return true;
		y2 = int((x2 * y1 - a) / x1);
		if (x1 * y2 - x2 * y1 == a)
		    return true;
	    }
	    printf("b");
	    for (y2 = int(a / x1); y2 <= m; y2++)
	    {
		x2 = int((x1 * y2 + a) / y1);
		if (x1 * y2 - x2 * y1 == a)
		    return true;
		x2 = int((x1 * y2 + a) / y1);
		if (x1 * y2 - x2 * y1 == a)
		    return true;
	    }
	}
    }
    return false;
}
*/

bool sub()
{
    for (x1 = 0; x1 <= n; x1++)
    {
	for (y1 = 0; y1 <= m; y1++)
	{
	    for (x2 = 0; x2 <= n; x2++)
	    {
		for (y2 = 0; y2 <= m; y2++)
		{
		    if (x1 * y2 - x2 * y1 == a)
			return true;
		}
	    }
	}
    }
    return false;
}

int main()
{
    int l1;
    inf = fopen("b.in", "r");
    outf = fopen("b.out", "w");
    fscanf(inf, "%d", &c);
    for (l1 = 1; l1 <= c; l1++)
    {
	fscanf(inf, "%d%d%d", &n, &m, &a);
	if (sub())
	    fprintf(outf, "Case #%d: 0 0 %d %d %d %d\n", l1, x1, y1, x2, y2);
	else
	    fprintf(outf, "Case #%d: IMPOSSIBLE\n", l1);
    }
    fclose(inf);
    fclose(outf);
    return 0;
}
