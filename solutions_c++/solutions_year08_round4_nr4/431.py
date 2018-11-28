#include <stdio.h>
#include <algorithm>

using namespace std;

FILE *inf, *outf;
int n, k;
char S[50010], s[50010];

int sub()
{
    int p[20], f = 1, cnt, min = 2147483647;
    int l1, l2, l3;
    for (l1 = 1; l1 <= k; l1++)
    {
	p[l1 - 1] = l1;
	f *= l1;
    }
    for (l1 = 1; l1 <= f; l1++)
    {
	for (l2 = 0; S[l2 + 1] != char(NULL); l2 += k)
	{
	    for (l3 = 0; l3 < k; l3++)
	    {
		s[l2 + l3 + 1] = S[l2 + p[l3]];
	    }
	}
	s[l2 + 1] = char(NULL);
	cnt = 0;
	for (l2 = 1; s[l2] != char(NULL); l2++)
	    if (s[l2 - 1] != s[l2])
		cnt++;
	if (min > cnt)
	    min = cnt;
	next_permutation(p, p + k);
    }
    return min;
}

int main()
{
    int l1;
    inf = fopen("d.in", "r");
    outf = fopen("d.out", "w");
    fscanf(inf, "%d", &n);
    for (l1 = 1; l1 <= n; l1++)
    {
	fscanf(inf, "%d%s", &k, S + 1);
	fprintf(outf, "Case #%d: %d\n", l1, sub());
    }
    fclose(inf);
    fclose(outf);
    return 0;
}
