#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <iomanip>
#include <utility>
using namespace std;

typedef long double ld;
const int nmax = 1000;
ld x[nmax], y[nmax];
#define sqr(a) ((a) * (a))
typedef pair<int, int> pi;
pi r[nmax];

int main() {
	int nt, it;

	cin >> nt;
	for (it = 1; it <= nt; it++) {
		int N, W, L;
		int i, j;
		
		cin >> N >> W >> L;

		for (i = 0; i < N; i++) {
			cin >> r[i].first;
			r[i].second = i;
		}
		sort(r, r + N);

		srand(0xDACE);
		for (i = N; i--; ) {
// 			x[i] = floor(ld(rand()) / RAND_MAX * W * 1000) / 1000;
// 			y[i] = floor(ld(rand()) / RAND_MAX * L * 1000) / 1000;
			x[i] = floor(ld(rand()) / RAND_MAX * W);
			y[i] = floor(ld(rand()) / RAND_MAX * L);
			for (j = i + 1; j < N; j++) {
// 				if (sqr(x[i] - x[j]) + sqr(y[i] - y[j]) < sqr(r[i].first + r[j].first) + 1E-3) {
				if (hypotl(x[i] - x[j], y[i] - y[j]) < r[i].first + r[j].first + 1E-3) {
					cerr << "/" << i;
					i++;
					break;
				}
			}
		}

// 		cout << "Case #" << it << ":" << setprecision(3) << fixed;
		cout << "Case #" << it << ":" << setprecision(0) << fixed;
		for (i = 0; i < N; i++) for (j = 0; j < N; j++) if (r[j].second == i) cout << ' ' << x[j] << ' ' << y[j];
		cout << endl;
		cerr << endl;
	}
	
	return 0;
}
