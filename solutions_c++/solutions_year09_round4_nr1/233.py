#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;


int get (string & s) {
	for (int i=(int)s.length()-1; i>=0; --i)
		if (s[i] == '1')
			return i+1;
	return 0;
}

int main() {
	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);

	int ts;
	cin >> ts;
	for (int tt=0; tt<ts; ++tt) {
		int n;
		cin >> n;
		vector<string> a (n);
		for (int i=0; i<n; ++i)
			cin >> a[i];
		int ans = 0;
		for (int i=0; i<n; ++i)
			if (get (a[i]) > i+1) {
				int sel = -1;
				for (int j=i+1; j<n; ++j)
					if (get (a[j]) <= i+1) {
						sel = j;
						break;
					}
				rotate (a.begin()+i, a.begin()+sel, a.begin()+sel+1);
				ans += sel - i;
			}
		printf ("Case #%d: %d\n", tt+1, ans);
	}

}
