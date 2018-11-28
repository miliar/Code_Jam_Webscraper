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

int last_one[40];

int main() {
	int tc, n;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		scanf("%d", &n);
		char row[100];
		for (int i=0; i<n; ++i) {
			scanf("%s", row);
			last_one[i] = -1;
			for (int j=0; j<n; ++j) {
				if (row[j] == '1')
					last_one[i] = j;
			}
		}
		int cnt = 0;
		for (int i=0; i<n; ++i) {
			for (int j=i; j<n; ++j)
				if (last_one[j] <= i) {
					while(j > i) {
						swap(last_one[j], last_one[j-1]);
						--j;
						++cnt;
					}
					break;
				}
		}
		printf("%d\n", cnt);
	}
	return 0;
}
