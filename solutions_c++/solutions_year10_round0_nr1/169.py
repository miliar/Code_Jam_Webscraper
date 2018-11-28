#include <stdio.h>
#include <string.h>

int tc, ntc;
int main()
{
	//FILE* fi = fopen("A.in", "r");
	//FILE* fo = fopen("A.out", "w");

	FILE* fi = fopen("A-large.in", "r");
	FILE* fo = fopen("A-large.out", "w");

	fscanf(fi, "%d", &ntc);
	int n, k;
	for (tc=1; tc<=ntc; tc++)
	{
		fscanf(fi, "%d %d", &n, &k);
		k %= (1<<n);

		fprintf(fo, "Case #%d: ", tc);
		if (k == (1<<n)-1) fprintf(fo, "ON\n");
		else fprintf(fo, "OFF\n");
	}

	return 0;
}