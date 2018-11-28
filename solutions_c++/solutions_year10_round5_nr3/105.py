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

#define MAXN 200

int p[MAXN], c[MAXN];

int main() {
	int tc;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		int n;
		scanf("%d", &n);
		map<int, int> C, C2;
		int ftotal = 0;
		for (int i=0; i<n; ++i) {
			scanf("%d %d", &p[i], &c[i]);
			ftotal += c[i];
			C[p[i]] = c[i];
		}
		int steps = 0;
		while(true) {
			int maxv = 0;
			int total = 0;
			for (map<int, int>::iterator it=C.begin(); it!=C.end(); ++it) {
				maxv = max(it->second, maxv);
				total += it->second;
			}
			assert(total == ftotal);
			if (maxv <= 1)
				break;
			for (map<int, int>::iterator it=C.begin(); it!=C.end(); ++it)
				if (it->second >= 2) {
					it->second -= 2;
					C[it->first + 1] += 1;
					C[it->first - 1] += 1;
					int last = it->first;
					++steps;
					for (map<int, int>::iterator it2=C.find(it->first); true; ) {
						--it2;
						assert(it2->first + 1 == last);
						if (it2->second <= 1)
							break;
						last = it2->first;
						++steps;
						it2->second -= 2;
						C[it2->first + 1] += 1;
						C[it2->first-1] += 1;
						it2 = C.find(it2->first);
					}
					break;
				}
		}
		printf("%d\n", steps);
	}
	return 0;
}
