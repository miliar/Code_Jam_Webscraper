#include <iostream>
#include <memory.h>
#include <vector>

using namespace std;

int power( int a, int b )
{
	if ( b == 0 ) return 1;
	if ( b == 1 ) return a;
	return a * power( a, b - 1 );
}

int count_recycled_pairs( int a, int b, int cur, int digits )
{
	int count = 0;

	vector< int > numbers;
 	for ( int i = 0; i < digits - 1; i++ )
	{
		int toLeft = 0;
		int toRight = cur / power( 10, i + 1 );
		for ( int j = 0; j <= i; j++ )
		{
			int curDigit = ( cur / power( 10, j ) ) % 10;
			toLeft += power( 10, digits - ( i + 1 ) + j ) * curDigit;
		}
		int newNumber = toLeft + toRight;
		if ( newNumber < a || newNumber > b || cur >= newNumber )
		{
			continue;
		}
		bool found = false;
		for ( int j = 0; j < numbers.size(); j++ )
		{
			if ( numbers[ j ] == newNumber )
			{
				found = true;
			}
		}
		if ( found )
		{
			continue;
		}
		//cout << a << " <= " << cur << " < "  << newNumber << " <= " << b << "\n";
		count++;
		numbers.push_back( newNumber );
	}
	return count;
}

int main( int argc, char* argv[] )
{
	std::string line;
	int num;
	cin >> num;
	//cout << "num: " << num << "\n";

	int cur = 0;
	while ( cur++ < num )
	{
		int a, b, count;
		cin.ignore();
		cin >> a >> b;
		//cout << "a: " << a << " b: " << b << "\n";
		count = 0;
		for ( int i = a; i <= b; i++ )
		{
			int digits = 0;
			int temp = i;
			while ( temp > 0 )
			{
				digits++;
				temp /= 10;
			}
			count += count_recycled_pairs( a, b, i, digits );
		}
		cout << "Case #" << cur << ": " << count << "\n";
		//if ( cur >= 3 ) return 0;
	}	
	return 0;
}
