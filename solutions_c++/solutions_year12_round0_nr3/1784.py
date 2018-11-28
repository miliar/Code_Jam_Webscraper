
#include <cstdio>
#include <vector>
#include <cassert>
#include <set>
#include <algorithm>
using namespace std;

int main() {
	int testsCount;
	scanf("%d", &testsCount);
	for (int test = 0; test < testsCount; ++test) {
		int A, B;
		scanf("%d %d", &A, &B);
		int res = 0;
		for (int i = A; i <= B; ++i) {
			vector<int> d;
			int x = i;
			while (x > 0) {
				d.push_back(x % 10);
				x /= 10;
			}
			set<int> reachables;
			reverse(d.begin(), d.end());
			assert(d[0] != 0);
			int len = (int)d.size();
			for (int j = 0; j < len; ++j) d.push_back(d[j]);
			for (int j = 1; j < len; ++j) if (d[j] > 0) {
				int rev = 0;
				for (int k = 0; k < len; ++k)
					rev = rev * 10 + d[j + k];
				if (i < rev && rev >= A && rev <= B) {
					reachables.insert(rev);
				}
			}
			res += (int)reachables.size();
		}
		printf("Case #%d: %d\n", test + 1, res);
	}
	return 0;
}
