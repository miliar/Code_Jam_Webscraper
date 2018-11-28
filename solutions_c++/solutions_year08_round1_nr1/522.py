#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char **argv) {
	int nTests;
	scanf("%d", &nTests);
	for (int i = 0; i < nTests; ++i) {
		vector<long long> x, y;
		int d;
		scanf("%d", &d);
		for (int j = 0; j < d; ++j) {
			long long c;
			scanf("%lld", &c);
			x.push_back(c);
		}
		for (int j = 0; j < d; ++j) {
			long long c;
			scanf("%lld", &c);
			y.push_back(c);
		}
		sort(x.begin(), x.end());
		sort(y.begin(), y.end());
		vector<long long>::iterator xit = x.begin();
		vector<long long>::reverse_iterator yit = y.rbegin();
		long long ret = 0;
		while (xit != x.end()) {
			ret += *xit * *yit;
			++xit; ++yit;
		}
		printf("Case #%d: %lld\n", i+1, ret);

	}
}
