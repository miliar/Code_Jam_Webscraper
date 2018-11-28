#include <stdio.h>
#include <stdlib.h>
#include <math.h>

__int64 triall(__int64 a)
{
	if ( a <=2 )
		return a;
	else
		return triall(a/2) + 1;
}

int main()
{
	FILE *fp1, *fp2;

	fp1 = fopen("B-large (1).in", "r");
	if ( fp1 == NULL )
		return 0;

	fp2 = fopen("out.txt", "w");
	if ( fp2 == NULL )
		return 0;

	__int64 T, L, P, C, i, trial, cnt;

	fscanf(fp1, "%lld", &T);

	for ( trial = 1; trial <= T; trial++ )
	{
		cnt = 0;
		fscanf(fp1, "%lld %lld %lld", &L, &P, &C);
		for ( i = C*L; i < P;)
		{
			i = i*C;
			cnt++;
		}
		fprintf(fp2, "Case #%lld: %lld\n", trial, triall(cnt));
	}


	
	fclose(fp1);
	fclose(fp2);
	
	return 0;
}