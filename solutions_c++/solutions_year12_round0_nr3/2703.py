#include <stdio.h>
#include <math.h>
#include <set>
#include <string>
#include <iostream>

using namespace std;

int count( int A, int B )
{
	set<string> s;

	for( int d = 10; d < B; d *= 10 )
	{
		for( int i = A; i < B; i++ )
		{
			int n = i;
			int m;

			int mod = n % d;
			m = n / d;
			int digits = log10(m) + 1;
			m += mod * pow(10, digits);

			if( n < m && m <= B )
			{
				char l[128];
				sprintf( l, "%d %d", n, m );
				s.insert(l);
			}
		}
	}
	return (int)s.size();
}

int main()
{
	int T;
	cin >> T;

	for( int t = 0; t < T; t++ )
	{
		int A;
		int B;

		cin >> A;
		cin >> B;
		printf( "Case #%d: %d\n", t+1, count( A, B ));
	}

}