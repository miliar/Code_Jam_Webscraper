#include <string>
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <fstream>
#include <queue>
#include <cassert>

using namespace std;

int C;
const int MAXN = 60;
long long X[MAXN];
long long V[MAXN];

int main(void) 
{
	scanf("%d", &C);

	for (int t = 1; t <= C; ++t) {

		int N, K, B, T;
		scanf("%d %d %d %d", &N, &K, &B, &T);

		for (int i = 0; i < N; ++i) {
			scanf("%lld", X + i);
		}
		for (int i = 0; i < N; ++i) {
			scanf("%lld", V + i);
		}

		int ret = 0;

		for (int i = N - 1; i >= 0; --i) {
			if (K == 0) break;
			long long dist = B - X[i];
			if (dist > V[i] * T) {
				ret += K;
			} else {
				K--;
			}
		}

		printf("Case #%d: ", t);

		if (K > 0) {
			puts("IMPOSSIBLE");
		} else {
			printf("%d\n", ret);
		}
	}

	return 0;
}