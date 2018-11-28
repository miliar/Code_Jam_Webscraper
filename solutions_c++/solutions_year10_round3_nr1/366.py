#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
	FILE *fp1, *fp2;

	fp1 = fopen("A-large (1).in", "r");
	if ( fp1 == NULL )
		return 0;

	fp2 = fopen("out.txt", "w");
	if ( fp2 == NULL )
		return 0;

	int T, N, A[10005], B[10005], trial, i, j, cnt;

	fscanf(fp1, "%d", &T);

	for ( trial = 1; trial <= T; trial++ )
	{
		cnt = 0;
		fscanf(fp1, "%d", &N);
		for ( i = 1; i <= N; i++ )
		{
			fscanf(fp1, "%d %d", &A[i], &B[i]);
		}

		for ( i = 1; i <= N; i++ )
		{
			for ( j = 1; j < i; j++ )
			{
				if ( A[i] > A[j] && B[i] < B[j] )
				{
					cnt++;
				}
				else if ( A[i] < A[j] && B[i] > B[j] )
				{
					cnt++;
				}
			}
		}
		fprintf(fp2, "Case #%d: %d\n", trial, cnt);
	}


	
	fclose(fp1);
	fclose(fp2);
	
	return 0;
}