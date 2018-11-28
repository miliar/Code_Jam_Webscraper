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
const int MOD = 10000;

void out( int x )
{
	printf("%.4d\n", x );
	return;
	string s;
	while ( x )
	{
		s.pb( char( x % 10 + '0' ) );
		x /= 10;
	}
	reverse( all ( s )) ;
	while ( s.length() != 4 ) s.pb( '0' );
	cout << s << endl;
}

char s[505];
int n;

string shab = "welcome to code jam";

int dp[505][25];

void solve()
{
	char buf[50];
	gets( buf );
	int tst;
	sscanf(buf, "%d", &tst);
	fr(t,1,tst)
	{
		printf("Case #%d: ", t );
		gets( s );
		n = strlen( s );
		clr( dp );
		fi( n ) 
			if ( s[i] == 'w' ) 
				dp[i][0] = 1;
		fr(i,1,18)
		{
			char cl = shab[i];
			char pl = shab[i-1];
			fj( n )
				if ( s[j] == cl )
				{
					fk( j )
						if ( s[k] == pl )
						{
							( dp[j][i] += dp[k][i-1] ) %= MOD;
						}
				}
		}
		int sum = 0;
		fi( n )
			( sum += dp[i][18] ) %= MOD;
		out( sum );
	}
}

int main()
{
	initf();
	solve();
	return (0);
}