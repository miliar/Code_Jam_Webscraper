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

int a[1000];

// f(x) = 1 + 1/2*2 + 1/3*f(x)
// f(x) = 2 * 3/2 = 3

int main() {
	int tc;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		int n;
		scanf("%d", &n);
		for (int i=0; i<n; ++i) {
			scanf("%d", &a[i]);
			--a[i];
		}
		int cnt = 0;
		for (int i=0; i<n; ++i) {
			int len = 0;
			while(a[i] != i) {
				swap(a[i], a[a[i]]);
				++len;
			}
			if (len)
				cnt += len+1;
		}
		printf("%d.000000\n", cnt);
	}
	return 0;
}
