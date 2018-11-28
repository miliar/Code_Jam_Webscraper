#include <stdio.h>

FILE *inf, *outf;
int n, r, h, w, a, b;
int t[110][110];
long long d[110][110];

int main()
{
    int l1, l2, l3;
    inf = fopen("d.in", "r");
    outf = fopen("d.out", "w");
    fscanf(inf, "%d", &n);
    for (l1 = 1; l1 <= n; l1++)
    {
	fscanf(inf, "%d%d%d", &h, &w, &r);
	for (l2 = 1; l2 <= h; l2++)
	    for (l3 = 1; l3 <= w; l3++)
	    {
		t[l2][l3] = false;
		d[l2][l3] = 0;
	    }
	for (l2 = 1; l2 <= r; l2++)
	{
	    fscanf(inf, "%d%d", &a, &b);
	    t[a][b] = true;
	}
	d[1][1] = 1;
	for (l2 = 1; l2 <= h; l2++)
	    for (l3 = 1; l3 <= w; l3++)
	    {
		if(t[l2][l3])
		    continue;
		d[l2 + 1][l3 + 2] += d[l2][l3];
		d[l2 + 1][l3 + 2] %= 10007;
		d[l2 + 2][l3 + 1] += d[l2][l3];
		d[l2 + 2][l3 + 1] %= 10007;
	    }
	fprintf(outf, "Case #%d: %lld\n", l1, d[h][w]);
    }
    fclose(inf);
    fclose(outf);
    return 0;
}
