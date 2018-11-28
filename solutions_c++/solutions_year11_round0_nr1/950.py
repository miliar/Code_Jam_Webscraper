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


int main() {
	int pos, n, tc;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		scanf("%d", &n);
		VI p[2], next;
		char which;
		for (int i=0; i<n; ++i) {
			scanf(" %c %d", &which, &pos);
			if (which == 'O') {
				p[0].push_back(pos);
				next.push_back(0);
			}
			else {
				p[1].push_back(pos);
				next.push_back(1);
			}
		}
		reverse(p[0].begin(), p[0].end());
		reverse(p[1].begin(), p[1].end());
		int pos[2] = {1,1};
		int res = 0;
		for (int i=0; i<(int)next.size(); ++i) {
			int steps = abs(p[next[i]].back()-pos[next[i]])+1;
			res += steps;
			pos[next[i]] = p[next[i]].back();
			p[next[i]].pop_back();
			if (!p[!next[i]].empty()) {
				if (abs(p[!next[i]].back()-pos[!next[i]]) <= steps)
					pos[!next[i]] = p[!next[i]].back();
				else {
					int sgn = (pos[!next[i]] >= p[!next[i]].back()? -1 : 1);
					pos[!next[i]] += sgn * steps;
				}
			}
		}
		printf("%d\n", res);
	}
	return 0;
}
