#include <string>
#include <vector>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;

/* PREWRITTEN CODE */

#define ALL(x) x.begin(),x.end()
#define PB push_back


#define FOR(i,p,k) for (int i=p; i<k; i++)
#define REP(i,n) for (int i=0; i<n; i++)
#define SIZE(x) (int)x.size()
/* COMPETITION CODE */

typedef long long ll;

int main () {
  int number_of_tests;
  scanf("%d", &number_of_tests);
  REP (test_number, number_of_tests) {
    printf("Case #%d: ", test_number+1);
    int R, k, N;
	int tab[1010];
	int ear[1010];
	int ski[1010];
	int cle[1010];
	ll cer[1011];
	scanf("%d %d %d", &R, &k, &N);
	REP (i, N) scanf("%d", &tab[i]);
	int ok = 0;
	REP (i, N) {if (ok <= k) ok += tab[i];}
	if (ok <= k) {printf("%lld\n", (ll) ok * (ll) R);}
	else {
		REP (i, N) {
			ear[i] = 0;
			int j;
			for (j = i; (j != i || ear[i] == 0) && ear[i] + tab[j] <= k; j = (j+1) % N) {
				ear[i] += tab[j];
			}
			ski[i] = j;
		}
		int taken[1010];
		REP (i, N) {
			REP (j, N) taken[j] = 0;
			int pos = i;
			cle[i] = 0;
			cer[i] = 0LL;
			while (!taken[pos]) {
				taken[pos] = 1;
				cle[i] += 1;
				cer[i] += (ll) ear[pos];
				pos = ski[pos];
			}
			if (pos != i) {
				cle[i] = -1;
			}
		}
		ll res = 0LL;
		int pos = 0;
		while (cle[pos] == -1 && R > 0) {
			res += (ll) ear[pos];
			R -= 1;
			pos = ski[pos];
		}
		while (R >= cle[pos]) {
			res += (ll) cer[pos];
			R -= cle[pos];
		}
		while (R > 0) {
			res += (ll) ear[pos];
			R -= 1;
			pos = ski[pos];
		}
/*printf("\n");		
REP (i, N) printf("i: %d, tab: %d, ski: %d, ear: %d, cle: %d, cer: %lld\n", i, tab[i], ski[i], ear[i], cle[i], cer[i]);*/
		printf("%lld\n", res);
	}
  }
  return 0;
}

