#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

int perm( int a, int b )
{
	int digits, temp;
	temp = a;
	digits = 0;
	while( temp )
	{
		digits++;
		temp /= 10;
	}

	vector <int> ad( digits ), bd( digits );
	int ptr = digits - 1;
	while ( a )
	{
		ad[ ptr ] = a%10;
		bd[ ptr ] = b%10;
		ptr--;
		a /= 10;
		b /= 10;
	}

	for(  int start = 0; start < digits; start++ )
	{
		int flag = 1;
		for( int k = start, iter = 0; iter < digits; k = ( k + digits + 1 ) % digits, iter++ )
		{
			if( ad[ k ] != bd[ iter ] )
			{
				flag = 0;
				break;
			}

		}
		if( flag == 1 )
			return 1;
	}
	return 0;
}

			




int main()
{
	int t;
	cin >> t;

	for( int x = 0; x < t; x++ )
	{

	int a,b;
	cin>>a>>b;
	int count = 0;

	for( int i = a; i < b; i++ )
	{
		for( int j = i+1; j <= b; j++ )
		{
			if( perm( i,j ) )
				count++;
		}
	}

	cout << "Case #" << x + 1 << ": " << count << endl;

	}
	return 0;
}


	
