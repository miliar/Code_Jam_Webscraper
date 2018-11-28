#include <iostream>
#include <algorithm>

using namespace std;

int N, n;
long long int x[800], y[800];

void read_data () {
	cin >> n;

	for (int i = 0; i < n; ++i) cin >> x[i];
	for (int i = 0; i < n; ++i) cin >> y[i];
}

void solve () {
	sort (&x[0], &x[n]);
	sort (&y[0], &y[n]);

	long long int res = 0;
	for (int i = 0; i < n; ++i)
		res += x[i]*y[n-i-1];

	cout << res << endl;
}

int main () {
	cin >> N;

	for (int t = 0; t < N; ++t) {
		printf ("Case #%d: ", t+1);

		read_data ();
		solve ();
	}

	return 0;
}
