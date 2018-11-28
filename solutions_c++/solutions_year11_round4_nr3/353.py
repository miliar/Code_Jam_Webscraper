#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int a[32];
vector < long long > f;

inline long long lcm ( long long a , long long b ) {
	return a / __gcd ( a , b ) * b;
}

int main() {
	long long i , j , n;
	long long ans;
	
	for (i = 2; i <= 2000000; i++) {
		for (j = 2; j * j <= i; j++)
			if ( i % j == 0 )
				break;
			
		if ( j * j > i ) {
			for (j = i * i; j <= 2000000000000LL; j *= i) {
				f.push_back ( j );
			}
		}
	}
	
	sort ( f.begin() , f.end() );
	int cases;
	
// 	printf ( "f.size = %d\n" , (int)f.size() );
	
	scanf ( "%d" , &cases );
	for (i = 1; i <= cases; i++) {
		scanf ( "%lld" , &n );
		ans = 1;
		
		for (j = 0; j < (int)f.size(); j++) {
			if ( f[j] > n ) break;
			if ( j == 0 || f[j - 1] != f[j] )
				++ ans;
		}
		
		if ( n == 1 ) ans = 0;
		
		printf ( "Case #%lld: %lld\n" , i , ans );
	}
	
	return 0;
}
