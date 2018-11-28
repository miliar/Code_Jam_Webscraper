#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	int nt, it;
	
	cin >> nt;
	for (it = 1; it <= nt; it++) {
		int n, i, j, a[40], r = 0;
		string t;

		cin >> n;
		for (i = 0; i < n; i++) {
			cin >> t;
			a[i] = -1;
			for (j = 0; j < n; j++) if (t[j] == '1') a[i] = j;
//			cout << a[i] << '\n';
		}
		for (i = 0; i < n; i++) {
			for (j = i; j < n; j++) if (a[j] <= i) break;
			for ( ; j > i; j--) swap(a[j], a[j - 1]), r++;
		}
		
		cout << "Case #" << it << ": " << r << '\n';
	}
	
	return 0;
}
