#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <functional>
#include <utility>

static double work()
{
	int B[2048];
	int W[2048];
	int X;
	int S, R;
	int t;
	int oN;
	scanf ("%d%d%d%d%d", &X, &S, &R, &t, &oN);
	R -= S;
	size_t N = 0;
	int prevE = 0;
	for (int i=0; i<oN; ++i) {
		int b, e, w;
		scanf ("%d%d%d", &b, &e, &w);
		if (b > prevE) {
			B[N] = prevE;
			W[N++] = S;
		}
		B[N] = b;
		W[N++] = w + S;
		prevE = e;
	}
	if (X > prevE) {
		B[N] = prevE;
		W[N++] = S;
	}
	B[N] = X;

	double D[2048];
	for (size_t i=0; i<N; ++i)
		D[i] = B[i+1] - B[i];

	// All running?
	{
		double T = 0;
		for (size_t i=0; i<N; ++i)
			T += D[i] / (W[i] + R);
		if (T <= t)
			return T;
	}

	// Some walk.
	{
		double wp[2048];
		for (size_t i=0; i<N; ++i)
			wp[i] = 1. + (double)R / W[i];

		unsigned ind[2048];
		for (size_t i=0; i<N; ++i)
			ind[i] = i;
		auto cmp = [&] (unsigned i, unsigned j) {
			return wp[i] > wp[j];
		};
		std::sort (ind, ind + N, cmp);
		double leftt = t;
		double T = t;
		for (size_t i=0; i<N && leftt>0; ++i) {
			size_t j = ind[i];
			double limit = D[j] / (W[j] + R);
			if (leftt > limit) {
				leftt -= limit;
				T -= limit * wp[j];
			}
			else {
				T -= leftt * wp[j];
				leftt = 0;
			}
		}
		for (size_t i=0; i<N; ++i)
			T += D[i] / W[i];
		return T;
	}
}

int main()
{
	int T;
	scanf ("%d", &T);
	for (int i=1; i<=T; ++i)
		printf ("Case #%d: %.9f\n", i, work());
	return 0;
}
