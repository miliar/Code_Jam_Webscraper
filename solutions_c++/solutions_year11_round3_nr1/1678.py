#include <stdio.h>
#include <math.h>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <functional>

#define fi(t,a,b,c) for(t a = ( b ); a < ( c ); ++ a )
#define fd(t,a,b,c) for(t a = ( b ); a >= ( c ); -- a )
#define fii(a,b,c) fi( int, a, ( b ), ( c ) )
#define fdi(a,b,c) fd( int, a, ( b ), ( c ) )
#define fiii(a) fii( i, 0, ( a ) )
#define fiij(a) fii( j, 0, ( a ) )
#define fiik(a) fii( k, 0, ( a ) )
#define fdii(a) fdi( i, 0, ( a ) )
#define fdij(a) fdi( j, 0, ( a ) )
#define fdik(a) fdi( k, 0, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )

using namespace std;

int ni() { int a; scanf( "%d", &a ); return a; }
float nf() { float a; scanf( "%f", &a ); return a; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }

template <class T> void out( T a, T b ) { bool first = true; for( T i = a; i != b; ++ i ) { if( !first ) printf( " " ); first = false; cout << * i; } printf( "\n" ); }
template <class T> void outl( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;

char tiles[100][100];
int r, c;

bool tryred(int i, int j)
{
	if(i == r-1 || j == c-1)
	{
		return false;
	}
	tiles[i][j] = '/';
	if(tiles[i][j+1] != '#') return false;
	tiles[i][j+1] = '\\';
	if(tiles[i+1][j] != '#') return false;
	tiles[i+1][j] = '\\';
	if(tiles[i+1][j+1] != '#') return false;
	tiles[i+1][j+1] = '/';
	return true;
}

void solve()
{
	scanf("%d %d", &r, &c);
	fiii(r)
	{
		scanf("%s", tiles[i]);
	}
	fiii(r)
	{
		fiij(c)
		{
			if(tiles[i][j] == '#')
			{
				if(!tryred(i,j))
				{
					printf("Impossible");
					return;
				}
			}
		}
	}

	fiii(r)
	{
		fiij(c)
		{
			printf("%c", tiles[i][j]);
		}
		if(i != r-1)
			printf("\n");
	}
}

int main(int argc, char** argv)
{
   freopen( "input.txt", "r", stdin );
   freopen( "output.txt", "w", stdout );

   int tt = ni();
   fiii(tt)
   {
      printf("Case #%d:\n", i + 1);
	  solve();
	  printf("\n");
   }
   return 0;
}