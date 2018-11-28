#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <cfloat>
#include <cctype>
#include <algorithm>
#include <sstream>
#include <bitset>

#define REP(i,a) for(i=0;i<a;++i)
#define FOR(i,a,b) for(i=a;i<=b;++i)
#define all(x) (x).begin(),(x).end()
#define pb(x) push_back(x)
#define sz(x) (int)(x).size()
using namespace std;

void main() {
	int T;
	int N, K;
	int i, j;

	scanf("%d", &T);

	REP(i, T) {
		scanf("%d %d", &N, &K);

		++K;

		if (K % 2 != 0) {
			printf("Case #%d: OFF\n", i + 1);
			continue;
		}

		int r = 0;

		while (K % 2 == 0) {
			K /= 2;
			++r;
		}

		if (r >= N) {
			printf("Case #%d: ON\n", i + 1);
		} else {
			printf("Case #%d: OFF\n", i + 1);
		}
	}
}