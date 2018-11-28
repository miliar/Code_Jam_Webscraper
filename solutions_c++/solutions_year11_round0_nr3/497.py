#include <cstdio>
#include <cstdlib>
#include <climits>

#include <iostream>
#include <algorithm>

using namespace std;

long long task() {
	int n, x = 0, m = INT_MAX;
	long long sum = 0;
	scanf("%d", &n);
	
	for (int i = 0; i < n; i++) {
		int val;
		scanf("%d", &val);
		
		x ^= val;
		sum += val;
		m = min(m, val);
	}
	
	if (x != 0) return -1;
	return sum - m;
}

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		long long r = task();
		if (r == -1) printf("Case #%d: NO\n", i);
		else printf("Case #%d: %lld\n", i, r);
	}
}

