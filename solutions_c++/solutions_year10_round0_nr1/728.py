#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <iostream>
#include <vector>

#define MP(x, y) make_pair(x, y)
#define PB(x) push_back(x)
#define forn(i, n) for(int i = 0; i < n; i++)

#define TASK "a"

typedef long long int64;
typedef long double ld;

int main() {
	freopen(TASK ".in", "rt", stdin);
	freopen(TASK ".out", "wt", stdout);
	int T;
	scanf("%d", &T);
	forn(t, T) {
		printf("Case #%d: ", t + 1);
		int n, k;
		scanf("%d%d", &n, &k);
		
		if ((k % (1 << n)) == ((1 << n)-1))
			printf("ON\n");
		else
			printf("OFF\n");		
	}
	
	return 0;
}

