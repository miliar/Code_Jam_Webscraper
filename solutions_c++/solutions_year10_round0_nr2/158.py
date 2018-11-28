#include <iostream>

using namespace std;

#define N 3

long long a[N];

long long gcd( long long a, long long b ){
	if( b == 0 ){
		return a;
	}
	else{
		return gcd( b, a % b );
	}
	return 0;
}

int main(){
	
	int tc, Tc;
	
	freopen( "B-small-attempt1.in", "r", stdin );
    freopen( "b.small.out.txt", "w", stdout );

	scanf( "%d", &Tc );
	
	int n;
	
	for( tc = 1; tc <= Tc; tc++ ){
		
		scanf( "%d", &n );
		
		for( int i = 0; i < n; i++ ){
			scanf( "%I64d", a + i );
		}
		
		sort( a, a + n );
		
		long long maxT = 0;
		for( int i = 0; i < n - 1; i++ ){
			for( int j = i + 1; j < n; j++ ){
				maxT = gcd( maxT, a[j] - a[i] );
			}
		}
		
		long long maxg = -1;
		long long miny;
		for( long long y = 1; y * y <= maxT; y++ ){
			if( maxT % y == 0 ){
				long long min = ( y - a[n - 1] % y ) % y;
				bool flag = true;
				for( int i = 0; i < n; i++ ){
					if( ( a[i] + min ) % y != 0 ){
						flag = false;
					}
				}
				if( flag == true ){
					if( y > maxg ){
						maxg = y;
						miny = min;
					}
				}
				long long b = maxT / y;
				min = ( b - a[n - 1] % b ) % b;
				flag = true;
				for( int i = 0; i < n; i++ ){
					if( ( a[i] + min ) % b != 0 ){
						flag = false;
					}
				}
				if( flag == true ){
					if( b > maxg ){
						maxg = b;
						miny = min;
					}
				}
			}
		}
				
				
		
		printf( "Case #%d: %I64d\n", tc, miny );
	}
	
	return 0;
}
 
		
	
	
