#include <cstdio>
#include <algorithm>

using namespace std;

int D[200][200];

int D2[200][200];

void extracth( int K, int S, bool left )
{
	for( int i=1; i<=S; ++i )
	{
		for( int j=1; j<=i; ++j )
		{
			int y = i + K - S;
			int x = j + (left ? 0 : K-S);
			
			D2[i][j] = D[y][x];			
		}
	}

	for( int i=S+1; i<=2*S-1; ++i )
	{
		for( int j=1; j<=(2*S-i); ++j )
		{
			int y = i + K - S;
			int x = j + (left ? 0 : K-S);
			
			D2[i][j] = D[y][x];
		}
	}
}

void extracttop( int K, int S )
{
	for( int i=1; i<=S; ++i )
	{
		for( int j=1; j<=i; ++j )
		{
			int y = i;
			int x = j;
			
			D2[i][j] = D[y][x];			
		}
	}

	for( int i=S+1; i<=2*S-1; ++i )
	{
		for( int j=1; j<=(2*S-i); ++j )
		{
			int y = i;
			int x = j + std::min<int>( K-S, i-S );
			
			D2[i][j] = D[y][x];
		}
	}
}

void extractbottom( int K, int S )
{
	for( int i=1; i<=S; ++i )
	{
		for( int j=1; j<=i; ++j )
		{
			int y = i + 2*(K-S);
			int x = j + std::min<int>( K-S, S-i );
			
			D2[i][j] = D[y][x];			
		}
	}

	for( int i=S+1; i<=2*S-1; ++i )
	{
		for( int j=1; j<=(2*S-i); ++j )
		{
			int y = i + 2*(K-S);
			int x = j;
			
			D2[i][j] = D[y][x];
		}
	}
}

bool okay( int S, bool horiz, bool vert )
{
	bool ok = true;
	for( int i=1; i<=S; ++i )
	{
		for( int j=1; j<=i; ++j )
		{
			int y = i;
			int x = j;

			int yv = i;
			int xv = (i-j+1);

			if( horiz )
			{
				if( D2[y][x] != D2[yv][xv] ) ok = false;
			}

			int yw = (2*S-i);
			int xw = j;

			if( vert )
			{
				if( D2[y][x] != D2[yw][xw] ) ok = false;
			}
		}
	}

	for( int i=S+1; i<=2*S-1; ++i )
	{
		for( int j=1; j<=(2*S-i); ++j )
		{
			int y = i;
			int x = j;

			int yv = i;
			int xv = ((2*S-i)-j+1);

			if( horiz )
			{
				if( D2[y][x] != D2[yv][xv] ) ok = false;
			}

			int yw = (2*S-i);
			int xw = j;

			if( vert )
			{
				if( D2[y][x] != D2[yw][xw] ) ok = false;
			}
		}
	}

	return ok;
}

int sz( int S )
{
	int n = 0;

	for( int i=1; i<=S; ++i )
		{
			n += i;
		}

		for( int i=S+1; i<=(2*S-1); ++i )
		{
			 n += 2*S-i;
		}

	return n;
}

int main()
{
	int C;
	scanf("%d",&C);

	int tcc = 1;
	while(C--)
	{
		int K;
		scanf("%d",&K);

		for( int i=1; i<=K; ++i )
		{
			for( int j=1; j<=i; ++j )
			{
				int x;
				scanf("%d",&x);
				D[i][j] = x;
			}
		}

		for( int i=K+1; i<=(2*K-1); ++i )
		{
			for( int j=1; j<=2*K-i; ++j )
			{
				int x;
				scanf("%d",&x);
				D[i][j] = x;
			}
		}

		{
			int i;
			for( i=0; i<K; ++i )
			{
				int S = K - i;

				extracth( K, S, true );
				if( okay( S, true, false ) )
					break;				

				extracth( K, S, false );
				if( okay( S, true, false ) )
					break;				
			}

			int hmin = i;

			for( i=0; i<K; ++i )
			{
				int S = K - i;

				extracttop( K, S);
				if( okay( S, false, true ) )
					break;				

				extractbottom( K, S );
				if( okay( S, false, true ) )
					break;					
			}

			int vmin = i;

			int sc = -(sz(K) - sz(K + hmin + vmin));
			
			printf("Case #%d: %d\n", tcc, sc );
		}

		++tcc;
	}
	return 0;
}