#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;


string p = "welcome to code jam";

string s;
int d[501][20];

int main() {
	freopen ("C.in", "rt", stdin);
	freopen ("C.out", "wt", stdout);

	int ts;
	cin >> ts;
	for (int t=0; t<ts; ++t) {
		if (!t)
			getline (cin, s);
		getline (cin, s);

		int ans = 0;
		for (int i=0; i<(int)s.length(); ++i) {
			for (int j=1; j<=19; ++j) {
				d[i][j] = 0;
				if (s[i] == p[j-1]) {
					for (int p=0; p<i; ++p)
						d[i][j] = (d[i][j] + d[p][j-1]) % 10000;
					if (j == 1)
						d[i][j] = (d[i][j] + 1) % 10000;
				}
			}
			ans = (ans + d[i][19]) % 10000;
		}
		printf ("Case #%d: %04d\n", t+1, ans);
	}

}