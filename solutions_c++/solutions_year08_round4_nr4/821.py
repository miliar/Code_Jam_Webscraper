#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <math.h>

#include <vector>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;

#define abs(x) ((x)<0?(-(x)):(x))
#define sqr(x) ((x)*(x))
#define FOR(i,n) for (int i = 0; i < (int) (n); i++)
#define REP(i,v) for (unsigned i = 0; i < v.size(); i++)
#define RL(i,s) for (unsigned i = 0; i < s.lengt(); i++)

char s[60000];
char ns[60000];

int main(void)
{
	freopen("d.in", "rt", stdin);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: ", tc);
		int perm[200];
		int k;
		scanf("%d", &k);
		scanf("%s", s);
		int l = (int) strlen(s);
		ns[l] = 0;
		FOR(i,k) perm[i] = i;
		int minc = 99999;
		do {
			FOR(j,l/k)
				FOR(i,k)
					ns[j*k+i] = s[j*k+perm[i]];
			int c = 0;
			for (int i = 1; i <= l; i++)
				if (ns[i-1] != ns[i]) c++;
			minc <?= c;
		} while (next_permutation(perm, perm+k));
		printf("%d\n", minc);
	}
	return 0;
}
