#define DBGi
// Grzegorz Guspiel
#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <algorithm>
using namespace std;

#ifdef DBG
#define debug(fmt, ...) printf(fmt, ## __VA_ARGS__ )
#else
#define debug(fmt, ...)
#endif

#define REP(ii,nn) for(int (ii)=0; (ii)<int(nn); (ii)++)
#define FOR(ii,bb,ee) for(int (ii)=(bb); (ii)<=(ee); (ii)++)
#define REPD(ii,nn) for(int (ii)=(nn)-1; (ii)>=0; (ii)--)
#define FORD(ii,bb,ee) for(int (ii)=(ee); (ii)>=(bb); (ii)--)
#define FORE(ii,vv) for(__typeof((vv).begin()) ii=(vv).begin(); (ii)!=(vv).end(); (ii)++)
#define ST first
#define ND second
#define PB push_back
#define PP pop_back
#define MP make_pair

typedef long long lld;

const int max_sieve = 2000100;
bool is_prime[max_sieve];
vector<int> primes;

int custom_log(lld p, lld n) {
	lld i = p;
	int r = -1;
	while(i <= n) {
		i *= p;
		r++;
	}
	debug("add %d for p=%lld n=%lld\n", r, p, n);
	return r;
}

int main() {
	REP(i,max_sieve) is_prime[i] = true;
	FOR(i,2,max_sieve-1) if(is_prime[i]) {
		for(int j = 2; j * i < max_sieve; j++)
			is_prime[j * i] = false;
		primes.PB(i);
	}
	//REP(i,20) printf("%d\n", primes[i]);
	int z; scanf("%d", &z);
	FOR(zz,1,z) {
		lld n; scanf("%lld", &n);
		lld result = 1;
		for(int i = 0; lld(primes[i]) * primes[i] <= n; i++)
			result += custom_log(primes[i], n);
		if(n == 1) result = 0;
		printf("Case #%d: %lld\n", zz,result);
	}
	return 0;
}

