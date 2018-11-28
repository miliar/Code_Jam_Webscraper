#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long LL;

LL W, D, GW, G, N, PD, PG, cas;

LL gcd(LL a, LL b) {
	return b == 0 ? a : gcd(b, a % b);
}

bool gao() {
	if (PG == 0)
		return PD == 0;
	if (PG == 100)
		return PD == 100;
	return 100/gcd(100, PD) <= N;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> cas;
	for (int c = 1; c <= cas; ++c) {
		cin >> N >> PD >> PG;
		printf("Case #%d: %s\n", c, gao() ? "Possible" : "Broken");
	}
	return 0;
}