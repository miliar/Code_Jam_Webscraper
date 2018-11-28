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

#define fr(i,a,b) for ( i = ( a ); i <= ( b ); ++i)
#define fi(a) for ( i = 0; i < ( a ); ++i)
#define fj(a) for ( j = 0; j < ( a ); ++j)
#define fk(a) for ( k = 0; k < ( a ); ++k)
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

string w[5005];
int L, D, N;

bool g[20][30];

void parse( string s )
{
	clr( g );
	int i;
	int pos = 0;
	fi( s.length() )
	{
		if ( s[i] == '(' ) 
		{
			int j = i + 1;
			while ( s[j] >= 'a' && s[j] <= 'z' )
			{
				g[pos][ s[j] - 'a' ] = true;
				++j;
			}
			i = j;
		}
		else
			g[pos][s[i]-'a'] = true;
		++pos;
	}
}

bool good( string s )
{
	int i;
	fi( s.length() )
	{
		if ( !g[i][s[i]-'a'] ) return ( false );
	}
	return ( true );
}

void solve()
{
	int i, j;
	cin >> L >> D >> N;
	fi( D )
		cin >> w[i];
	string s;
	fi( N )
	{
		cout << "Case #" << i + 1 << ": ";
		cin >> s;
		parse( s );
		int am = 0;
		fj( D )
			if ( good( w[j] ) )
				++am;
		cout << am << endl;
	}
}

int main()
{
	initf();
	solve();
	return (0);
}