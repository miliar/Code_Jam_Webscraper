#include <iostream>
#include <queue>
using namespace std;


long long int f[ 10000000 ];
int pos[ 1010 ];
int r, k, n;
int p[ 1010 ];
int total, now;
unsigned long long int sum, ans;
queue< int > que;

int main()
{
	
	int test, t = 0, i, x;
	
	freopen( "C-large.in", "r", stdin );
	freopen( "Cout.txt", "w", stdout );
	scanf( "%d", &test );
	
	while ( test-- )
	{
		
		while ( !que.empty() )
			que.pop();
		memset( pos, -1, sizeof( pos ) );
		
		scanf( "%d %d %d", &r, &k, &n );
		
		for ( i = 0; i < n; ++i )
		{
			scanf( "%d", &p[ i ] );
			que.push( i );
		}
		
		f[ 0 ] = 0;
		total = 0;
		while ( pos[ now = que.front() ] == -1 )
		{
			que.push( now );
			que.pop();
			pos[ now ] = ++total;
			
			sum = p[ now ];
			
			while ( sum + p[ que.front() ] <= k && que.front() != now )
			{
				sum += p[ que.front() ];
				que.push( que.front() );
				que.pop();
			}
			
			f[ total ] = sum + f[ total - 1 ];
		}
		
		
		if ( r > total )
		{
			r -= total;
			ans = f[ total ];
			
			x = total - pos[ now ] + 1;
			sum = f[ total ] - f[ pos[ now ] - 1 ];
			
			ans += sum * ( r / x );
			x = r % x;
			
			ans += f[ pos[ now ] - 1 + x ] - f[ pos[ now ] - 1 ];
		}
		else
			ans = f[ r ];
			
		printf( "Case #%d: %llu\n", ++t, ans );
		
	}
	
	return 0;
}
