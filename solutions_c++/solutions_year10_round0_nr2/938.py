#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
	int C, num[4], N, rest, x, y, min;
	FILE *fp1, *fp2;

	fp1 = fopen("B-small-attempt10.in", "r");
	if ( fp1 == NULL )
		return 0;
	
	fp2 = fopen("output.txt", "w");
	if ( fp2 == NULL )
		return 0;

	fscanf(fp1, "%d", &C);

	for ( int i = 1; i <= C; i++ )
	{
		fscanf(fp1, "%d", &N);

		for ( int j = 1; j <= N; j++ )
			fscanf(fp1, "%d", &num[j]);

		if ( N == 3 )
		{
			x = abs(num[2] - num[1]);
			y = abs(num[3] - num[2]);
			if ( num[2] == num[1] && num[1] == num[3] )
			{
				min = x;
			}
			else if ( num[1] == num[2] )
			{
				x = abs(num[3] - num[2]);
				min = num[1]%x;
				if ( min == 0 )
				{
					min=x;
				}
			
			}
			else if ( num[2] == num[3] )
			{
				min = num[1]%x;
				if ( min == 0 )
				{
					min=x;
				}
		
			}
			else if ( num[3] == num[1] )
			{
				min = num[1]%x;
				if ( min == 0 )
				{
					min=x;
				}
		
			}

			else
			{
			if ( y > x )
			{
				rest = x;
				x = y;
				y = rest;
			}
				
			do
			{
				rest = x%y;
				x = y;
				y = rest;
			}while ( rest > 0 );

			if ( x == 1 )
				min = 1;
			else
				min = num[1]%x;
			if ( min == 0 )
				min = x;
			}

		}
		else
		{
			if ( num[1] == num[2] )
			{
				min = x;
			}

			else
			{
				x = abs(num[2] - num[1]);
				min = num[1]%x;
				if ( min == 0 )
				{
					min = x;
				}

			}
		}

		fprintf(fp2, "Case #%d: %d\n", i, x-min);
		//printf("%d\n", x);
	}

	fclose(fp1);
	fclose(fp2);
	
	return 0;
}