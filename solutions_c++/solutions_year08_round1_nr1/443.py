#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

vector<long long> x, y;

int main (void) {

	int i, k;
	int casos;
	int n, a;

	scanf("%d", &casos);
	for (k=1; k<=casos; ++k) {

		scanf("%d", &n);
		x.clear();
		y.clear();

		for (i=0; i<n; ++i) {
			scanf("%d", &a);
			x.push_back(a);
		}
		for (i=0; i<n; ++i) {
			scanf("%d", &a);
			y.push_back(a);
		}

		sort(x.begin(), x.end());
		sort(y.begin(), y.end());

		long long sum=0;
		for (i=0; i<n; ++i) {
			sum += x[i]*y[n-i-1];
		}
		printf("Case #%d: %lld\n", k, sum);
	}

	return 0;
}
