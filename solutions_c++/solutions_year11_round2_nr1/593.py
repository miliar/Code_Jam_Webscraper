#include <cstdio>
#include <cstdlib>


double rpi[200];
double wp[200];
int cwp[200];
double owp[200];
double oowp[200];
int G[200][200];
char buff[200];

int main()
{
	FILE * fin = fopen( "in.txt" , "r" );
	FILE * fout = fopen( "out.txt" , "w" );
	
	int T;
	fscanf( fin , "%d" , &T );
	
	for( int t = 1 ; t <= T ; t++ )
	{
		int N;
		fscanf( fin , "%d" , &N );
		for( int i = 0 ; i < N ; i++ )
		{
			fscanf( fin , "%s" , buff );
			for( int j = 0 ; j < N ; j++ )
			{
				if( buff[j] == '1' )
				{
					G[i][j] = 1;
				}else if( buff[j] == '0' )
				{
					G[i][j] = 0;
				}else
				{
					G[i][j] = -1;
				}
			}
		}
		for( int i = 0 ; i < N ; i++ )
		{
			wp[i] = 0;
			int cc = 0;
			for( int j = 0 ; j < N ; j++ )
			{
				if( G[i][j] != -1 )
				{
					cc++;
					wp[i] += G[i][j];
				}
			}
			if( cc ) wp[i] /= cc;
			cwp[i] = cc;
		}	
		for( int i = 0 ; i < N ; i++ )
		{
			owp[i] = 0;
			int cc = 0;
			for( int j = 0 ; j < N ; j++ )
			{
				if( G[i][j] != -1 && j != i)
				{
					cc++;
					owp[i] += (wp[j]*cwp[j]-G[j][i])/(cwp[j]-1);
				}
			}
			if( cc ) owp[i] /= cc;
		}
		for( int i = 0 ; i < N ; i++ )
		{
			oowp[i] = 0;
			int cc = 0;
			for( int j = 0 ; j < N ; j++ )
			{
				if( G[i][j] != -1 && j != i)
				{
					cc++;
					oowp[i] += owp[j];
				}
			}
			if( cc ) oowp[i] /= cc;
		}
		fprintf( fout , "Case #%d:\n" , t );
		for( int i = 0 ; i < N ; i++ )
		{
			rpi[i] = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
			fprintf( fout , "%lf\n" , rpi[i] );	
		}
	}
	
	
	system("PAUSE");
	return 0;
}
