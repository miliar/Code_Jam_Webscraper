#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdlib>

using namespace std;

#define fn(n, i)		for(int i = 0; i < (n); ++i)
#define INF		0x3f3f3f3f

int malted[128], unmalted[128];

int main() {
	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);

	int C, n, m, t, x, y;
	cin >> C;
	fn(C, test) {
		cin >> n >> m;
		fn(m , i) {
			cin >> t;
			malted[i] = 0;
			unmalted[i] = 0;
			fn(t, j) {
				cin >> x >> y;
				if (y)
					malted[i] |= 1 << (x-1);
				else
					unmalted[i] |= 1 << (x-1);
			}
		}
		int best = INF, res, w, tmp;
		fn(1 << n, shakes) {
			tmp = shakes;
			for (w = 0; tmp; tmp &= tmp-1) ++w;
			bool ok = true;
			fn(m, i) {
				if((malted[i] & shakes) == 0 && (unmalted[i] & ~shakes) == 0) {
					ok = false;
					break;
				}
			}
			if (ok && w < best) {
				best = w;
				res = shakes;
			}
		}
		cout << "Case #" << test+1 << ": ";
		if (best == INF) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			fn(n, i) {
				cout << ((1 << i) & res ? "1 " : "0 ");
			}
			cout << endl;
		}
	}

	return 0;
}