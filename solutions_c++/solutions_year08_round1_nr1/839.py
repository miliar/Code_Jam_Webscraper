#include<iostream>
#include<fstream>
#include<cstdlib>
using namespace std;

void swap( int &a, int &b )
{
	int temp = b;
	b = a;
	a = temp;
}

int main()
{
	fstream inClient( "A-small-attempt0.in", ios::in );
	fstream outClient( "A-small-out.txt", ios::out );

	int numOfCases;
	inClient >> numOfCases;

	for( int i = 0; i < numOfCases; i++ )
	{
		int n;
		inClient >> n;

		int *aPtr, *bPtr;
		aPtr = new int [ n ];
		bPtr = new int [ n ];

		for( int j = 0; j < n; j++ )
		{
			inClient >> aPtr[ j ];
		}

		for( int j = 0; j < n; j++ )
		{
			inClient >> bPtr[ j ];
		}

		for( int j = 0; j < n - 1; j++ )
		{
			if( aPtr[ j ] > aPtr[ j + 1 ] )
			{
				for( int k = j; k >= 0; k-- )
				{
					if( aPtr[ k ] > aPtr[ k + 1 ] )
					{
						swap( aPtr[ k ], aPtr[ k + 1 ] );
					}
					else
						break;
				}
			}
		}

		for( int j = 0; j < n - 1; j++ )
		{
			if( bPtr[ j ] < bPtr[ j + 1 ] )
			{
				for( int k = j; k >= 0; k-- )
				{
					if( bPtr[ k ] < bPtr[ k + 1 ] )
					{
						swap( bPtr[ k ], bPtr[ k + 1 ] );
					}
					else
						break;
				}
			}
		}

		int sum = 0;
		for( int j = 0; j < n; j++ )
		{
			sum += ( aPtr[ j ] * bPtr[ j ] );
		}

		outClient << "Case #" << i + 1 << ": " << sum << endl;

		delete [] aPtr;
		delete [] bPtr;
	}
	
	inClient.close();
	outClient.close();
	
	return 0;
}