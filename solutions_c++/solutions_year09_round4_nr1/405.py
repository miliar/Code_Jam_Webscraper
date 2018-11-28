//AlexFetisov
//Accepted
//I'm Feeling Lucky!

#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:128000000")

#include <iostream>

void initf()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
}

#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
#include <string>
#include <sstream>

using namespace std;

#define fr(i,a,b) for ( int i = ( a ); i <= ( b ); ++i)
#define fi(a) for ( int i = 0; i < ( a ); ++i)
#define fj(a) for ( int j = 0; j < ( a ); ++j)
#define fk(a) for ( int k = 0; k < ( a ); ++k)
#define CLR(a, b) memset( ( a ), ( b ), sizeof( ( a ) ) )
#define clr(a) CLR( ( a ), 0 )
#define pb push_back
#define mp make_pair
#define all( v ) ( v ).begin(),( v ).end()

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef vector < int > vi;
typedef pair < int, int > pii;

const int inf = 1 << 30;

int a[50][50];
int n; 

void swa( int i, int j )
{
	fk( n ) swap( a[i][k], a[j][k] );
}

void solve()
{
	int test;
	scanf("%d", &test);
	fr(tst,1,test)
	{
		printf("Case #%d: ", tst );
		/////////////////////////////////////

		cin >> n;
		fi( n ) 
		{
			fj( n ) 
			{
				char c;
				cin >> c;
				a[i][j] = c - '0';
			}
		}

		int last = 0;
		int ret = 0;

		fi( n )
		{
			++last;
			int id = -1;
			fj( n ) if ( j >= i )
			{
				bool ok = true;
				fr(k,last,n-1)
					if ( a[j][k] != 0 )
					{
						ok = false;
						break;
					}	
				if ( ok )
				{
					id = j;
					break;
				}
			}
			if ( id != i ) 	
				for ( int j = id; j > i; --j )
				{
					++ret;
					swa( j, j-1 );
				}
		}
		cout << ret << endl;
	}
}

int main()
{
	initf();
	solve();
	return (0);
}