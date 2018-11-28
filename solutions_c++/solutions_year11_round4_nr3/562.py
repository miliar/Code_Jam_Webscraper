#include<algorithm>
#include<cstring>
#include<cstdio>
#include<vector>
#include<queue>
#include<cmath>
#include<set>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define FOR(x,y,z) for(int x=y;x<=z;++x)
#define FORD(x,y,z) for(int x=y;x>=z;--x)
#define FOReach(x,Z) for(__typeof((Z).begin()) x=(Z).begin();x!=(Z).end();++x)
#define REP(x,y) for(int x=0;x<y;++x)

#define PB push_back
#define ALL(X) (X).begin(),(X).end()
#define SZ(X) ((int)(X).size())
#define CLR(X,x) memset(X, x, sizeof(X))

#define MP make_pair
#define ST first
#define ND second

#define DBG

#ifdef DBG
#define debug printf
#else
#define debug(fmt, ...)
#endif


const int MAX = 1000000;
const int INF = 1000000001;

LL n;

int logp(LL p) {
	int ret = 0;
	LL w = 1;
	while(w*p <= n)
		++ret,
		w *= p;
	return ret;
}

VI primes;

bool isPrime(int x) {
	if(x < 4)
		return true;
	if(x % 2 == 0)
		return false;
	for(int i=0;i<primes.size() && primes[i]*primes[i] <= x;++i)
		if(x % primes[i] == 0)
			return false;
	return true;
}

void genPrimes() {
	FOR(i,2,MAX)
		if(isPrime(i))
			primes.PB(i);
}


main() {
	genPrimes();
	int Z;
	scanf("%d", &Z);
	FOR(z,1,Z)
	{
		printf("Case #%d: ", z);
		scanf("%lld", &n);
		if(n == 1) {
			printf("0\n");
			continue;
		}
		int ans = 1;
		for(int i = 0; i < primes.size() && (LL)primes[i]*primes[i] <= n; ++i)
		{
			int p = primes[i];
			ans += logp(p)-1;
		}
		printf("%d\n", ans);
	}
	return 0;
}

