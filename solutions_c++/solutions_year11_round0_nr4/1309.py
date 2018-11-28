#include <iostream>
using namespace std;

double pow(double x, int m)
{
	double w = 1, a = x;
	while (m) {
		if (m&1) w *= a;
		a *= a; m >>= 1;
	}
	return w;
}

int main()
{
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);

	double f[1010]; int a[1000], n, test;
	f[1] = 0;
	for (int i = 2; i < 1001; ++i) {
		f[i] = 1;
		for (int j = 2; j < i; ++j) {
			int k = i / j;
			f[i] += f[j] / j;
		}
		f[i] /= i - 1.0;
		f[i] *= i;
	}
	//for (int i = 1; i < 101; ++i)
		//cout << f[i] << endl;
	cin >> test;
	for (int te = 0; te < test; ++te) {
		cin >> n;
		for (int i = 0; i < n; ++i) cin >> a[i];
		double ans = 0;
		for (int i = 0; i < n; ++i)
			if (a[i]) {
				int k = 0;
				for (int j = i; a[j]; ++k) {
					int t = j; j = a[j] - 1; a[t] = 0;
				}
				ans += f[k];
			}
		cout << "Case #" << te + 1 << ": " << ans << endl;
	}
	return 0;
}

