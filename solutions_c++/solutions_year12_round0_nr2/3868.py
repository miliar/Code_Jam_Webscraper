#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>

using namespace std;

int ti[128];
int p;
int br[128][128];

int best_result (int N, int S)
{
	if (br[N][S] >= 0) return br[N][S];
	
	if (N == 0) return 0;
	
	if (ti[N] == 0) {
		int b = 0;
		
		if (p > 0) {
			b = best_result (N - 1, S);
		}
		else if (p == 0) {
			b = 1 + best_result (N - 1, S);			
		}

		br[N][S] = b;
		return b;
	}
			
	
	int m = ti[N] / 3;
	bool has_sur = false, no_sur = false;
	for (int x = m - 1; x <= m + 2; ++x) 
		for (int y = x; y <= m + 2; ++y)
			for (int z = y; z <= m + 2; ++z) {
				if (x + y + z == ti[N]) {
					if (z - x <= 1) {
						// no surprising
						if (z >= p) {
							no_sur = true;
						}
						
					} else if (S > 0 && z - x == 2) {
						// surprising
						if (z >= p) {
							has_sur = true;
						}
					}
				}
		
			}

	int max_best = 0;
	
	int no_sur_best = best_result (N - 1, S);
	int sur_best;
	
	if (S > 0)
		sur_best = best_result (N - 1, S - 1);
	else
		sur_best = 0;
	
	if (no_sur)
		max_best = 1 + no_sur_best;
	else
		max_best = no_sur_best;
		
	if (has_sur)
		max_best = max (max_best, 1 + sur_best);
	else
		max_best = max (max_best, sur_best);
		
	br[N][S] = max_best;
	
	return max_best;
}

int main (void)
{
	int T, N, S, t;
	
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cin >> N >> S >> p;
		for (int k = 1; k <= N; ++k) {
			cin >> ti[k];
		}
		memset (br, -1, 128 * 128);
		cout << "Case #" << i << ": " << best_result (N, S) << endl;
	}

	return 0;
}