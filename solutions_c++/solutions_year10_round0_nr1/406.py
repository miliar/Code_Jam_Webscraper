#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdio>
using namespace std;

/* PREWRITTEN CODE */

#define ALL(x) x.begin(),x.end()
#define PB push_back


#define FOR(i,p,k) for (int i=p; i<k; i++)
#define REP(i,n) for (int i=0; i<n; i++)
#define SIZE(x) (int)x.size()
/* COMPETITION CODE */

int main() {
	int T, N, K;
	scanf("%d", &T);
	REP (i, T) {
		scanf("%d %d", &N, &K);
		printf("Case #%d: O", i+1);
		if ((K + 1) % (1 << N)) {
			printf("FF\n");
		} else printf("N\n");
	}
	return 0;
}
