#include <stdio.h>
#define AND 1
#define OR 0
#define CHANGEABLE 1
#define INFINITE 100000

FILE *inf, *outf;
int n, m, v, g[10010], c[10010], l[10010];
int d[2][10010];

int main()
{
    int l1, l2, p, q;
    inf = fopen("a.in", "r");
    outf = fopen("a.out", "w");
    fscanf(inf, "%d", &n);
    for (l1 = 1; l1 <= n; l1++)
    {
	fscanf(inf, "%d%d", &m, &v);
	for (l2 = 1 ; l2 <= (m - 1) / 2; l2++)
	    fscanf(inf, "%d%d", &g[l2], &c[l2]);
	for (; l2 <= m; l2++)
	{
	    fscanf(inf, "%d", &l[l2]);
	    if (l[l2] == 0)
	    {
		d[0][l2] = 0;
		d[1][l2] = INFINITE;
	    }
	    else
	    {
		d[0][l2] = INFINITE;
		d[1][l2] = 0;
	    }
	}
	for (l2 = (m - 1) / 2; l2 >= 1; l2--)
	{
	    p = l2 * 2;
	    q = l2 * 2 + 1;
	    if (g[l2] == AND)
	    {
		d[0][l2] = d[0][p] + d[0][q];
		if (d[0][l2] > d[0][p] + d[1][q])
		    d[0][l2] = d[0][p] + d[1][q];
		if (d[0][l2] > d[1][p] + d[0][q])
		    d[0][l2] = d[1][p] + d[0][q];
		d[1][l2] = d[1][p] + d[1][q];
		if (c[l2] == CHANGEABLE)
		{
		    if (d[0][l2] > d[0][p] + d[0][q] + 1)
			d[0][l2] = d[0][p] + d[0][q] + 1;
		    if (d[1][l2] > d[0][p] + d[1][q] + 1)
			d[1][l2] = d[0][p] + d[1][q] + 1;
		    if (d[1][l2] > d[1][p] + d[0][q] + 1)
			d[1][l2] = d[1][p] + d[0][q] + 1;
		    if (d[1][l2] > d[1][p] + d[1][q] + 1)
			d[1][l2] = d[1][p] + d[1][q] + 1;
		}
	    }
	    else
	    {
		d[0][l2] = d[0][p] + d[0][q];
		d[1][l2] = d[0][p] + d[1][q];
		if (d[1][l2] > d[1][p] + d[0][q])
		    d[1][l2] = d[1][p] + d[0][q];
		if (d[1][l2] > d[1][p] + d[1][q])
		    d[1][l2] = d[1][p] + d[1][q];
		if (c[l2] == CHANGEABLE)
		{
		    if (d[0][l2] > d[0][p] + d[0][q] + 1)
			d[0][l2] = d[0][p] + d[0][q] + 1;
		    if (d[0][l2] > d[0][p] + d[1][q] + 1)
			d[0][l2] = d[0][p] + d[1][q] + 1;
		    if (d[0][l2] > d[1][p] + d[0][q] + 1)
			d[0][l2] = d[1][p] + d[0][q] + 1;
		    if (d[1][l2] > d[1][p] + d[1][q] + 1)
			d[1][l2] = d[1][p] + d[1][q] + 1;
		}
	    }
	}
	if (d[v][1] < INFINITE)
	    fprintf(outf, "Case #%d: %d\n", l1, d[v][1]);
	else
	    fprintf(outf, "Case #%d: IMPOSSIBLE\n", l1);
    }
    fclose(inf);
    fclose(outf);
    return 0;
}
