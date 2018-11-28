// ==========================================================================
//  A.cpp
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
_BEGIN_CONTEST_PROBLEM(A, "A-large.in")
#endif // _OJ_PROJECT

#define infinite_loop	for (;;)

char grid[100][101];

int main(
	) {
		int T;
		scanf("%d", &T);

		for (int _T = 0; _T < T; ++_T) {
			int N;
			scanf("%d", &N);

			for (int i = 0; i < N; ++i) scanf("%s", &grid[i]);

			double WP[100], OWP[100], OOWP[100];

			for (int i = 0; i < N; ++i) {
				int pWP = 0, qWP = 0;
				for (int j = 0; j < N; ++j)
					if (grid[i][j] == '1')
						++pWP, ++qWP;
					else if (grid[i][j] == '0')
						++qWP;
				WP[i] = 1. * pWP / qWP;

				double pOWP = 0;
				int qOWP = 0;
				for (int j = 0; j < N; ++j)
					if (grid[i][j] == '1' || grid[i][j] == '0') {
						int pTWP = 0, qTWP = 0;
						for (int k = 0; k < N; ++k)
							if (k != i)
								if (grid[j][k] == '1')
									++pTWP, ++qTWP;
								else if (grid[j][k] == '0')
									++qTWP;
						pOWP += 1. * pTWP / qTWP, ++qOWP;
					}

				OWP[i] = pOWP / qOWP;
			}

			for (int i = 0; i < N; ++i) {
				double pOOWP = 0;
				int qOOWP = 0;
				for (int j = 0; j < N; ++j)
					if (grid[i][j] == '1' || grid[i][j] == '0')
						pOOWP += OWP[j], ++qOOWP;
				OOWP[i] = 1. * pOOWP / qOOWP;
			}

			printf("Case #%d:\n", _T + 1);
			for (int i = 0; i < N; ++i)
				printf("%.10lf\n", 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]);
		}

		return 0;
	}

#if defined _OJ_PROJECT
_END_PROBLEM
#endif // _OJ_PROJECT

// ==========================================================================
//  End of file.
// ==========================================================================
