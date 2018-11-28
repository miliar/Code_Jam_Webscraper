#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;

int n;
char str[101][101];
double score[101];

double wp[101], owp[101], oowp[101];

double cal(int a, int b) {
	double sum = 0.0f;
	int num = 0;
	for (int i = 0; i < n; ++i) {
		if (i != b) {
			if (str[a][i] != '.') {
				sum ++;
				if (str[a][i] == '1') num++;
			}
		}
	}

	return num / sum;
}

int main() {
	int t;
	freopen("A.in", "r", stdin);
	freopen("outA.txt", "w", stdout);

	scanf ("%d", &t);
	for (int ii = 1; ii <= t; ++ii) {
		scanf ("%d", &n);
		memset(score, 0, sizeof(score));

		int num;
		double sum;
		for (int i = 0; i < n; ++i) {
			num = 0;
			sum = 0.0;
			scanf ("%s", str[i]);
			for  (int j = 0; j < n; ++j) {
				if (str[i][j] == '1') {
					num++;
				}
				if (str[i][j] != '.')
					sum++;
			}
			wp[i] = (double) num / sum;
		}

		for (int i = 0; i < n; ++i) {
		    sum = 0.0f;
			num = 0;


			for (int j = 0; j < n; ++j) {
				if (str[i][j] != '.') {
					num++;
					sum += cal(j, i);
				}
			}
			owp[i] = sum / num;
		}

		for (int i = 0; i < n; ++i) {
			double sum = 0.0f;
			num = 0;

			for (int j = 0; j < n; ++j) {
				if (str[i][j] != '.') {
					num++;
					sum += owp[j];
				}
			}
			oowp[i] = sum / num;
		}

		printf("Case #%d:\n", ii); 
		for (int i = 0; i < n; ++i) {
			score[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
			printf("%.12lf\n", score[i]);
		}
	}
}