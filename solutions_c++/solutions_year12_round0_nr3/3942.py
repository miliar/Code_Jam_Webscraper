#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

string rotate( string a )
{
	string b;
	b = a.c_str()+1;
	b.push_back( a[0] );
	if( b[0] == '0' )
		return rotate( b );
	return b;
}

int main()
{
	freopen( "C:/Users/Serdar/Desktop/C.in" , "r" , stdin );
	freopen( "C:/Users/Serdar/Desktop/C.out" , "w" , stdout );

	int N;
	int A,B;
	char str[30];
	string S,BS;

	cin >> N;

	int ca = 0;
	while( N-- )
	{
		ca++;
		int cnt = 0;
		cin >> A >> B;
		sprintf( str , "%d" , B );
		BS = str;

		for( int i = A ; i <= B ; i++ )
		{
			sprintf( str , "%d" , i );
			S = str;

			string k = rotate( S );
			while( k != S )
			{
				if( k >= S && k <= BS  )
					cnt++;
				k = rotate(k);
			}
		}



		printf("Case #%d: %d\n" , ca , cnt );

	}

	return 0;
}
