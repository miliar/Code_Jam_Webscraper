#include <stdio.h>
#include <math.h>

int T, t;
__int64 n, A, B, C, D, X0, Y0, M;
double aX[100000], aY[100000];
__int64 X, Y;
int i, j, k;

double len(double X1, double Y1, double X2, double Y2)
{
  return sqrt((X1 - X2) * (X1 - X2) + (Y1 - Y2) * (Y1 - Y2));
}

int main() {

	FILE *in = fopen("A-small.in", "rt");
	FILE *out = fopen("A-small.out", "wt");

	//FILE *in = fopen("A-large.in", "rt");
	//FILE *out = fopen("A-large.out", "wt");

	fscanf(in, "%d", &T);

	for (t = 1; t <= T; t++) {
		fscanf(in, "%d %d %d %d %d %d %d %d", &n, &A, &B, &C, &D, &X0, &Y0, &M);
		
		X = X0; Y = Y0;
		aX[0] = X; aY[0] = Y;
		for (i = 1; i < n; i++) {
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			aX[i] = X;
			aY[i] = Y;
		}

		int cnt = 0;
		for (i = 0; i < n; i++) {
			for (j = i+1; j < n; j++) {
				if (aX[j] == aX[i] && aY[j] == aY[i]) continue;
				for (k = j+1; k < n; k++) {
					if ((aX[k] == aX[j] && aY[k] == aY[j]) ||
						(aX[k] == aX[i] && aY[k] == aY[i])) continue;
					//if (len(aX[i],aY[i], aX[j],aY[j]) + len(aX[i],aY[i], aX[k],aY[k]) < len(aX[j],aY[j], aX[k],aY[k])) continue;
					//if (len(aX[i],aY[i], aX[k],aY[k]) + len(aX[k],aY[k], aX[j],aY[j]) < len(aX[i],aY[i], aX[j],aY[j])) continue;
					//if (len(aX[i],aY[i], aX[j],aY[j]) + len(aX[j],aY[j], aX[k],aY[k]) < len(aX[i],aY[i], aX[k],aY[k])) continue;
					__int64 iX1, iY1, iX2, iY2, iX3, iY3;
					iX1 = aX[i]; iY1 = aY[i];
					iX2 = aX[j]; iY2 = aY[j];
					iX3 = aX[k]; iY3 = aY[k];
					if ((iX1 + iX2 + iX3) % 3 == 0 && (iY1 + iY2 + iY3) % 3 == 0) cnt++;
				}
			}
		}
		
		fprintf(out, "Case #%d: %d\n", t, cnt);


	}

	fclose(in);
	fclose(out);

	return 0;
}