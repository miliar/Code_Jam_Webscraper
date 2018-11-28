#pragma comment( linker, "/stack:128000000" )
#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>

void prepare( )
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
}

#include <cmath>
#include <cassert>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <sstream>
#include <iostream>
#include <deque>

using namespace std;

#define fo(a,b,c) for(a =(b);a<(c);++a)
#define fr(a,b) fo(a,0,(b))
#define fi(a) fr(i,(a))
#define fj(a) fr(j,(a))
#define fk(a) fr(k,(a))
#define all(a) (a).begin(),(a).end()
#define mp make_pair
#define pb push_back
#define sz(a) (int)(a).size()
#define _(a,b) memset((a),(b),sizeof(a))
#define __(a) _((a),0)

typedef long long lint;

int n, m;

struct Tree
{
	map<string, int> d;
};

vector<Tree> q;

int main( )
{
	prepare( );
	int i, j, k;
	int t, tn;
	cin >> tn;
	fr( t, tn )
	{
		q.clear( );
		q.pb( Tree( ) );
		scanf( "%d %d", &n, &m );
		int ans = 0;
		fi( n )
		{
			string s;
			cin >> s;
			fj( sz( s ) )
			{
				if ( s[j] == '/' )
					s[j] = ' ';
			}
			stringstream ss( s );
			int ct = 0;
			while ( ss >> s )
			{
				if ( q[ct].d.find( s ) != q[ct].d.end( ) )
					ct = q[ct].d[s];
				else
				{
					q[ct].d[s] = sz( q );
					q.pb( Tree( ) );
					ct = sz( q ) - 1;
				}
			}
		}

		fi( m )
		{
			string s;
			cin >> s;
			fj( sz( s ) )
			{
				if ( s[j] == '/' )
					s[j] = ' ';
			}
			stringstream ss( s );
			int ct = 0;
			while ( ss >> s )
			{
				if ( q[ct].d.find( s ) != q[ct].d.end( ) )
					ct = q[ct].d[s];
				else
				{
					++ ans;
					q[ct].d[s] = sz( q );
					q.pb( Tree( ) );
					ct = sz( q ) - 1;
				}
			}
		}

		printf( "Case #%d: %d\n", t + 1, ans );
	}
	return 0;
}