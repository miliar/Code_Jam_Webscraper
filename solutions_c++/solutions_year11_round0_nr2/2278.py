#include <algorithm>
#include <iostream>
#include <string>
#include <set>
#include <map>

using namespace std;

map< char, int > mp;

char combine[ 8 ][ 8 ];
char siktir[ 8 ][ 8 ];

bool isbasic ( char c )
{
	if( c == 'Q' || c == 'W' || c == 'E' || c == 'R' || 
			c == 'A' || c == 'S' || c == 'D' || c == 'F' )
			return true;
	return false;
}

void solve ()
{
	memset( combine, 0, sizeof( combine ) );
	memset( siktir, 0, sizeof( siktir ) );

	int n;
	string s;
	cin >> n;
	while( n-- )
	{
		cin >> s;
		combine[ mp[ s[ 0 ] ] ][ mp[ s[ 1 ] ] ] = s[ 2 ];
		combine[ mp[ s[ 1 ] ] ][ mp[ s[ 0 ] ] ] = s[ 2 ];
	}

	cin >> n;
	while( n-- )
	{
		cin >> s;
		siktir[ mp[ s[ 0 ] ] ][ mp[ s[ 1 ] ] ] = 1;
		siktir[ mp[ s[ 1 ] ] ][ mp[ s[ 0 ] ] ] = 1;
	}

	cin >> n >> s;
	int i, j;
	
	string cur;
	char c, t;
	for( i = 0; i < n; ++i )
	{
		c = s[ i ];
		if( cur.size() == 0 )
		{
			cur += c;
			continue;
		}
		t = cur[ cur.size() - 1 ];
		if( isbasic( c ) )
		{
			if( isbasic( t ) && combine[ mp[ c ] ][ mp[ t ] ] != 0 )
				cur[ cur.size() - 1 ] = combine[ mp[ c ] ][ mp[ t ] ];
			else
			{
				for( j = 0; j < cur.size(); ++j )
					if( isbasic( cur[ j ] ) && siktir[ mp[ cur[ j ] ] ][ mp[ c ] ] )
					{
						cur = "";
						break;
					}
				if( cur != "" )
					cur += c;
			}
		}
		else
			cur += c;
	}
	cout << "[";
	if( cur.size() > 0 )
	{
		cout << cur[ 0 ];
		for( i = 1; i < cur.size(); ++i )
			cout << ", " << cur[ i ];
	}
	cout << "]\n";
}

int main ()
{
	mp[ 'Q' ] = 0;
	mp[ 'W' ] = 1;
	mp[ 'E' ] = 2;
	mp[ 'R' ] = 3;
	mp[ 'A' ] = 4;
	mp[ 'S' ] = 5;
	mp[ 'D' ] = 6;
	mp[ 'F' ] = 7;


	int T, i;


	freopen( "b-large.in", "r", stdin );
	freopen( "b-large.out", "w", stdout );

	cin >> T;
	for( i = 1; i <= T; ++i )
	{
		cout << "Case #" << i << ": ";
		solve();
	}
}