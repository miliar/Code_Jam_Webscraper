#include<iostream>
#include<cstdio>
#include<cmath>

using namespace std;

const double t = (double)(sqrt(5.0)+1)/2;

int main()
{
	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int test_cases, casen = 0;
	for ( scanf( "%d", &test_cases ); test_cases > 0; test_cases -- )
	{
		long long ans = 0;
		int A1, A2, B1, B2;
		scanf( "%d %d %d %d", &A1, &A2, &B1, &B2 );
		for (int i = A1; i <= A2; i++ )
		{
			int l1 = i, l2 = (int)floor(i * t);
			if ( l1 < B1 ) l1 = B1;
			if ( l2 > B2 ) l2 = B2;
			if ( l2 >= l1 ) ans += l2 - l1 + 1;		
		}
		for (int i = B1; i <= B2; i++ )
		{
			int l1 = i + 1, l2 = (int)floor(i * t);
			if ( l1 < A1 ) l1 = A1;
			if ( l2 > A2 ) l2 = A2;
			if ( l2 >= l1 ) ans += l2 - l1 + 1;	
		}
		printf( "Case #%d: ", ++ casen );
		cout << (long long)(A2 - A1 + 1) * (B2 - B1 + 1) - ans << endl;
	}
}
