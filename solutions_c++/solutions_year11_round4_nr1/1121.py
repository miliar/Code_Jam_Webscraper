#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;

const int nmax = 1000;
struct way {
	int b, e, w;
	bool operator <(const way &w2) const {return w < w2.w;}
} w[nmax];
typedef long double ld;

int main() {
	int nt, it;
	
	cin >> nt;
	for (it = 1; it <= nt; it++) {
		int X, S, R, N, i;
		ld l, t, r = 0;
		
		cin >> X >> S >> R >> t >> N;
		l = X;
		for (i = 0; i < N; i++) {
			cin >> w[i].b >> w[i].e >> w[i].w;
			l -= w[i].e - w[i].b;
		}
		sort(w, w + N);
		
		if (l / R <= t) {
			r += l / R;
			t -= l / R;
		} else {
			r += t + (l - t * R) / S;
			t = 0;
		}
		for (i = 0; i < N; i++) {
			l = w[i].e - w[i].b;
			if (l / (w[i].w + R) <= t) {
				r += l / (w[i].w + R);
				t -= l / (w[i].w + R);
			} else {
				r += t + (l - t * (w[i].w + R)) / (w[i].w + S);
				t = 0;
			}
		}
		
		cout << "Case #" << it << ": " << setprecision(9) << fixed << r << '\n';
	}
	
	return 0;
}
