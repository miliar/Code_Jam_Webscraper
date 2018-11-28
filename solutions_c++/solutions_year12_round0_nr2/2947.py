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

int main()
{
	
	freopen( "test.txt" , "r" , stdin );
	freopen( "C:\\out.txt" , "w" , stdout );
	int T;
	cin >> T;

	int N;
	int S;
	int p;

	REP( cases , 1 , T + 1 )
	{
		printf( "Case #%d: " , cases );
		
		cin >> N >> S >> p;

		int count = 0;

		int n;

		REP( num , 0 , N )
		{
			cin >> n;

			if( n / 3 >= p )
			{
				++count;
				continue;
			}

			if( n % 3 == 0 && S > 0 && n / 3 + 1 >= p && n / 3 - 1 >= 0 && n / 3 + 1 <= 10 )
			{
				--S;
				++count;
				continue;
			}
			else if( n % 3 == 1 && n / 3 + 1 >= p && n / 3 + 1 <= 10 )
			{
				++count;
				continue;
			}
			else if( n % 3 == 2 && n / 3 + 1 >= p && n / 3 + 1 <= 10  )
			{ 
				++count;
				continue;
			}
			else if( n % 3 == 2 && n / 3 + 2 >= p && S > 0 && n / 3 + 2 <= 10 )
			{
				--S;
				++count;
				continue;
			}
			else
			{}
		 
		}

		cout << count << endl;
		
	}

	return 0;
}