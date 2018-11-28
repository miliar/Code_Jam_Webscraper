#include<stdio.h>
#include<math.h>

int C;
int n;

int x[100], y[100], r[100];

double result;

double min(double a, double b)
{
	if(a < b) return a; else return b;
}

double max(double a, double b)
{
	if(a > b) return a; else return b;
}

double dist(int i, int j)
{
	return sqrt(double(x[i]-x[j])*(x[i]-x[j]) + double(y[i]-y[j])*(y[i]-y[j]));
}

int main()
{
	FILE *infile = fopen("c.in", "rt"), *outfile = fopen("c.out", "wt");
	fscanf(infile, "%d", &C);

	for(int tc=1; tc<=C; tc++) {
		fscanf(infile, "%d", &n);
		int i, j;

		for(i=0; i<n; i++) {
			fscanf(infile, "%d %d %d", &x[i], &y[i], &r[i]);
		}

		if(n == 1) {
			result = (double)r[0];
		}
		else if(n == 2) {
			result = max(r[0], r[1]);
		}
		else if(n == 3) {
			double r0, r1, r2;
			r0 = max( r[0], dist(1, 2) + r[1] + r[2] );
			r1 = max( r[1], dist(0, 2) + r[0] + r[2] );
			r2 = max( r[2], dist(0, 1) + r[0] + r[1] );
			result = min(min(r0, r1), r2) / 2.0;
		}

		fprintf(outfile, "Case #%d: %lf\n", tc, result);
	}

	fclose(infile);
	fclose(outfile);
	return 0;
}
