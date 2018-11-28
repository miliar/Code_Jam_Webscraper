#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

typedef long long LL;

int t[1005];
LL sv[1005];
int rv[1005];

int n, k, r;

void alg() {
	scanf("%d %d %d", &r, &k, &n);
	int sum = 0;
	for (int i = 0; i < n; ++i) {
		scanf("%d", &t[i]);
		sum += t[i];
		sv[i] = rv[i] = -1;
	}
	if (sum <= k) {
		printf("%lld\n", LL(r) * sum);
		return;
	}
	int c = 0;
	int rounds = 0;
	LL csum = 0;
	while (rounds < r) {
		if (rv[c] >= 0) {
			int a = (r - rounds) / (rounds - rv[c]);
			csum += a * (csum - sv[c]);
			rounds += (rounds - rv[c]) * a;
			for (int i = 0; i < n; ++i)
				sv[i] = rv[i] = -1;
			continue;
		}
		rv[c] = rounds;
		sv[c] = csum;
		int p = c;
		int cs = 0;
		while (cs + t[p] <= k) {
			cs += t[p];
			p = (p + 1) % n;
		}
		csum += cs;
		c = p;
		++rounds;
	}
	printf("%lld\n", csum);
}

int main() {
	int d;
	scanf("%d", &d);
	for (int i = 1; i <= d; ++i) {
		printf("Case #%d: ", i);
		alg();
	}
}
