#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<fstream>
#define MAXSIZE 500
using namespace std;

int N, Board[MAXSIZE][MAXSIZE] = {0}, INTWP[MAXSIZE], Count[MAXSIZE];
float OWP[MAXSIZE], OOWP[MAXSIZE], WP[MAXSIZE], ANS[MAXSIZE];

void ini()
{
	memset( INTWP, 0, sizeof(INTWP));	
	memset( Count, 0, sizeof(Count));	
	memset( WP, 0, sizeof(WP));
	memset( OWP, 0, sizeof(OWP));
	memset( OOWP, 0, sizeof(OOWP));
	memset( ANS, 0, sizeof(ANS));	
}

int main()
{
	int datacase, t = 0;
	char tem[MAXSIZE] = {0};
	freopen("A-large.in", "r", stdin );
	freopen("A-large.out", "w", stdout );
	scanf("%d", &datacase );
	while( datacase-- )
	{
		ini();
		scanf("%d\n", &N );
		for( int i = 0; i < N; i++ )
		{
			gets(tem);
			for( int j = 0; tem[j]; j++ )
			{
				if( tem[j] == '.' )
				{
					Board[i][j] = -1;
				}
				else if( tem[j] == '0' )
				{
					Count[i]++;
					Board[i][j] = 0;
				}
				else if( tem[j] == '1' )
				{
					Count[i]++;
					Board[i][j] = 1;
					INTWP[i]++;
				}
			}
		}
		for( int i = 0; i < N; i++ )
		{
			if( Count[i] > 0  )
				WP[i] = (double)INTWP[i]/(double)Count[i];
		}
		for( int i = 0; i < N; i++ )
		{
			double SumOWP = 0;
			for( int j = 0; j < N; j++ )
			{
				if( i == j )
					continue;
				if( Board[j][i] == -1 )
					continue;
				if( Board[j][i] == 0 )
				{
					if( Count[j]-1 > 0 )
						SumOWP += (double)INTWP[j]/(double)(Count[j]-1);
				}
				if( Board[j][i] == 1 )
				{
					if( Count[j]-1 > 0 )
						SumOWP += (double)(INTWP[j]-1)/(double)(Count[j]-1);						
				}
			}
		//	printf("%d %lf\n", i, SumOWP );
			if( Count[i] > 0 )
				OWP[i] = SumOWP / (double)Count[i];
		}
		for( int i = 0; i < N; i++ )
		{
			for( int j = 0; j < N; j++ )
			{
				if( i == j )
					continue;
				if( Board[j][i] == -1 )
				{
					continue;
				}
				OOWP[i] += OWP[j];
			}
			if( Count[i] > 0 )
				OOWP[i] = OOWP[i] / (double)(Count[i]);
			ANS[i] = 0.25 * WP[i] + 0.50 * OWP[i] +  0.25 * OOWP[i];
		}
		
		printf("Case #%d:\n", ++t );
		for( int i = 0; i < N; i++ )
		{
			//printf("%lf %lf %lf ", WP[i], OWP[i], OOWP[i] );
			printf("%0.12lf\n", ANS[i] );
		} 
	}

	return 0;
}
