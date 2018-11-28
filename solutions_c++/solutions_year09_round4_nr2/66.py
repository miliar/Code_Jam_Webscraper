#include <iostream>
#include <string>
#include <set>

using namespace std;

const int nmax = 50;
const bool deb = false;

int d[nmax][nmax][nmax];

struct state {
	int r, c, d;
	
	bool operator <(const state &s) const {return ::d[r][c][d] < ::d[s.r][s.c][s.d] || ::d[r][c][d] == ::d[s.r][s.c][s.d] && (r < s.r || r == s.r && (c < s.c || c == s.c && d < s.d));}
};

set<state> q;

void upd(state s, int d) {
	if (::d[s.r][s.c][s.d] > d) {
		q.erase(s);
		::d[s.r][s.c][s.d] = d;
		q.insert(s);
	}
}

int main() {
	int nt, it;
	
	cin >> nt;
	for (it = 1; it <= nt; it++) {
		int r, c, f, i, j, k, i0, i1;
		string a[50];
		state s = {0}, s1;


		cin >> r >> c >> f;
		for (i = 0; i < r; i++) cin >> a[i];
		
		memset(d, 127, sizeof d);
		d[0][0][0] = 0;
		q.clear();
		q.insert(s);
		while (q.size()) {
			s = *q.begin();
			q.erase(q.begin());
			if (deb) cout << s.r << ' ' << s.c << ' ' << s.d << '\n';
			if (s.r == r - 1) break;
			// izvēlamies lēkt
			for (i = s.c; i >= 0 && (a[s.r][i] == '.' || i >= s.d || i == s.c); i--) if (a[s.r + 1][i] == '.') {
				for (j = 1; s.r + j < r && a[s.r + j][i] == '.'; j++) ;
				if (--j <= f) {
					s1.r = s.r + j;
					s1.c = s1.d = i;
					upd(s1, d[s.r][s.c][s.d]);
				}
				break;
			}
			for (i = s.c; i < c && (a[s.r][i] == '.' || i <= s.d || i == s.c); i++) if (a[s.r + 1][i] == '.') {
				for (j = 1; s.r + j < r && a[s.r + j][i] == '.'; j++) ;
//				cout << j << '\n';
				if (--j <= f) {
					s1.r = s.r + j;
					s1.c = s1.d = i;
					upd(s1, d[s.r][s.c][s.d]);
				}
				break;
			}
			// izvēlamies rakt
			for (i = s.c; i >= 0 && (a[s.r][i] == '.' || i >= s.d || i == s.c) && a[s.r + 1][i] != '.'; i--) ; i0 = i + 1;
			for (i = s.c; i < c && (a[s.r][i] == '.' || i <= s.d || i == s.c) && a[s.r + 1][i] != '.'; i++) ; i1 = i - 1;
			if (deb) cout << i0 << '_' << i1 << " (" << s.r << ' ' << s.c << ' ' << s.d << ") " << a[s.r] << "\n";
			if (i0 < i1) {
				for (i = i0; i <= i1; i++) for (j = i; j <= i1; j++) {
					// krist kreisajā galā
					if (i > i0) {
						for (k = 2; s.r + k < r && a[s.r + k][i] == '.'; k++) ;
						if (--k <= f) {
							s1.r = s.r + k;
							s1.c = i;
							s1.d = (k == 1 ? j : i);
							upd(s1, d[s.r][s.c][s.d] + j - i + 1);
						}
					}
					// labajā
					if (j < i1) {
						for (k = 2; s.r + k < r && a[s.r + k][j] == '.'; k++) ;
						if (--k <= f) {
							s1.r = s.r + k;
							s1.c = j;
							s1.d = (k == 1 ? i : j);
							upd(s1, d[s.r][s.c][s.d] + j - i + 1);
						}
					}
				}
			}
		}
		
		cout << "Case #" << it << ": ";
		if (s.r == r - 1) cout << "Yes " << d[s.r][s.c][s.d]; else cout << "No";
		cout << '\n';
	}
	
	return 0;
}
