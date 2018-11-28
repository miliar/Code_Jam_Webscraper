#define _USE_MATH_DEFINES

#include <iostream>
#include <set>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <iterator>
#include <queue>
#include <ctime>

using namespace std;

int main(int argc, char* argv[])
{
	freopen("alignment.in" , "r", stdin);
	freopen("alignment.out" , "w", stdout);

	int t;
	cin >> t;
	for (int test = 0; test < t; ++test) {
		int n;
		cin >> n;
		string a[100];
		for (int i = 0; i < n; ++i)
			cin >> a[i];
		int w[100], g[100];
		double wp[100], owp[100], oowp[100];
		memset(wp, 0, sizeof(wp));
		memset(owp, 0, sizeof(owp));
		memset(oowp, 0, sizeof(oowp));

		memset(w, 0, sizeof(w));
		memset(g, 0, sizeof(g));
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
				if (a[i][j] != '.') {
					++g[i];
					if (a[i][j] == '1')
						++w[i];
				}
		for (int i = 0; i < n; ++i)
			wp[i] = w[i] / (double) g[i];

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j)
				if (a[i][j] != '.')
					owp[i] += (w[j] - (a[j][i] - '0')) / double(g[j] - 1);
			owp[i] /= g[i];
		}

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j)
				if (a[i][j] != '.')
					oowp[i] += owp[j];
			oowp[i] /= g[i];
		}

		cout << "Case #" << test + 1<< ":\n";
		cout.setf(ios::fixed);
		cout.precision(10);
		for (int i = 0; i < n; ++i)
			cout << 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] << '\n';
	}

	return 0;
}
