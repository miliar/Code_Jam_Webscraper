// ZOJ.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <cstdio>
#include <map>
#include <queue>

#define REP(i,j,k) for(int i = j ; i < k ; ++i)
#define INF (0x7FFFFFFF)
#define MAX (875714)   
//#define MAX (100)

using namespace std;



char S[ 20 ];
char T[ 20 ];
bool check( int m , int n )
{
	sprintf( S , "%d" , m );
	sprintf( T , "%d" , n );

	string orig = S;
	string target = T;

	orig.append( orig );

	if( orig.find( target ) == string::npos )
	{
		return false;
	}
	else
	{
		return true;
	}

}


int main()
{
	freopen( "test.txt" , "r" , stdin );
	//freopen( "C:\\out.txt" , "w" , stdout );

	int T;
	cin >> T;

	REP( cases , 1 , T + 1 )
	{
		printf( "Case #%d: " , cases );

		int A;
		int B;
		cin >> A >> B;

		int count = 0;

		REP( n , A , B + 1 )
		{
			REP( m , n + 1 , B + 1 )
			{
				if( check( m , n ) )
				{
					++count;
				}
			}
		}

		cout << count << endl;

	}

	return 0;
}