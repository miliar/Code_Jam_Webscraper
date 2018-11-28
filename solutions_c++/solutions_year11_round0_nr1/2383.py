#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector< int > v1;
vector< int > v2;
vector< pair< char, int > > v;

int solve ()
{
	int n;
	char c;
	int b;
	v1.erase(v1.begin(), v1.end());
	v2.erase(v2.begin(), v2.end());
	v.erase(v.begin(), v.end());
	cin >> n;
	for( int j = 0; j < n; ++j )
	{
		cin >> c >> b;
		if( c == 'O' )
			v1.push_back( b );
		else
			v2.push_back( b );
		v.push_back( make_pair( c, b ) );
	}

	int p1 = 1, p2 = 1;

	int i1 = 0, i2 = 0, i = 0;

	bool b1, b2;

	int ans = 0;

	while( i < n )
	{
		++ans;
		b1 = b2 = false;
		c = v[ i ].first;
		b = v[ i ].second;
		if( c == 'O' && p1 == b )
		{
			++i;
			++i1;
			b1 = true;
		}
		if( c == 'B' && p2 == b )
		{
			++i;
			++i2;
			b2 = true;
		}

		if( !b1 && i1 < v1.size() && p1 != v1[ i1 ] )
		{
			if( v1[ i1 ] < p1 )
				--p1;
			else
				++p1;
		}

		if( !b2 && i2 < v2.size() && p2 != v2[ i2 ] )
		{
			if( v2[ i2 ] < p2 )
				--p2;
			else
				++p2;
		}
	}
	return ans;
}

int main ()
{
	int T;
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );
	cin >> T;
	for( int i = 1; i <= T; ++i )
		cout << "Case #" << i << ": " << solve() << endl;
	return 0;
}