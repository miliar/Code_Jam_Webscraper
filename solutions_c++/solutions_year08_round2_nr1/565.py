#include <iostream.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

#define DEBUG

struct coord
{
	long long x, y;
};

int main( int argc, char *argv[] )
{
	FILE *fpIn, *fpOut;
	int numTestCases, caseNum = 1, i = 0, j = 0, k = 0;

	long int n, A, B, C, D, x0, y0, M;
	long int numCropTs = 0;
	coord trees[100000];

	if( ( fpIn = fopen( argv[1], "r" ) ) == 0 )
	{
		cout << "Problem opening input file" << endl;
		return 1;
	}

	if( ( fpOut = fopen( argv[2], "w" ) ) == 0 )
	{
		cout << "Problem opening output file" << endl;
		return 1;
	}

	fscanf( fpIn, "%d", &numTestCases );

	while( caseNum <= numTestCases )
	{
		fscanf( fpIn, "%ld%ld%ld%ld%ld%ld%ld%ld", &n, &A, &B, &C, &D, &x0, &y0, &M );
		
		trees[0].x = x0;
		trees[0].y = y0;
		cout << x0 << " " << y0 << endl;
		for( i = 1; i < n; i++ )
		{
			trees[i].x = (A * trees[i-1].x + B) % M;
			trees[i].y = (C * trees[i-1].y + D) % M;
			cout << trees[i].x << " " << trees[i].y << endl;
		}

		numCropTs = 0;
		for( i = 0; i < n; i++ )
		{
			for( j = i + 1; j < n; j++ )
			{
				for( k = j + 1; k < n; k++ )
				{
					if( ( i == j ) || ( j == k ) || ( k == i ) )
						continue;
					else if( ( ( trees[i].x + trees[j].x + trees[k].x ) % 3 == 0 ) && ( ( trees[i].y + trees[j].y + trees[k].y ) % 3 == 0 ) )
						numCropTs++;
				}
			}
		}

		fprintf( fpOut, "Case #%d: %d\n", caseNum, numCropTs );

		caseNum++;
	}
}
