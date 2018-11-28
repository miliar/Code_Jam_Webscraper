#include <iostream>
#include <algorithm>
#include <iterator>

using namespace std;

int	a[10001];
int	b[10001];
int	c[10001];

bool
mycmp(int i, int j) {
	return a[i] < a[j];
}

void
init(int n) {
	int	i;
	for (i=0;i<n;i++) c[i] = i;
}

int
get(int n) {
	int	i, j, ans = 0;

	for (i=n-1;i>0;i--) {
		for (j=i-1;j>=0;j--) {
			if (b[c[j]] > b[c[i]]) {
				ans++;
			}
		}
	}

	return ans;
}

int
main(void) {
	int	t, n, i, j;

	cin >> t;

	for (i=1;i<=t;i++) {
		cin >> n;
		for (j=0;j<n;j++) {
			cin >> a[j] >> b[j];
		}
		init(n);
		sort(&c[0], &c[n], mycmp);
		cout << "Case #" << i << ": " << get(n) << endl;
	}
	return 0;
}
