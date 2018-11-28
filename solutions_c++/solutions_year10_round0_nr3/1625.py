#include <iostream>
#include <algorithm>
#include <string.h>
#include <list>
#include <vector>

using namespace std;

int t, r, k, n, m;
long long result, res[1005];
list <int> in;
vector < list <int> > S;

bool operator == (list <int> & a, list <int> & b) {
	list <int>::iterator it1 = a.begin(), it2 = b.begin();
	while (it1 != a.end() && it2 != b.end()) {
		if ((*it1) != (*it2)) return false;
		it1++; it2++;
	}
	return true;
}

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++) {
		// Start: Clean-up
		in.clear();
		S.clear();
		memset(res, 0, sizeof(res));
		result = 0;
		m = 0;
		// End: Clean-up
		scanf("%d%d%d", &r, &k, &n);
		for (int i = 0, a; i < n; i++) {
			scanf("%d", &a);
			in.push_back(a);
		}
		S.push_back(in);
		while (true) {
			int kk = k, l = 0;
			while (kk >= in.front() && l < in.size()) {
				kk -= in.front();
				res[S.size() - 1] += in.front();
				in.push_back(in.front());
				in.pop_front();
				l++;
			}
			bool flag = true;
			for (int i = 0; i < S.size() && flag == true; i++) {
				if (S[i] == in) {
					m = i;
					flag = false;
				}
			}
			if (flag == false) break;
			S.push_back(in);
		}
		for (int i = 0; i < m && i < r; i++) result += res[i]; // Pre-cycle
		r -= m;

		int rs = S.size() - m;
		long long sum = 0;
		for (int i = m; i < S.size(); i++) sum += res[i];
		result += (r / rs) * sum;

		r = (r % rs); // Post-cycle
		for (int i = m; i < m + r; i++) result += res[i];

		printf("Case #%d: %lld\n", cas, result);
	}
	return 0;
}