#include <iostream>
#include <map>
using namespace std;

const int smax = 512;
bool b[smax][smax];
int w[smax][smax];

int main() {
	int nc, ic;
	
	for (cin >> nc, ic = 0; ic < nc; ic++) {
		memset(w, 0, sizeof w);
		
		int m, n, i, j, k, t, wt, it, jt;
		map<int, int> r;
		char s[2] = {0};
		
		cin >> m >> n;
		for (i = 0; i < m; i++) {
			for (j = 0; j < n; j += 4) {
				cin >> s[0];
				sscanf(s, "%1x", &t);
				b[i][j] = t >> 3 & 1;
				b[i][j + 1] = t >> 2 & 1;
				b[i][j + 2] = t >> 1 & 1;
				b[i][j + 3] = t & 1;
			}
		}
		
		for (i = 0; i < m; i++) {
			for (j = n; j--; ) {
				w[i][j] = (j == n - 1 || b[i][j + 1] == b[i][j] ? 1 : w[i][j + 1] + 1);
			}
		}
		
		while (1) {
			t = 0;
			for (i = 0; i < m; i++) {
				for (j = 0; j < n; j++) if (wt = w[i][j]) {
					for (k = 0; i + k < m && b[i + k][j] == (k & 1 ? !b[i][j] : b[i][j]); k++) {
						wt = min(wt, w[i + k][j]);
						if (k >= wt) break;
					}
					if (k > t) t = k, it = i, jt = j;
				}
			}
			if (!t) break;
			r[t]++;
			for (i = 0; i < t; i++) {
				for (j = 0; j < t; j++) w[it + i][jt + j] = 0;
				for (j = 0; j < jt; j++) w[it + i][j] = min(w[it + i][j], jt - j);
			}
		}
		
		cout << "Case #" << ic + 1 << ": " << r.size() << '\n';
		for (map<int, int>::reverse_iterator ir = r.rbegin(); ir != r.rend(); ir++) cout << ir->first << ' ' << ir->second << '\n';
	}
	
	return 0;
}
