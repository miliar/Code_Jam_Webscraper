#include <cstdio>
#include <vector>
using namespace std;

int P[1100000], V[1100000];
const double eps = 1e-9;

int main() {
	int T;
	scanf("%d", &T);
	int C, D;


	for (int t=0; t<T; ++t) {
		scanf("%d%d", &C, &D);
		int sum = 0;
		for (int i=0; i<C; ++i) {
			scanf("%d%d", &P[i], &V[i]);
			sum += V[i];
		}

		double hi = sum * D;
		double lo = 0;

		while (hi - lo > eps) {
			double mid = (lo + hi) / 2;

			bool valid = true;
			double next = -1e9;
			for (int i=0; i<C; ++i) {
				double first = P[i] - mid;
				if (first < next) first = next;

				next = first + double(D) * V[i];
				if (next - D > P[i] + mid + eps) {
					valid = false;
					break;
				}
			}

			if (valid) hi = mid; else lo = mid;
		}

		printf("Case #%d: %.9lf\n", t+1, hi);
	}
	return 0;
}
