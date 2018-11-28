#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

int n;

string d[5050];
int was[5050][16];

vector <char> a[5005];

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	int L, D, N;
	cin >> L >> D >> N;
	for (int i = 0; i < D; ++i) {
		cin >> d[i];
	}
	for (int i = 0; i < N; ++i) {
		int sz = 0;
		string s;
		cin >> s;
		int j = 0;
		long long ans = 0;
		while (j < s.size()) {
			if (s[j] == '(') {
				++j;
				while (s[j] != ')') {
					a[sz].push_back(s[j]);
					++j;
				}
				sz++;
			} else {
				a[sz++].push_back(s[j]);
			}
			++j;
		}
/*		for (int j = 0; j < sz; ++j) {
			for (int k = 0; k < a[j].size(); ++k)
				printf("%c ",a[j][k]);
			printf("\n");
		}
*/
		ans = 0;

		memset(was, 0, sizeof(was));
		for (int j = 0; j < L; ++j) {
			for (int uk = 0; uk < a[j].size(); ++uk)
				for (int k = 0; k < D; ++k)
					if (d[k][j] == a[j][uk]) was[k][j]++;
		}

		for (int j = 0; j < D; ++j) {
			long long res = 1;
			for (int k = 0; k < L; ++k) {
				int kol = 0;
				if (was[j][k] > 0) kol = was[j][k];
				res *= kol;
			}
			ans += res;
		}

		printf("Case #%d: %I64d\n", i + 1, ans);

//		printf("-----------\n");
		for (int j = 0; j < sz; ++j) {
			a[j].clear();
		}
//		return 0;

	}



	return 0;
}
