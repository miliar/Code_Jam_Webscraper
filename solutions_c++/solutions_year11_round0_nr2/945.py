// Adrian Kügel
#include <string.h>
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

char comb[26][26], opp[26][26];
char line[200];

int main() {
	int tc;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		int c, d;
		scanf("%d", &c);
		memset(comb, 0, sizeof(comb));
		memset(opp, 0, sizeof(opp));
		char s[5];
		for (int i=0; i<c; ++i) {
			scanf("%s", s);
			comb[s[0]-'A'][s[1]-'A'] = s[2];
			comb[s[1]-'A'][s[0]-'A'] = s[2];
		}
		scanf("%d", &d);
		for (int i=0; i<d; ++i) {
			scanf("%s", s);
			opp[s[0]-'A'][s[1]-'A'] = 1;
			opp[s[1]-'A'][s[0]-'A'] = 1;
		}
		int n;
		scanf("%d ", &n);
		int l = 0;
		for (int i=0; i<n; ++i) {
			scanf("%c", &line[l]);
			while (l && comb[line[l]-'A'][line[l-1]-'A']) {
				line[l-1] = comb[line[l]-'A'][line[l-1]-'A'];
				--l;
			}
			for (int i=0; i<l; ++i)
				if (opp[line[i]-'A'][line[l]-'A'])
					l = -1;
			++l;
		}
		printf("[");
		for (int i=0; i<l; ++i) {
			if (i) printf(", ");
			printf("%c", line[i]);
		}
		puts("]");
	}
	return 0;
}
