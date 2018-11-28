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

char s[100000], s2[100000];
int p[100];

int main() {
	int tc;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		int k;
		scanf("%d", &k);
		gets(s);
		gets(s);
		int l = strlen(s);
		assert(l % k == 0);
		for (int i=0; i<k; ++i)
			p[i] = i;
		int best = l;
		do {
			for (int i=0; i<l; i+=k) {
				for (int j=0; j<k; ++j)
					s2[i+j] = s[i+p[j]];
			}
		//	puts(s2);
			char prev = -1;
			int cnt = 0;
			for (int i=0; i<l; ++i) {
				if (s2[i] != prev) {
					prev = s2[i];
					++cnt;
				}
			}
			best = min(best, cnt);
		}while(next_permutation(p, p+k));
		printf("%d\n", best);
	}
	return 0;
}
