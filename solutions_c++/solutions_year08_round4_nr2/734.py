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
#define RL(i,s) for (unsigned i = 0; i < s.length(); i++)

char s[60000];
char ns[60000];

int c[10001];
int xgate[10001];
int gate[10001];
int val[10001];

int main(void)
{
	freopen("b.in", "rt", stdin);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: ", tc);
		int n, m, a;
		scanf("%d%d%d", &n, &m, &a);
		int sx1=-1, sy1, sx2, sy2;
		FOR(x1, n+1)
		FOR(y1, m+1)
		FOR(x2, n+1)
		FOR(y2, m+1) {
			int t = x1*y2-x2*y1;
			if (abs(t) == a) {
				sx1 = x1;
				sy1 = y1;
				sx2 = x2;
				sy2 = y2;
			}
		}
		if (sx1 == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("0 0 %d %d %d %d\n", sx1, sy1, sx2, sy2);
	}
	return 0;
}
