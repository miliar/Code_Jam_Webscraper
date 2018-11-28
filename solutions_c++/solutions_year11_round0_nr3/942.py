// Adrian Kügel
#include <stdio.h>
#include <vector>
#include <set>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <map>
#include <assert.h>
#include <limits.h>
#include <complex>
#include <algorithm>
#include <ctype.h>
#include <string>
using namespace std;

typedef set<int> SI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef complex<double> tComp;
typedef pair<short, int> PCI;

int c[1000];

int main() {
	int n, tc;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		scanf("%d", &n);
		int xsum = 0, sum = 0, minval = 1000000000;
		for (int i=0; i<n; ++i) {
			scanf("%d", &c[i]);
			xsum ^= c[i];
			sum += c[i];
			if (c[i] < minval)
				minval = c[i];
		}
		if (xsum)
			puts("NO");
		else
			printf("%d\n", sum - minval);
	}
	return 0;
}
