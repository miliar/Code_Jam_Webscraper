#include <stdio.h>
#include <string>
#include <map>
#include <set>
using namespace std;

int X, S, R, t, N;
int B[1001];
int E[1001];
int w[1001];
double y, tt;
int i, j;

int main() {
	int kejs, kejsis;
	scanf("%d", &kejsis);
	for (kejs = 1; kejs <= kejsis; kejs++) {
		printf("Case #%d: ", kejs);
		scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
		for (i = 0; i < N; i++) {
			scanf("%d%d%d", &B[i], &E[i], &w[i]);
			X -= (E[i] - B[i]);
		}

		/*
		bool ch;
		do {
			ch = false;
			for (i = 1; i < N; i++) {
				if (B[i-1] > B[i]) {
					swap(B[i], B[i-1]);
					swap(E[i], E[i-1]);
					swap(w[i], w[i-1]);
					ch = true;
				}
			}
		} while (ch);
	*/
		y = 0;
		tt = t;

		if (X > 0) {
			double v = R;
			double s = X;
			double t2 = s / v;

			if (t2 > tt) {
				double s2 = tt*v;
				double t3 = (s - s2) / (S);
				y += tt + t3;
				tt = 0;
			} else{
				y += t2;
				tt -= t2;
			}
		}

		for (;;) {
			int mi = -1;
			for (i = 0; i < N; i++) {
				if (B[i] < 0) continue;
				if (mi == -1 || w[i] < w[mi]) mi = i;
			}
			if (mi == -1) break;
			double v = w[mi] + R;
			double s = (E[mi] - B[mi]);
			double t2 = s / v;
			if (t2 > tt) {
				double s2 = tt*v;
				double t3 = (s - s2) / (w[mi] + S);
				y += tt + t3;
				tt = 0;
			} else{
				y += t2;
				tt -= t2;
			}
			B[mi] = -1;
		}

		printf("%.10lf\n", y);
	}
	return 0;
}
