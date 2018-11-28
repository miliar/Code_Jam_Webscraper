#include <cstdio>

#include <vector>
using namespace std;

typedef vector<int> TIntVector;
typedef vector<float> TFloatVector;
typedef vector<TFloatVector> TFloatVectorVector;

double Power(double p, int n) {
	double res = 1.;
	for (int i = 0; i < n; ++i)
		res *= p;
	return res;
}

int main() {
	// freopen("input.txt", "r", stdin);
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);

	int t;
	scanf("%d", &t);

	static const size_t MAXN = 1001;

	TFloatVectorVector binom;
	binom.resize(MAXN);
	binom[0].resize(1);
	binom[0][0] = 1.;
	for (size_t i = 1; i < MAXN; ++i) {
		binom[i].resize(i + 1);
		binom[i][0] = 1.;
		binom[i][i] = 1.;
		for (size_t j = 1; j < i; ++j)
			binom[i][j] = binom[i - 1][j - 1] + binom[i - 1][j];
	}
	
	for (int iTest = 0; iTest < t; ++iTest) {
		int n;
		TIntVector perm;
		scanf("%d", &n);
		int bad = 0;
		for (int i = 0; i < n; ++i) {
			int m;
			scanf("%d", &m);
			if (m != i + 1)
				++bad;
		}
		TFloatVector probs(n + 1);
		probs[bad] = 1;

		double ans = 0;
		size_t i = 0;
		double p = 0;
		while ((1. - p > 1e-9) && (i < 10000)) {
			ans += probs[0]*i;
			p += probs[0];

			TFloatVector nextProbs(n + 1);
			for (size_t j = 1; j <= n; ++j)
				for (size_t k = 0; k <= j; ++k)
					nextProbs[k] += probs[j]*binom[j][k]*Power(1 - 1./j, k)*Power(1./j, j - k);
			probs = nextProbs;
			++i;
		}

		printf("Case #%d: %.10lf\n", iTest + 1, ans);
	}

	return 0;
}