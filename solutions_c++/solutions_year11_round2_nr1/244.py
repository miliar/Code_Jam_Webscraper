#include<stdio.h>
#include<string.h>
#define maxn 128

int m[ maxn ][ maxn ];
int nr_played[ maxn ];
int nr_won[ maxn ];

void solve()
{
	double WP[ maxn ];
	double OWP[ maxn ];
	double OOWP[ maxn ];
	int N;
	scanf("%d", &N);
	memset( nr_played, 0, sizeof(nr_played));
	memset( nr_won, 0, sizeof(nr_won));
	for( int i = 0; i < N; ++i)
	{
		char sir[ maxn ];
		scanf("%s", sir);
		for( int j = 0; j < N; ++j)
		{
			if( sir[ j ] == '.')
			{
				m[ i ][ j ] = -1; continue;
			}
			
			m[ i ][ j ] = sir[ j ] - '0';
			nr_played[ i ]++;
			nr_won[ i ] += m[ i ][ j ];
		}
		WP[ i ] = nr_won[ i ] *  1.0 / nr_played[ i ];
		
	}
	for( int i = 0; i < N; ++i)
	{
		double sum_owp = 0;
		double nr_owp = 0;
		for( int j = 0; j < N; ++j)
		{
			if( m[ i ][ j ] >= 0 )
			{
				nr_owp++;
				if( m[ i ][ j ] == 0)
				{
					sum_owp += double(nr_won[ j ] - 1.0)/  (nr_played[ j ] -1.0);
				}
				else sum_owp += (double)nr_won[ j ] /  (nr_played[ j ] -1.0);
			}
		}
		OWP[ i ] = sum_owp /nr_owp;
	}
	for( int i = 0; i < N; ++i)
	{
		double sum_oowp = 0;
		double nr_oowp = 0;
		for( int j = 0; j < N; ++j)
		{
			if( m[ i ][ j ] == -1) continue;
			sum_oowp += OWP[ j ];
			nr_oowp++;
		}
		OOWP[ i ] = sum_oowp / nr_oowp;
	}
	for( int i = 0; i < N; ++i)
	{
		printf("%.10lf\n", WP[ i ] * 0.25 + OWP[ i ] * 0.5 + OOWP[ i ] *0.25);
	}

	return;
}


int main()
{
	//freopen("RPI.in","r",stdin);
	//freopen("RPI.out","w",stdout);
	
	int TT;
	scanf("%d", &TT);
	for( int ii = 1; ii <= TT; ++ii)
	{
		printf("Case #%d:\n", ii);
		solve();
	}
	
	
	
	
	
	return 0;
}
