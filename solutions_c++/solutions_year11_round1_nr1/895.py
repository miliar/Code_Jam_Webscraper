#include<stdio.h>

long long gcd(long long a, long long b) {
	if ( b == 0 ) {
		return a;
	}
	return gcd( b, a%b );
}

int main()
{
	int T;
	long long N, A, B;
	scanf("%d", &T);
	
	for ( int t = 1 ; t <= T ; t++ ) {
		scanf("%I64d %I64d %I64d", &N, &A, &B);
		printf("Case #%d: ", t);
		if ( !A && !B ) {
			puts("Possible");
		}
		else if ( A && !B ) {
			puts("Broken");
		}
		else if ( A != 100 && B == 100 ) {
			puts("Broken");
		}
		else if ( A == 100 && B == 100 ) {
			puts("Possible");
		}
		else if ( N >= 100/gcd(100,A) ) {
			puts("Possible");
		}
		else {
			puts("Broken");
		}
	}
	return 0;
}

