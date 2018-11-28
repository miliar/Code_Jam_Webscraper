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

char buf[150][150];
int wygranych[150];
int wszystkich[150];
double result[150];
double WP[150];
double OWP[150];
double OOWP[150];

void testcase() {
	int n;
	scanf("%d", &n);
	REP(i,n) {
		WP[i] = OWP[i] = OOWP[i] = 0.0;
		wygranych[i] = wszystkich[i] = 0;
		scanf("%s", buf[i]);
	}

	REP(i,n) REP(j,n) if (buf[i][j] != '.') {
		++wszystkich[i];
		if (buf[i][j] == '1')
			++wygranych[i];
	}

	REP(i,n) {
		if (wszystkich[i] > 0) {
			WP[i] = (double)wygranych[i] / (double)wszystkich[i];
		} else {
			WP[i] = 0;
		}
	}

	REP(i,n) {
		REP(j,n) if(i != j) {
			if (buf[i][j] != '.') {
				if (buf[i][j] == '1')
					OWP[i] += (double)wygranych[j] / (double)(wszystkich[j]-1);
				else OWP[i] += (double) (wygranych[j]-1) / (double) (wszystkich[j]-1);
			}
		}
		OWP[i] /= (double)(wszystkich[i]);
	}

	REP(i,n) {
		OOWP[i] = 0.0;
		REP(j,n)
			if (buf[i][j] != '.')
				OOWP[i] += OWP[j];
		OOWP[i] /= (double)(wszystkich[i]);
	}
	REP(i,n)
	printf("%.7lf\n", 0.25*WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]);
}

int main() {
	int t, v = 0;
	for (scanf("%d", &t); t--;) {
		printf("Case #%d:\n", ++v);
		testcase();
	}
}
