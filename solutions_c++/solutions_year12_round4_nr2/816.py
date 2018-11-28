#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <math.h>
using namespace std;

int i, j, k, kejsis, kejs, n, W, L;
int ret;
double sx[1000], sy[1000], vx[1000], vy[1000], d, v;
double r[1000];

inline double sqr(double x) {
	return x*x;
}

inline double bad (int i, int j) {
	return sqrt(sqr(sx[i] - sx[j]) + sqr(sy[i] - sy[j])) - (r[i] + r[j]);
}

int main(int argc, char ** argv) {
	int fk = 1, tk;
	scanf("%d", &kejsis);
	tk = kejsis;
	if (argc == 3) {
		sscanf(argv[1], "%d", &fk);
		sscanf(argv[2], "%d", &tk);
	}
	for (int kejs = 1; kejs <= kejsis; ++kejs) {
		scanf("%d%d%d", &n, &W, &L);
		for (i = 0; i < n; i++) {
			scanf("%lf", &r[i]);
			sx[i] = (rand() % 10000) / 10000.;
			sy[i] = (rand() % 10000) / 10000.;
		}
		if (kejs < fk || kejs > tk) continue;
		printf("Case #%d:", kejs);

		bool zmena = true;
		while (zmena) {
			zmena = false;
			for (i = 0; i < n; i++) vx[i] = vy[i] = 0;

			for (i = 0; i < n; i++) {
				for (j = i+1; j < n; j++) {
					d = sqrt(sqr(sx[i] - sx[j]) + sqr(sy[i] - sy[j]));
					v = r[i] + r[j];
					if (d - v < 1e-6) {
						zmena = true;
						vx[i] += (sx[i] - sx[j]) / d;
						vx[j] += (sx[j] - sx[i]) / d;
						vy[i] += (sy[i] - sy[j]) / d;
						vy[j] += (sy[j] - sy[i]) / d;
					}
				}
			}
			for (i = 0; i < n; i++) {
				sx[i] += vx[i]; if (sx[i] < 0) sx[i] = (rand() % 10000) / 10000000.; if (sx[i] > W) sx[i] = W - (rand() % 10000) / 10000000.;
				sy[i] += vy[i]; if (sy[i] < 0) sy[i] = (rand() % 10000) / 10000000.; if (sy[i] > L) sy[i] = L - (rand() % 10000) / 10000000.;
			}
/*
			for (i = 0; i < n; i++) {
				for (j = i+1; j < n; j++) {
					while (sx[i] == sx[j] && sy[i] == sy[j]) {
						sx[i] += (rand() % 10000) / 10000. - 0.5; if (sx[i] < 0) sx[i] = 0; if (sx[i] > W) sx[i] = W;
						sy[i] += (rand() % 10000) / 10000. - 0.5; if (sy[i] < 0) sy[i] = 0; if (sy[i] > L) sy[i] = L;
					}
				}
			}
			*/
		}
		for (i = 0; i < n; i++) {
			printf(" %.10lf %.10lf", sx[i], sy[i]);
		}
		printf("\n");
	}
	return 0;
}

