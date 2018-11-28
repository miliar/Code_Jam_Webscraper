#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define rep(i,n) for( int i = 0, _n = (n); i < _n; i++ )
#define forn(i,a,b) for( int i = (a), _n = (b); i <= _n; i++ )
#define ford(i,a,b) for( int i = (a), _n = (b); i >= _n; i-- )
#define foreach(it,c) for( typeof((c).begin()) it = (c).begin(); it != (c).end(); it++ )

#define debug(x) cout << ">>" << #x << " = " << x << endl;

#define two(x) (1<<(x))
#define contain(S,x) (((S)&two(x)) > 0)
#define twoll(x) (1LL<<(x))
#define containll(S,x) (((S)&twoll(x))>0)

#define pb push_back
#define mp make_pair

void open()
{
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );
}

const int dr[] = { +1, +1, +1,  0 };
const int dc[] = { +1, -1,  0, +1 };

int n,K;
char a[51][51];
char b[51][51];

void rotate()
{
	rep( i, n ) rep( j, n )
		b[i][j] = a[n-j-1][i];
		
	rep( i, n ) rep( j, n )
		a[i][j] = b[i][j];
}

void gravity()
{
	ford( i, n-1, 0 ) ford( j, n-1, 0 )
		if( a[i][j] != '.' )
		{
			int x = i;
			while( x+1 < n && a[x+1][j]=='.' )
				swap( a[x][j], a[x+1][j] ), x++;	
		}	
}

int is_valid( int r, int c )
{
	return ( r >= 0 && r < n && c >= 0 && c < n );	
}

int main()
{
	open();
	
	int ntc; scanf("%d",&ntc);
	rep(T,ntc)
	{
		scanf( "%d%d", &n,&K );
		rep( i, n ) scanf( "%s", a[i] );
		rotate();
		gravity();
		
		/*
		rep( i, n ) 
		{
			rep( j, n ) printf( "%c", a[i][j] );
			printf( "\n" );
		}
		*/
		int blue = 0, red = 0;
		rep( i, n ) rep( j, n ) if( a[i][j] != '.' )
		{
			rep( k, 4 )
			{
				int jml = 0;
				int r = i, c = j;
				while( is_valid(r,c) && a[i][j] == a[r][c] )
				{
					jml++;
					r += dr[k];
					c += dc[k];
				}
				if( jml >= K )
				{
					if( a[i][j] == 'B' ) blue = 1;
					if( a[i][j] == 'R' ) red = 1;	
				}
			}
		}
		
		printf( "Case #%d: ", T+1 );
		if( blue && red ) printf( "Both\n" );
		else if( blue ) printf( "Blue\n" );
		else if( red ) printf( "Red\n" );
		else printf( "Neither\n" );
	}
	return 0;
}
