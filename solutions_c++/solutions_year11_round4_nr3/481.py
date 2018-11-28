#include <iostream>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <string>
#include <cstring>
#include <vector>
#include <map>

using namespace std;

//#define DBG


string spam;
vector <int> a;
long long st[10000], fn[10000], sp[10000];

int main() {
#ifdef DBG
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int j = 0; j < t; ++j) {
		long long n;
		cin >> n;
		vector <long long> a;
		a.clear();
		int mx = 1;
		for (int i = 2; i <= n; ++i) {
			int f = true;
			for (int q = 2; q * q <= i; ++q) {
				if (i % q == 0) {
					f = false;
				}
			}
			if (f) {
				mx++;
				int tt = i;
				while (tt * i <= n) {
					mx++;
					tt *= i;
				}
				a.push_back(tt);
			}
		}
		sort(a.begin(), a.end());
		int mm = 0;
		if (a.size() == 0) {
			mm = 1;
		} else {
			int rr = a.size() - 1;
			long long gg;
			while (rr >= 0) {
				gg = a[rr];
				--rr;
				while (rr >= 0 && gg * a[rr] <= n) {
					gg *= a[rr];
					--rr;
				}
				mm++;
			}
		}
		cout << "Case #" << j + 1 << ": " << mx - mm << endl;
	}
	return 0;
}