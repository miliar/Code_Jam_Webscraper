#include <iostream>

using namespace std;

int main() {
	int tn;
	cin >> tn;
	for(int ti = 0; ti < tn;) {
		int n, a, b, c, d, m;
		cin >> n >> a >> b >> c >> d;
		long long *x = new long long[n], *y = new long long[n];
		cin >> x[0] >> y[0] >> m;
		for(int i = 1; i < n; i++)
			x[i] = (a * x[i - 1] + b) % m, y[i] = (c * y[i - 1] + d) % m;
		int r = 0;
		for(int i = 0; i < n; i++)
			for(int j = i + 1; j < n; j++)
				for(int k = j + 1; k < n; k++)
					if(!((x[i] + x[j] + x[k]) % 3 || (y[i] + y[j] + y[k]) % 3)) r++;
		cout << "Case #" << ++ti << ": " << r << endl;
	}
	return 0;
}
