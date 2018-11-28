#include <iostream>
using namespace std;

int main()
{
	
	long long int i, j, now, test = 0, t, rate, C, L, P;
	
	
	freopen( "B-large.in", "r", stdin );
	freopen( "B-out.txt", "w", stdout );
	
	scanf( "%lld", &t );
	while ( t-- )
	{
		scanf( "%lld %lld %lld", &L, &P, &C ); 
		
		now = L * C;
		rate = C;
		for ( i = 0; now < P; ++i )
		{
			now = now * rate;
			rate *= rate;
		}
		printf( "Case #%lld: %lld\n", ++test, i );
	}
	
	return 0;
}
