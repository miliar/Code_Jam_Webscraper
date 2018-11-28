// AlexFetisov
// Accepted
// I'm Feeling Lucky!

#define _CRT_SECURE_NO_DEPRECATE
#pragma comment (linker, "/STACK:128000000")

#include <iostream>

void initf()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
}

#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <queue>
//#include <cmath>

using namespace std;

#define fr(i,a,b) for (int i =  ( a ); i <= ( b ); ++i)
#define fi( a ) for (int i = 0; i < ( a ); ++i)
#define fj( a ) for (int j = 0; j < ( a ); ++j)
#define fk( a ) for ( int k = 0; k < ( a ); ++k )
#define CLR( a, b ) memset( ( a ), ( b ), sizeof( ( a ) ) )
#define clr( a ) CLR( ( a ), 0 )
#define mp make_pair
#define pb push_back
#define all( v ) ( v ).begin(), ( v ).end()

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef vector < int > vi;
typedef pair < int, int > pii;

const int inf = 1 << 30;

set < string > S;
string name;

double rec( string s )
{
	while ( s[0] == ' ' ) s.erase( s.begin() );
	s.erase( s.begin() );
	reverse( all( s ) );
	while ( s[0] == ' ' ) s.erase( s.begin() );
	s.erase( s.begin() );
	reverse( all( s ) );
	int st = 0;
	int pos1 = -1, pos2 = -1;
	fi( s.length() )
	{
		if ( s[i] == '(' && st == 0 )
		{
			if ( pos1 == -1 ) 
				pos1 = i;
			else
				if ( pos2 == -1 )
					pos2 = i;
			++st;
			continue;
		}
		if ( s[i] == '(' ) ++st;
		else
			if ( s[i] == ')' ) -- st;
	}
	if ( pos1 == -1 )
	{
		stringstream ss( s );
		double x;
		ss >> x;
		return ( x );
	}
	string s1 = s.substr( 0, pos1 );
	string s2 = s.substr( pos1, pos2 - pos1 );
	string s3 = s.substr( pos2 );
	stringstream ss( s1 );
	double x;
	string ch;
	ss >> x >> ch;
	double ret = 1.;
	if ( S.find( ch ) != S.end() )
	{
		ret = rec( s2 );
	}
	else
		ret = rec( s3 );
	ret *= x;
	return ( ret );
}

void solve()
{
	int t;
	cin >> t;
	fr(tst,1,t)
	{
		printf("Case #%d:\n", tst);
		////////////////////////////////
		int n;
		cin >> n;
		string s;
		string s1;
		getline( cin, s1, '\n' );
		fi( n )
		{
			getline( cin, s1, '\n' );
			s += s1;
		}
		cin >> n;
		fi( n )
		{
			int x;
			cin >> name >> x;
			S.clear();
			string ss;
			fj ( x ) 
			{
				cin >> ss;
				S.insert( ss );
			}
			double A = rec( s );
			printf("%.8lf\n", A );
		}
	}
}

int main()
{
    initf();
    solve();
    return ( 0 );
}
