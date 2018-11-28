#ifdef DEBUG
	#define D(x...) fprintf(stderr,x);
#else
	#define D(x...) 0
#endif
#include <cstdio>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define MAX_SIEVE 2000000

int main() {
	vector<int> smallprimes;
	vector<bool> sieve = vector<bool>(MAX_SIEVE,0);
	for (int i = 2; i < MAX_SIEVE; i++) {
		if (sieve[i]) continue;
		smallprimes.push_back(i);
		for (int j = i*2; j < MAX_SIEVE; j += i) sieve[j] = 1;
	}

	int nTests;
	scanf("%d ",&nTests);
	for (int test=1;test<=nTests;test++) {
		if (1) fprintf(stderr,"Case %d/%d\n",test,nTests);
		
		long long N;
		scanf("%lld",&N);

		if (N == 1) {
			printf("Case #%d: 0\n",test);
			continue;
		}

		long long ans = 1;

		for (int i = 0; i < smallprimes.size(); i++) {
			long long tmp = smallprimes[i];
			if (tmp > N) break;
			int j = -1;
			while (tmp <= N) {
				tmp *= (long long) smallprimes[i];
				j++;
			}
			ans += j;
		}
		
		printf("Case #%d: %lld\n",test,ans);
	}
}
