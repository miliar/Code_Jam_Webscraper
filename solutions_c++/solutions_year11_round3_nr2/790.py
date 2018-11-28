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

const int MAXN = 1001;
LL L, t, n, c;
LL sumy[MAXN];

LL solve1() {
	LL result = sumy[n-1];
	REP(i,n) { // booster
		// i-ty odcinek przebedzie szybciej
		LL kiedy = 0;
		if (i) kiedy = sumy[i-1];
		LL dl = sumy[i] - kiedy;
		LL normalnie = max(t-kiedy, 0LL); // kiedy dotrze
		result = min(result, sumy[n-1] - dl + normalnie + (dl-normalnie)/2);
	}
	return result;
}

LL solve2() {
	LL result = sumy[n-1];
	REP(i,n) REP(j,i) {
		//j-ty pierwszy
		LL kiedyJ = 0;
		if (j) kiedyJ = sumy[j-1];
		LL dlJ = sumy[j] - kiedyJ;
		LL normalnieJ = max(t-kiedyJ, 0LL);

		LL kiedyI = sumy[i-1];
		kiedyI = min(kiedyI, sumy[i-1] - dlJ + normalnieJ + (dlJ-normalnieJ)/2);
		LL dlI = sumy[i] - sumy[i-1];

		LL normalnieI = max(t-kiedyI, 0LL);
		LL nomI = sumy[i] - sumy[i-1];
		LL nomJ = sumy[j] - sumy[j-1];
		result = min(result, sumy[n-1] - nomI - nomJ + min(nomJ, normalnieJ + (dlJ-normalnieJ)/2) + min(nomI, normalnieI + (dlI - normalnieI)/2));
	}
	return result;
}

void testcase() {
	scanf("%lld%lld%lld%lld", &L, &t, &n, &c);
	vector<LL> chlopy;
	REP(i,c) {
		LL x;
		scanf("%lld", &x);
		chlopy.PB(x*2);
	}

	vector<LL> praw;
	REP(i,n) {
		praw.PB( chlopy[i%c] );
		sumy[i] = chlopy[i%c];
		if (i) sumy[i] += sumy[i-1];
	}

	if (L == 0) {
		printf("%lld\n", sumy[n-1]);
	} else if (L == 1) {
		printf("%lld\n", solve1());
	} else {
		printf("%lld\n", solve2());
	}
}

int main() {
	int t, v = 0;
	for (scanf("%d", &t); t--;) {
		printf("Case #%d: ", ++v);
		testcase();
	}
}
