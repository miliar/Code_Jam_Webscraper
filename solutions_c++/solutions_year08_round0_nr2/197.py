#include <stdio.h>
#include <set>
#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>

using namespace std;

int main()
{
	int case_num, n, m;
	
	freopen( "D:\\output.txt", "w", stdout );

	scanf( "%d", &case_num );

	for( int k=1; k<=case_num; ++k )
	{
		int t, a, b;
		scanf( "%d%d%d", &t, &a, &b );
		
		map<int, int> A, B;

		for( int i=0; i<a; ++i )
		{
			int t1, t11, t2, t22;
			scanf( "%d:%d %d:%d", &t1, &t11, &t2, &t22 );
			t1 = t1*60 + t11;
			t2 = t2*60 + t22;

			--A[t1];
			++B[t2+t];
		}

		for( int i=0; i<b; ++i )
		{
			int t1, t11, t2, t22;
			scanf( "%d:%d %d:%d", &t1, &t11, &t2, &t22 );
			t1 = t1*60 + t11;
			t2 = t2*60 + t22;

			--B[t1];
			++A[t2+t];
		}

		int ansA = 0, sum = 0;
		for( map<int,int>::const_iterator iter = A.begin();
			iter != A.end();
			++iter )
		{
			sum += iter->second;
			if( sum < 0 )
			{
				ansA -= sum;
				sum = 0;
			}
		}
		
		int ansB = 0;
		sum = 0;
		for( map<int,int>::const_iterator iter = B.begin();
			iter != B.end();
			++iter )
		{
			sum += iter->second;
			if( sum < 0 )
			{
				ansB -= sum;
				sum = 0;
			}
		}

		printf( "Case #%d: %d %d\n", k, ansA, ansB );
	}

	return 0;
}
