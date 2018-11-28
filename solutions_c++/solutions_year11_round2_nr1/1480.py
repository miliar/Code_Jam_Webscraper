#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#define FOR(i,a,b) for(int i=int(a); i<int(b); ++i)
#define FORD(i,a,b) for(int i=int(a)-1; i>=int(b); --i)
#define FORE(i,q) for(typeof((q).begin()) i=(q).begin(); i!=(q).end(); ++i)
using namespace std;

typedef long long LG;
typedef long double LD;

struct wp {
    int wins, matches;
} Rank[111];

int n;
LD OWP[111], OOWP[111];
char T[111][111];

void calcwp(int k) {
    Rank[k].matches = Rank[k].wins = 0;
    OWP[k] = OOWP[k] = 0;
    FOR(i,0,n) {
	if(T[k][i] != '.') ++Rank[k].matches;
	if(T[k][i] == '1') ++Rank[k].wins;
    }
}

void calcowp(int k) {
    FOR(i,0,n) {
	if(T[k][i] == '.') continue;
	OWP[k] += LD(Rank[i].wins - int(T[i][k] - '0'))
		/ LD(Rank[i].matches - 1);
    }
    OWP[k] /= LD(Rank[k].matches);
}

void calcoowp(int k) {
    FOR(i,0,n) {
	if(T[k][i] == '.') continue;
	OOWP[k] += OWP[i];
    }
    OOWP[k] /= LD(Rank[k].matches);
}

void testcase(int zzz) {
    scanf("%d", &n);
    FOR(i,0,n) scanf("%s", T[i]);
    FOR(i,0,n) calcwp(i);
    FOR(i,0,n) calcowp(i);
    FOR(i,0,n) calcoowp(i);
    printf("Case #%d:\n", zzz);
    FOR(i,0,n) {
	printf("%.9Lg\n",
	    0.25 * LD(Rank[i].wins) / LD(Rank[i].matches) +
	    0.5 * OWP[i] + 0.25 * OOWP[i]
	);
    }
}

int main() {
    int ZZZ; scanf("%d", &ZZZ);
    FOR(zzz,0,ZZZ) testcase(zzz + 1);
    return 0;
}
