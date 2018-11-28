//For Future
//By JFantasy

#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

typedef long long LL;

const int maxn = 1000005;

int prime[maxn];
bool mk[maxn];

void getprime() {
	memset( mk , 0 , sizeof(mk) );
	for ( int i = 2; i < maxn; i++ ) {
		if ( !mk[i] ) prime[++prime[0]] = i;
		for ( int j = 1; j <= prime[0] && i * prime[j] < maxn; j++ ) {
			mk[i*prime[j]] = 1;
			if ( i % prime[j] == 0 ) break;
		}	
	}
}

int main() {
	getprime();
	int cas , q = 0;
	scanf( "%d" , &cas );
	while ( cas-- ) {
		LL n;
		cin >> n;
		LL ans = 1;
		for ( int i = 1; i <= prime[0]; i++ ) {
			LL now = prime[i];
			while ( n >= now*prime[i] ) {
				ans++;
				now = now * prime[i];
			}
		}
		if ( n == 1 ) ans = 0;
		printf( "Case #%d: %lld\n" , ++q , ans );
	}
	return 0;
}
