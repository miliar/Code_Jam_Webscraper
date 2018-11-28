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

void solve()
{
	int t;
	cin >> t;
	fk( t )
	{
		printf("Case #%d: ", k + 1 );
		ll x;
		string s;
		cin >> s;
		reverse( all ( s ) );
		vi v;
		fi( s.length() )
		{
			v.pb( s[i] - '0' );
		}
		bool ok = true;
		fi( v.size() ) if ( i )
			if ( v[i] < v[i-1] )
			{
				ok = false;
				break;
			}
		ll y = 0;
		if ( ok )
		{
			int am = 0;
			v.pb( 0 );
			fi( v.size() ) if ( v[i] == 0 ) ++am;
			vi vv;
			fi( v.size() ) if ( v[i] ) vv.pb( v[i] );
			sort( all ( vv )) ;
			v.clear();
			v.pb( vv[0] );
			fi( am ) v.pb( 0 );
			fi( vv.size() ) if ( i ) v.pb( vv[i] );
			fi( v.size() )
			{
				cout << v[i];
			}
		}
		else
		{
			reverse( all ( v ) );
			next_permutation( all ( v ) );
			fi( v.size() )
			{
				cout << v[i];
			}
		}
		cout << endl;

	}
}

int main()
{
    initf();
    solve();
    return ( 0 );
}
