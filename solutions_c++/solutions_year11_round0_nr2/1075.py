#include<iostream>
#include<string>
#include<vector>

using namespace std;
const int MAXN = 26; 


char m[ MAXN ][ MAXN ];
bool o[ MAXN ][ MAXN ];
string s;

int main()
{
	freopen("input.txt", "rt", stdin );
	freopen("output.txt", "wt", stdout );
	int tests;
	cin >> tests;
	for( int t = 1; t <= tests; t++ )
		{
			memset( o, 0, sizeof( o ));
			memset( m, 0, sizeof( m ));
			int c , d , l;
			cin >> c;
			for( int i = 0; i < c; i++ )
			{	
				cin >> s;
				m[ s[ 0 ] - 'A'][ s[ 1 ] - 'A' ] = s[ 2 ];
				m[ s[ 1 ] - 'A'][ s[ 0 ] - 'A' ] = s[ 2 ];
			}
			cin >> d;
			for( int i = 0; i < d; i++ )
				{
					cin >> s;
					o[ s[ 0 ] - 'A' ][ s[ 1 ] - 'A' ] = true;
					o[ s[ 1 ] - 'A' ][ s[ 0 ] - 'A' ] = true;
				}
			cin >> l;
			cin >> s;
			vector< char > lst;
			for( int i = 0; i < s.size(); i++ )
				{
					if( lst.size() == 0 )
						{
							lst.push_back( s[ i ] ); 
							continue;
						}
					if( m[ lst.back() - 'A' ][ s[ i ] - 'A' ] )
						{
							lst[ lst.size() - 1 ] =  m[ lst.back() - 'A' ][ s[ i ] - 'A' ];
							continue;
						}
					bool clr = false;
					for( int j = 0; j < lst.size(); j++ )
						if( o[ lst[ j ] - 'A' ][ s[ i ] - 'A' ] )
							{
							clr = true;
							break;
							}
					if( clr )
						lst.clear();
					else
						lst.push_back( s[ i ] );
				}
			cout << "Case #" << t << ": [";
			for( int i = 0; i < lst.size(); i++ )
				{
					cout << lst[ i ];
					if( i + 1 != lst.size() )
						cout << ", ";
				}
			cout << "]" << endl;


		} 
	return 0;
}