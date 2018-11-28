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

int c[10001];
int xgate[10001];
int gate[10001];
int val[10001];

int main(void)
{
	freopen("a.in", "rt", stdin);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: ", tc);
		int m, v;
		scanf("%d%d", &m, &v);
		for (int i = 0; i < (m-1)/2; i++) {
			scanf("%d%d", &gate[i], &c[i]);
			xgate[i] = gate[i];
		}
		for (int i = 0; i < (m+1)/2; i++) {
			scanf("%d", &val[(m-1)/2+i]);
		}
		//
		int L = (m-1)/2;
		int numC = 0;
		FOR(i,L) if (c[i]) numC++;
		int answer = 9999;
		for (int mask = 0; mask < (1 << numC); mask++) {
			int pc = __builtin_popcount(mask);
			if (pc >= answer) continue;
			int X = mask;
			FOR(i,L) if (c[i]) {
				if (X&1) gate[i] = 1- xgate[i];
				else gate[i] = xgate[i];
				X >>= 1;
			}
			for (int i = L-1; i>=0; i--) {
				int child1 = val[(i+1)*2-1];
				int child2 = val[(i+1)*2];
				if (gate[i] == 1) child1 &= child2;
				else child1 |= child2;
				val[i] = child1;
			}
			if (val[0] == v) answer = pc;
		}
		if (answer == 9999)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", answer);
	}
	return 0;
}
