#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;


int main() {
	freopen ("A.in", "rt", stdin);
	freopen ("A.out", "wt", stdout);

	int l, d, n;
	cin >> l >> d >> n;
	vector<string> w (d);
	for (int i=0; i<d; ++i)
		cin >> w[i];
	for (int i=0; i<n; ++i) {
		vector < vector<bool> > a (l, vector<bool> (26));
		string p;
		cin >> p;
		bool open = false;
		for (int j=0, pos=0; j<(int)p.length(); ++j)
			if (p[j] == ')')
				++pos,  open = false;
			else if (p[j] == '(')
				open = true;
			else if (p[j] >= 'a' && p[j] <= 'z') {
				a[pos][p[j]-'a'] = true;
				if (!open)  ++pos;
			}
		int ans = 0;
		for (int j=0; j<d; ++j) {
			bool ok = true;
			for (int k=0; k<l && ok; ++k)
				ok &= a[k][w[j][k]-'a'];
			ans += ok;
		}
		printf ("Case #%d: %d\n", i+1, ans);
	}

}