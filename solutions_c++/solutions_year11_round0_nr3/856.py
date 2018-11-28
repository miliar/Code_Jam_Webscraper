#include <stdio.h>
#include <string.h>

int tc, ntc;
int n;
int ar[1000];

int doit()
{
	int i;
	int x = 0;
	for (i=0; i<n; i++) x ^= ar[i];
	if (x != 0) return -1;
	
	int sum = 0;
	int minv = 10000000;
	for (i=0; i<n; i++)
	{
		sum += ar[i];
		if (ar[i] < minv) minv = ar[i];
	}
	
	return sum - minv;
}

int main()
{
	FILE* fi = fopen("C-large.in", "r");
	FILE* fo = fopen("C-large.out", "w");
	
	fscanf(fi, "%d", &ntc);
	int i;
	
	for (tc=1; tc<=ntc; tc++)
	{
		fscanf(fi, "%d", &n);
		for (i=0; i<n; i++)
			fscanf(fi, "%d", &ar[i]);
		
		int res = doit();
		printf("Case #%d: ", tc);
		if (res == -1) printf("NO\n");
		else printf("%d\n", res);
		
		fprintf(fo, "Case #%d: ", tc);
		if (res == -1) fprintf(fo, "NO\n");
		else fprintf(fo, "%d\n", res);

	}
	
	fclose(fi); fclose(fo);
}