#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;


int main() {
	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);

	int ts;
	cin >> ts;
	for (int tt=0; tt<ts; ++tt) {
		printf ("Case #%d: ", tt+1);

		int n;
		cin >> n;
		vector<int> a (n);
		for (int i=0; i<n; ++i)
			scanf ("%d", &a[i]);

		int x = 0;
		for (int i=0; i<n; ++i)
			x ^= a[i];
		if (x) {
			puts ("NO");
			continue;
		}

		sort (a.begin(), a.end());
		int s = 0;
		for (int i=1; i<n; ++i)
			s += a[i];

		printf ("%d\n", s);

	}

}