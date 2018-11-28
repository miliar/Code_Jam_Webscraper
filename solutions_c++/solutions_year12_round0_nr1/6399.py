#include<iostream>
#include<stdio.h>

using namespace std;

char map[] = "yhesocvxduiglbkrztnwjpfmaq";
int main()
{
	freopen( "in.txt", "r" , stdin );
	freopen( "data.out", "w", stdout );

	int T;
	char str[ 110 ];

	cin >> T;
	gets( str );
	for( int t = 1; t <= T; t ++ ) {
		cout << "Case #" << t << ": ";
		
		memset( str, '\0', 110 );
		
		
		gets( str );
		for( int i = 0; str[i] != '\0'; i ++ ) {
			if( str[i] == ' ' ) cout << ' ';
			else cout << map[ str[ i ] - 'a' ];
		}
		cout << "\n";
	}

	return 0;
}