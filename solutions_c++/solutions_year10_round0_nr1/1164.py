#define LOCAL

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>

#include <iostream>
#include <algorithm>
#include <memory>
#include <vector>
#include <string>
#include <set>
#include <map>

#define PB(a) push_back(a)
#define MP(a, b) make_pair(a, b)

using namespace std;

typedef long long int64;

int T;
             
int main() {
	#ifdef LOCAL
		freopen("input.txt", "rt", stdin);
		freopen("output.txt", "wt", stdout);
	#endif

	scanf("%d", &T);

	for (int cs = 1; cs <= T; cs++) {
		printf("Case #%d: ", cs);

		int n, k;
		scanf("%d %d", &n, &k);

		if (n == 1) {
			if (k % 2 == 1) printf("ON");
			else printf("OFF");
		}
		else {
			int p = 1 << n;
			if (k % p == p-1) printf("ON");
			else printf("OFF");
		}

		printf("\n");
	}

	return 0;
}

