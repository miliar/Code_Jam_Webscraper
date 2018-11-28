// Adrian Kügel
#include <stdio.h>
#include <vector>
#include <set>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <map>
#include <assert.h>
#include <limits.h>
#include <complex>
#include <algorithm>
#include <ctype.h>
#include <string>
using namespace std;

typedef set<int> SI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef complex<double> tComp;

int primes[1000];
char comp[1001];
char have[1001];

int main() {
	int tc, l = 0;
	for (int i=2; i<=1000; ++i) {
		if (!comp[i]) {
			primes[l++] = i;
			for (int j=i*i; j<=1000; j+=i)
				comp[j] = 1;
		}
	}
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		int a, b, p;
		scanf("%d %d %d", &a, &b, &p);
		memset(have, 0, sizeof(have));
		int cnt = 0;
		for (int i=a; i<=b; ++i) {
			if (have[i])
				continue;
			have[i] = 1;
			++cnt;
			queue<int> Q;
			Q.push(i);
			while(!Q.empty()) {
				int c = Q.front();
				Q.pop();
				for (int j=a; j<=b; ++j) {
					if (have[j]) continue;
					for (int k=0; k<l; ++k) {
						if (primes[k] < p)
							continue;
						if (c%primes[k]== 0 && j%primes[k] == 0) {
							have[j] = 1;
							Q.push(j);
							break;
						}
					}
				}
			}
		}
		printf("%d\n", cnt);
	}
	return 0;
}
