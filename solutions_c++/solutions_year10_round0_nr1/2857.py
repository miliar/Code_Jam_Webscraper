#include <stdio.h>

int sum[32];
int sqe[32];

int main ()
{

	int t;
	int n, k;

	FILE *fout = fopen("A.out","w");

	sum[0] = 1;
	sqe[0] = 1;
	for(int i=1;i<31; i++)
	{
		sqe[i] = sqe[i-1] * 2;
		sum[i] = sum[i-1] + sqe[i];
	}

	int ce = 0;

	scanf("%d", &t);
	while (t--)
	{
		scanf("%d %d", &n, &k);	
		
		ce++;
		k = k % sqe[n];
		if (k == sum[n-1])
			fprintf(fout, "Case #%d: ON\n", ce);
		else
			fprintf(fout, "Case #%d: OFF\n", ce);
	}
	fclose(fout);

	return 0;
}