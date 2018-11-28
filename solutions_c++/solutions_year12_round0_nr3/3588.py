#include <stdio.h>
#include <stdlib.h>
#include <vector>
using namespace std;
long pow ( long a, int b )
{
	if ( b == 0 )
		return 1;
	long a1 = a;
	for ( int i = 0 ; i < b-1; i++ )
	{
		a = a*a1;
	}
	return a;
};

int order( long number )
{
	long a;
	for ( int i = 0; i < 7; i ++ )
	{
		a = number / pow ( 10, i );
		if ( a == 0 )
			return i;
	}
};
int sameDigits ( long a, long b )
{
	long incA = a, incB = b;
	int a1, b1, notSameOrder = 0;
	bool have;
	int i, j, aOrder = order ( a ), bOrder = order ( b );
	for ( i = 1; i <= aOrder; i++ )
	{
		a1 = a % 10;
		a = a / 10;
		notSameOrder++;
		for ( b = incB, have = false, j = 1; j <= bOrder; j ++ )
		{
			b1 = b % 10;
			if ( a1 == b1 )
			{
				have = true;
				break;
			}
			b = b / 10;
		}
		if ( have == false )
			return notSameOrder;
	}
	if ( aOrder == 1 || bOrder == 1 )
		return notSameOrder;
	return 0;
};

bool check ( long incA, long incB )
{
	int i, ost, nullCount = 0;
	long a1 = incA, a = incA, b = incB;
	do
	{
		if ( a == b )
		{
			return true;
		}
		if ( (ost = a % 10) == 0 )
		{
			nullCount++;
			a = (( a - ost ) / 10) + (ost * pow ( 10, order ( a ) - 1 ));
		}
		else 
		{
			a = (( a - ost ) / 10) + (ost * pow ( 10, order ( a ) - 1 + nullCount ));
			nullCount = 0;
		}
	}
	while ( a1 != a );
	return false;
};

int main()
{
	FILE *input, *output;
	unsigned char InputSymbol = 0;
	int numberOfTests, i, result [ 100 ];
	long a, b, j, k, notSame;
	if ( ( input = fopen ( "C:\\test.txt", "r" ) ) == 0 )
		return -1;
	fscanf ( input, "%d", &numberOfTests );
	for ( i = 0 ; i < numberOfTests; i++ )
	{
		result [ i ] = 0;
		fscanf ( input, "%ld", &a );
		fscanf ( input, "%ld", &b );
		for ( j = a; j <=b; j ++ )
		{
			for ( k = j+1; k <=b; k ++ )
			{
				if ( (notSame = sameDigits( k, j )) == 0 && sameDigits ( j, k ) == 0 )
				{
					if ( check (k, j) )
						result [ i ] ++;
				}
				else
				{
					if ( notSame > 1 )
					{
						k = (k - k%10) + pow ( 10, notSame - 1);
						k--;
					}
				}
			}
		}
	}
	fclose ( input );
	if ( ( output = fopen ( "C:\\Output.txt", "w" ) ) == 0 )
		return -1;
	for ( i = 0; i < numberOfTests; i++ )
	{
		fprintf ( output, "Case #%d: %d\n", i+1, result[i]);
	}
	fclose ( output );
	return 0;
}