#include <stdio.h>
#include <stdlib.h>

int main()
{
	unsigned int K, N, T;
	FILE *fp1, *fp2;

	fp1 = fopen("A-large.in", "r");
	if ( fp1 == NULL )
		return 0;
	
	fp2 = fopen("output.txt", "w");
	if ( fp2 == NULL )
		return 0;	

	fscanf(fp1, "%d", &T);

	for ( unsigned int i = 1; i <= T; i++)
	{
		fscanf(fp1, "%d %d", &N, &K);

		fprintf(fp2, "Case #%d: %s\n", i, ((K+1)%(1<<N)) == 0 ? "ON":"OFF");
		
	}

	fclose(fp1);
	fclose(fp2);
	
	return 0;
}