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

const int MAXN = 1024;

int r, k, n;
int g[MAXN], st[MAXN];
int64 pt[MAXN];

inline int nxt(int i) {
	return (i+1) % n;
}
             
int main() {
	#ifdef LOCAL
		freopen("input.txt", "rt", stdin);
		freopen("output.txt", "wt", stdout);
	#endif

	scanf("%d", &T);

	for (int cs = 1; cs <= T; cs++) {
		printf("Case #%d: ", cs);

		scanf("%d %d %d", &r, &k, &n);
		for (int i = 0; i < n; i++) scanf("%d", &g[i]);

		int fstpos = 0;
		int counter = 0;

		do {
			int sum = 0; 
			int leadpos = fstpos;

			do {
				sum += g[fstpos];
				fstpos = nxt(fstpos);
			} while (sum + g[fstpos] <= k && fstpos != leadpos);
			
			counter++;
			st[counter] = sum;
		} while (fstpos != 0);

		memset(pt, 0, sizeof(pt));

		pt[0] = 0;
		for (int i = 1; i <= counter; i++) {
			pt[i] = pt[i-1] + st[i];
		}

		int64 ans = pt[counter] * (r / counter) + pt[r % counter];
        
        printf("%I64d", ans);

		printf("\n");
	}

	return 0;
}
