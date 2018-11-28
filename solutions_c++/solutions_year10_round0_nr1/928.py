#include <cstdio>
#include <cstring>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>

#define Eo(x) { std::cerr << #x << " = " << x << std::endl; }

typedef long long int64;

int main() {
	int t = 0, tc;
	unsigned n, k;
	for(scanf("%d", &tc); t < tc; t++) {
		scanf("%u%u", &n, &k);
		unsigned mask = (1 << n) - 1;
		k &= mask;
		printf("Case #%d: %s\n", t+1, k == mask ? "ON" : "OFF");
	}
	return 0;
}
