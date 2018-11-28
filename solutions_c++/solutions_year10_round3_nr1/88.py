#include <iostream>
#include <vector>

using namespace std;


int main() {
	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);

	int ts;
	cin >> ts;
	for (int tt=1; tt<=ts; ++tt) {

		int n;
		cin >> n;
		vector < pair<int,int> > a (n);
		for (int i=0; i<n; ++i)
			scanf ("%d%d", &a[i].first, &a[i].second);

		int ans = 0;
		for (int i=0; i<n; ++i)
			for (int j=0; j<n; ++j)
				if (a[i].first < a[j].first && a[i].second > a[j].second)
					++ans;

		printf ("Case #%d: %d\n", tt, ans);
	}


}

