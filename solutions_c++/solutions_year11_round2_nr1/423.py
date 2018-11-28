#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

#define X first
#define Y second

typedef long long llong;
typedef long double ldouble;

void solve()
{
	int n;
	cin >> n;
	vector<string> a(n);
	for (int i = 0; i < n; ++i)
		cin >> a[i];
	vector<ldouble> rpi(n);
	vector<ldouble> owp(n);
	for (int i = 0; i < n; ++i){
		ldouble pl = 0, win = 0;
		for (int j = 0; j < n; ++j)
			if (a[i][j] != '.'){
				++pl;
				if (a[i][j] == '1')
					++win;
			}
		rpi[i] = win / pl * 0.25;
	}

	for (int i = 0; i < n; ++i){
		int cnt = 0;
		for (int j = 0; j < n; ++j)
			if (a[i][j] != '.'){
				++cnt;
				ldouble pl = 0, win = 0;
				for (int k = 0; k < n; ++k)
					if (k != i && a[j][k] != '.'){
						++pl;
						if (a[j][k] == '1')
							++win;
					}
				owp[i] += win / pl;
			}
		owp[i] /= cnt;
		rpi[i] += 0.5 * owp[i];
	}

	for (int i = 0; i < n; ++i){
		ldouble sum = 0;
		int cnt = 0;
		for (int j = 0; j < n; ++j)
			if (a[i][j] != '.'){
				sum += owp[j];
				cnt++;
			}
		rpi[i] += sum / cnt * 0.25;
	}
	cout.precision(12);
	for (int i = 0; i < n; ++i)
		cout << rpi[i] << "\n";
}

int main()
{
#if 1
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test){
		printf("Case #%d:\n", test);
		solve();
	}

	return 0;
}
