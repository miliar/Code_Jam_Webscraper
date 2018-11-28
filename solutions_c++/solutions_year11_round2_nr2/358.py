// ==========================================================================
//  B.cpp
// ==========================================================================

#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <functional>
#include <numeric>
#include <iterator>
#include <algorithm>

using namespace std;

#if defined _OJ_PROJECT
_BEGIN_CONTEST_PROBLEM(B, "B-large.in")
#endif // _OJ_PROJECT

#define infinite_loop	for (;;)

int points[1000000];

inline bool f(
	long long time, int D, int N
	) {
		long long prev = points[0] - time;
		for (int i = 1; i < N; ++i) {
			long long t = max(points[i] - time, prev + D);
			if (t - points[i] > time) return false;
			prev = t;
		}
		return true;
	}

int main(
	) {
		int T;
		scanf("%d", &T);

		for (int _T = 0; _T < T; ++_T) {
			int D, C;
			scanf("%d %d", &C, &D);

			int N = 0;
			for (int i = 0, P, V; i < C; ++i) {
				scanf("%d %d", &P, &V);
				for (int j = 0; j < V; ++j) points[N++] = P * 2;
			}

			sort(points, points + N);

			long long low = 0, high = 1LL << 58;
			while (low < high) {
				long long mid = (high + low) >> 1;

				if (f(mid, D * 2, N))
					high = mid;
				else
					low = mid + 1;
			}

			printf("Case #%d: %.1lf\n", _T + 1, low * 0.5);
		}

		return 0;
	}

#if defined _OJ_PROJECT
_END_PROBLEM
#endif // _OJ_PROJECT

// ==========================================================================
//  End of file.
// ==========================================================================
