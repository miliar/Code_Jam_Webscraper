#include <cstdio>
#include <algorithm>

using namespace std;

double solve() {
	int A, B;
	scanf("%d %d", &A, &B);

	double res = B+2;


	double succesProb = 1;

	for(int i = 0; i < A; i++) {
		double prob;
		scanf("%lf", &prob);
		succesProb *= prob;
		int missing = 2*(A-i-1) + (B-A);
		res = min(res,  (succesProb*(1+missing) + (1-succesProb)*(missing+B+2)));

	}


	return res;

}

int main() {
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) {
		printf("Case #%d: %.10lf\n", i, solve());
	}

}