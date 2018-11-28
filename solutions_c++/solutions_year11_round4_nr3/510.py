#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;

#define NPRIME 1000001
#define MAXNUMPRIME 78500
typedef long long LL;

int nCase=1, T, N;

bool notPrime[NPRIME] = {false};
LL prime[MAXNUMPRIME]={2};
int numPrime = 1;


void getPrimeTable() {
	for( LL x=3;x<NPRIME;x+=2) {
		if( !notPrime[x] ) {
			prime[numPrime++] = x;
			for( LL j = (x*3) ; j<NPRIME ; j+=(x<<1) ) notPrime[j] = true;
		}
	}
}

int getMax(int x) {
	bool isPrime = true;
	int cnt = 1;
	for ( int i=0;i<numPrime;++i) {
		if ( prime[i] > x ) break;
		if ( x%prime[i]==0 ) isPrime = false;
		for ( LL t = prime[i] ; t<=x; t *= prime[i] ) {
			++cnt;
		}
	}
	if( isPrime ) {
		++cnt;
	}
	return cnt;
}
int getMin(int x) {
	bool isPrime = true;
	int cnt = 0;
    for ( int i=0;i<numPrime;++i) {
		if ( prime[i] > x ) break;
		++cnt;
	}
	return cnt;
}



int main()
{
	getPrimeTable();
	
	scanf("%d", &T);
	while(T-->0) {
		scanf("%d", &N);
		int ans;
		if ( N==1 ) ans = 0;
		else {
			int M=getMax(N), m=getMin(N);
//			printf("N=%3d, (min, max)=(%d, %d), diff=%d\n", N, m, M, M-m);
			ans = M-m;
		}
		printf( "Case #%d: %d\n", nCase++, ans);
	}
	return 0;
}
