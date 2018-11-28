/*
"Problem A. Speaking in Tongues" < in.txt > out.txt

*/
#include <iostream>
#include <map>
using namespace std ;
int main ()
{
	string s1 = "abcdefghijklmnopqrstuvwxyz" ;
	string s2 = "yhesocvxduiglbkrztnwjpfmaq" ;
	map < char , char > Index ;
	for ( int i = 0 ; i < s1 . size() ; i ++ )
	{
		Index[ s1[ i ] ] = s2[ i ] ;
	}
	Index[ ' ' ] = ' ' ;
	int n = 0 , Case = 1 ;
	cin >> n ;
	string s ;
	ws( cin ) ;
	while ( n -- )
	{
		printf( "Case #%d: " , Case ++ ) ;
		getline( cin , s ) ;
		int i = 0 , l = s . size() - 1 ;
		while ( s[ i ] == ' ' ) i ++ ;
		while ( s[ l ] == ' ' ) l -- ;
		for (  ; i <= l ; i ++ )
		{
			putchar( Index[ s[ i ] ] ) ;
		}
		cout << endl ;
	}
}
