#include <cstdio>
#include <algorithm>

using namespace std;

int V[200], X[200];
double ART[200], RT[200];

int main()
{
	int C;
	scanf("%d",&C);

	int tcc = 1;
	while(C--)
	{
		int N, K, B, T;
		scanf("%d%d%d%d",&N,&K,&B,&T);
		
		for( int i=0; i<N; ++i )
			scanf("%d",&X[i]);

		for( int i=0; i<N; ++i )		
			scanf("%d",&V[i]);
		
		int pt = 0;
		int sc = 0;
		int done = 0;
		for( int i=N-1; i>=0; --i )
		{
			if( X[i] + V[i]*T >= B )
			{
				sc += pt;
				if( ++done >= K )
					break;
			}
			else
			{
				++pt;
			}			
		}

		if( done >= K )
			printf("Case #%d: %d\n", tcc, sc );
		else
			printf("Case #%d: IMPOSSIBLE\n", tcc );

		
		/*for(;;)
		{
			int ok = 0;
			for( int i=N-1; i>=0; --i )
			{
				if( ART[i] <= T + 0.000001 )
				{
					++ok;
				}
			}		
			
			if( ok >= K )
				break;

			{
				int i;
				for( i=N-1; i>=1; --i )
				{
					if( RT[i] > RT[i-1] )
					{
						double TA, TB;
						TA = ART[i];
						TB = RT[i];

						RT[i] = RT[i-1];
						ART[i] = ART[i-1];

						RT[i-1] = TA;
						ART[i-1] = TB;

						if( i == N - 1 )
							ART[i] = RT[i];
						else
							ART[i] = std::max<double>( RT[i], ART[i+1] );

						++sc;
						break;
					}
				}

				if( i == 0 )
				{
					sc = -1;
					break;
				}
			}			
		}	*/

		++tcc;
	}
	return 0;
}