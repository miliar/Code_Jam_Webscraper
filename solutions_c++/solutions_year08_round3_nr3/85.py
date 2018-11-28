#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#include <vector>
#include <set>
#include <map>

using namespace std;

long long A[10005];
long long limits[10005];
long long acc[10005];

long long mod = 1000000007;
//long long mod = 3;

long long cases, limits_cnt, gen_array_cnt, X, Y, Z;

void generate() {
	long long i;
	for (i=0; i<limits_cnt; i++) {
		limits[i] = A[i % gen_array_cnt];
		A[i % gen_array_cnt] = (X * A[i % gen_array_cnt] + Y * (i+1) ) % Z;
	}

	/*
	for (i=0; i<limits_cnt;i++ ) {
		printf("Limit %lld is %lld\n", i, limits[i] );
	}
	*/
}

int main ( int argc, char ** argv ) {
	long long nr,x,y;
	
	scanf("%lld", &cases);
	for (nr=0; nr<cases; nr++) {
		scanf("%lld %lld %lld %lld %lld", &limits_cnt, &gen_array_cnt, &X, &Y, &Z);
		for (x=0; x<gen_array_cnt; x++) {
			scanf("%lld", &A[x]);
		}
		generate();
		for (y=0; y<limits_cnt; y++) {
			acc[y] = 1;
			for (x=0; x<y; x++) {
				if ( limits[ x ] >= limits[ y ] ) continue;
				acc[y] = (acc[y] + acc[x]) % mod;
			}
		}
		long long sum = 0;
		for (x=0; x<limits_cnt; x++) {
	//		printf("Acc %lld is %lld\n", x, acc[x]);
			sum = ( sum + acc[x] ) % mod;
		}
		printf("Case #%lld: %lld\n", nr+1, sum);
	}
	return 0;
}
