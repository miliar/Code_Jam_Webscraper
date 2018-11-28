#include <stdio.h>
#include <algorithm>

using namespace std;

FILE *inf, *outf;
int t, n, v1[810], v2[810];
long long answer;

int main()
{
    int l1, l2, l3;
    inf = fopen("a.in", "r");
    outf = fopen("a.out", "w");
    fscanf(inf, "%d", &t);
    for (l1 = 1; l1 <= t; l1++)
    {
	fscanf(inf, "%d", &n);
	for (l2 = 1; l2 <= n; l2++)
	    fscanf(inf, "%d", &v1[l2]);
	for (l2 = 1; l2 <= n; l2++)
	    fscanf(inf, "%d", &v2[l2]);
	sort(v1 + 1, v1 + n + 1);
	sort(v2 + 1, v2 + n + 1);
	answer = 0;
	for (l2 = 1; l2 <= n; l2++)
	    answer += (long long)v1[l2] * (long long)v2[n - l2 + 1];
	fprintf(outf, "Case #%d: %lld\n", l1, answer);
    }
    fclose(inf);
    fclose(outf);
    return 0;
}

