#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <iostream>

using namespace std;

#define Size(a) ((int)a.size())
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ntests;
	scanf("%d", &ntests);
	for (int itest = 1; itest <= ntests; itest++) {
		printf("Case #%d: ", itest);
		int r, k, n;
		cin >> r >> k >> n;
		vector<int> a(n, 0);
		vector<int> was(n, 0);
		vector<long long> psg(n, 0);
		for (int i = 0; i < n; i++) {
			scanf("%d", &a[i]);
		}
		long long res = 0;
		bool skip = true;
		for (int i = 1, p = 0; i <= r;) {
			if (skip && was[p]) {
				int k = (r - i) / (i - was[p]);
				res +=  (res - psg[p]) * k;
				i += k * (i - was[p]);
				skip = false;
				continue;
			}
			was[p] = i;
			psg[p] = res;
			int cpsg = 0, j = 0;
			for (j = 0; j < n; j++) {
				if (cpsg + a[(p + j) % n] <= k) {
					cpsg += a[(p + j) % n];
				} else {
					break;
				}
			}
			res += cpsg;
			p = (p + j) % n;
			i++;
		}
		cout << res << endl;
	}
	return 0;
}