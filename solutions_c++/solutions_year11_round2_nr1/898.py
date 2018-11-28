#include <stdio.h>

int arr[100][100];
int win[100];
int total[100];
double WP[100];
double OWP[100];
double OOWP[100];

int main()
{
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; ++Case) {
		int N;
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				char c;
				do {
					scanf("%c", &c);
				} while (c != '0' && c != '1'
					 && c != '.');
				if (c == '0')
					arr[i][j] = -1;
				else if (c == '1')
					arr[i][j] = 1;
				else
					arr[i][j] = 0;
			}
		}
		for (int i = 0; i < N; ++i) {
			int w = 0;
			int t = 0;
			for (int j = 0; j < N; ++j) {
				if (arr[i][j] == 1) {
					++w;
					++t;
				} else if (arr[i][j] == -1) {
					++t;
				}
			}
			win[i] = w;
			total[i] = t;
			WP[i] = ((double) w) / t;
		}
		for (int i = 0; i < N; ++i) {
			double sum = 0.0;
			int t = 0;
			for (int j = 0; j < N; ++j) {
				if (arr[i][j] == 1) {
					sum += ((double) win[j]) / (total[j] - 1);
					++t;
				} else if (arr[i][j] == -1) {
					sum += ((double) (win[j] - 1)) / (total[j] - 1);
					++t;
				}
			}
			OWP[i] = sum / t;
		}
		for (int i = 0; i < N; ++i) {
			double sum = 0.0;
			int t = 0;
			for (int j = 0; j < N; ++j) {
				if (arr[i][j] != 0) {
					sum += OWP[j];
					++t;
				}
			}
			OOWP[i] = sum / t;
		}
		printf("Case #%d:\n", Case);
		for (int i = 0; i < N; ++i) {
			double ans = 0.25 * WP[i]
				+ 0.50 * OWP[i]
				+ 0.25 * OOWP[i];
			//printf("%f %f %f %f\n",
			  //     WP[i], OWP[i], OOWP[i], ans);
			printf("%f\n", ans);
		}
	}
	return 0;
}

