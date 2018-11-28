
#include <iostream>
#include <string>
#include <cassert>

using namespace std;

string sfrom = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a zoo  q";
string sto   = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y qee  z";

int main()
{
	int m1[ 500 ];
	for ( int i = 0; i < (int)sto.length(); ++i )
	{
		m1[ sto[ i ] ] = sfrom[ i ];
	}
	for ( char c = 'a'; c <= 'z'; ++c )
		assert( 'a' <= m1[ c ] && m1[ c ] <= 'z' );
	assert( m1[ ' ' ] == ' ' );

	int T;
	char s[ 1000 ];
	cin >> T;
	cin.getline( s, sizeof( s ) );
	assert( s[ 0 ] == '\0' );
	for ( int t = 1; t <= T; ++t )
	{
		cin.getline( s, sizeof( s ) );
		for ( int i = 0; s[ i ] != '\0'; ++i )
			s[ i ] = m1[ s[ i ] ];
		cout << "Case #" << t << ": " << s << endl;
	}

	return 0;
}
