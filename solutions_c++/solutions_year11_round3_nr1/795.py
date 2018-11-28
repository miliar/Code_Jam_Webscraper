#include <cstdio>
#include <algorithm>
#include <set>
#include <queue>
#include <string>
#include <vector>
#include <list>
using namespace std;

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORE(it,V) for(__typeof(V.begin()) it = V.begin(); it != V.end(); ++it)
#define FI first
#define SE second
#define PB push_back
#define MP make_pair
typedef long long LL;

char buf[57][57];
void testcase() {
	int n, m;
	scanf("%d%d", &n, &m);
	REP(i,n) scanf("%s", buf[i]);
	REP(i,n) REP(j,m) {
		if (buf[i][j] == '#') {
			if (i == n-1 || j == m-1 || buf[i][j+1] != '#'
				|| buf[i+1][j] != '#' || buf[i+1][j+1] != '#') {
				printf("Impossible\n");
				return;
			}
			buf[i][j] = '/';
			buf[i][j+1] = '\\';
			buf[i+1][j] = '\\';
			buf[i+1][j+1] = '/';
		}
	}
	REP(i,n) {
		REP(j,m) printf("%c", buf[i][j]);
		printf("\n");
	}
}

int main() {
	int t, v = 0;
	for (scanf("%d", &t); t--;) {
		printf("Case #%d:\n", ++v);
		testcase();
	}
}
