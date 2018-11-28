#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
using namespace std;

#define MAX 105
double wp[MAX], owp[MAX], oowp[MAX], oppo[MAX];
double wp_z[MAX][MAX]; // wp_z[r][c] is the WP of r without considering match against c
char map[MAX][MAX];
char line[1024];

int main()
{
	int kase, serial=1,
		n;
	double win, match, sum;

	gets(line);
	kase = atoi(line);
	while (kase--) {
		// begin test case
		gets(line);
		n = atoi(line);

		for (int r=0; r<n; ++r) gets(map[r]);

		for (int r=0, c; r<n; ++r) {
			win = match = 0;
			for (c=0; c<n; ++c) {
				switch (map[r][c]) {
				case '1': match+=1; win+=1; break;
				case '0': match+=1; break;
				}
			}
			oppo[r] = match; // num of opponent
			wp[r] = win / match;

			for (c=0; c<n; ++c) {
				switch (map[r][c]) {
				case '1': wp_z[r][c] = (win-1) / (match-1); break;
				case '0': wp_z[r][c] = win / (match-1); break;
				case '.': wp_z[r][c] = win / match; break;
				}
//				printf("%.2lf ", wp_z[r][c]);
			}
//			puts("");
		}
//		puts("==");

		for (int r=0, c; r<n; ++r) {
			sum = 0;
			for (c=0; c<n; ++c)
				if (r != c && map[r][c] != '.')
					sum += wp_z[c][r];

			owp[r] = sum / oppo[r];
		}

		for (int r=0, c; r<n; ++r) {
			sum = 0;
			for (c=0; c<n; ++c)
				if (r != c && map[r][c] != '.')
					sum += owp[c];
			oowp[r] = sum / oppo[r];
		}

//		for (int i=0; i<n; ++i)
//			printf("%.10lf ", wp[i]);
//		puts("");
//		for (int i=0; i<n; ++i)
//			printf("%.10lf ", owp[i]);
//		puts("");
//		for (int i=0; i<n; ++i)
//			printf("%.10lf ", oowp[i]);
//		puts("");


		printf("Case #%d:\n", serial++);
		for (int i=0; i<n; ++i) {
			printf("%.10lf\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
		}
		// end test case
	}
	return 0;
}
