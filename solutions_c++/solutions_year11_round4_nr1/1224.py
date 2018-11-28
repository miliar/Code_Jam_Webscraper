#include <algorithm>
#include <vector>
#include <stdio.h>

int main() {
	int T = 0;
	scanf("%d", &T);
	for (int t = 0; t < T; ++t) {
		int N;
		double X, S, R, runtime;
		scanf("%lf %lf %lf %lf %d", &X, &S, &R, &runtime, &N);
		std::vector< std::pair< double, std::pair<double,double> > > V(N);
		for (int n = 0; n < N; ++n) scanf("%lf %lf %lf", &V[n].second.first, &V[n].second.second, &V[n].first);
		double vsum = 0;
		std::sort(V.begin(), V.end());
		for (int n = 0; n < N; ++n) vsum += V[n].second.second - V[n].second.first;
		double total_time = 0;
		{
			double len = X - vsum;
			if (len > 0 && runtime > 0) {
				double runlen = runtime * R;
				if (runlen > len) runlen = len;
				double runtimehere = runlen / R;
				total_time += runtimehere;
				runtime -= runtimehere;
				len -= runlen;
			}
			if (len > 0) {
				total_time += len / S;
			}
		}
		for (int n = 0; n < N; ++n) {
			double B, E, w;
			B = V[n].second.first;
			E = V[n].second.second;
			w = V[n].first;
			double len = E - B;
			if (runtime > 0) {
				double runlen = runtime * (R + w);
				double runtimehere = std::min(runlen, len) / (R + w);
				fprintf(stderr, "> B,E = %lf,%lf, runtimehere = %lf\n", B, E, runtimehere);
				total_time += runtimehere;
				runtime -= runtimehere;
				len -= runlen;
			}
			if (len > 0) {
				total_time += len / (S + w);
				fprintf(stderr, "> B,E = %lf,%lf, walk = %lf\n", B, E, len / (S + w));
			}
		}
		printf("Case #%d: %.6f\n", t+1, total_time);
	}
}
