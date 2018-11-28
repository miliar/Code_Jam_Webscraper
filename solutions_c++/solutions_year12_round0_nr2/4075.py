#include <iostream>
using namespace std;  

void solve(int);

int main() {
	int testCases;
	scanf("%d",&testCases);
	for(int i = 1; i <= testCases; ++i) {
		solve(i);
	}
	return 0;
}

void solve(int testCase) {
	int n, s ,p, ti[100], numberOfGooglersWithAtLeastP = 0, nonSurprisingMax, surprisingMax;
	scanf("%d%d%d",&n,&s,&p);
	for(int i = 0; i < n; ++i) {
		scanf("%d",&ti[i]);
		nonSurprisingMax = ti[i]/3;
		surprisingMax = ti[i]/3;
		if((ti[i]%3) == 0) {
			++surprisingMax;
		} else if((ti[i]%3) == 1) {
			++nonSurprisingMax;
			++surprisingMax;
		} else {
			++nonSurprisingMax;
			surprisingMax += 2;
		}
		if((ti[i]/3) == 0 && (ti[i]%3) < 2) {
			surprisingMax = 0;
		}
		if(nonSurprisingMax >= p) {
			++numberOfGooglersWithAtLeastP;
		} else if(s > 0 && surprisingMax >= p) {
			--s;
			++numberOfGooglersWithAtLeastP;
		}
	}
	printf("Case #%d: %d\n", testCase, numberOfGooglersWithAtLeastP);
}