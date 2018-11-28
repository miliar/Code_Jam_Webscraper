#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

typedef pair<int,int> ii;

#define REP(i,n) for (int i = 0; i < (n); i++)

int main () {

	int cases;

	scanf ("%d",&cases);

	REP(tt, cases) {
		printf ("Case #%d: ",tt+1);
		vector<ii> presses;
		int p, k, l;

		scanf ("%d %d %d",&p,&k,&l);

		if (p*k < l) { printf ("Impossible\n"); continue; }

		REP(key, l) {
			int P;
			scanf ("%d",&P);

			presses.push_back (make_pair (P, key));
		}

		sort (presses.rbegin(), presses.rend());

		int level = k;
		int penalty = 1;
		long long cost = 0;

		REP(P, presses.size()) {
			level--;
			cost += presses[P].first * penalty;
			if (level == 0) { level = k; penalty++; }
		}

		printf ("%lld\n",cost);
	}




	return 0;
}
