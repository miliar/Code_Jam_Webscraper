#include <stdio.h>

int N;
char schedule[1000][1000];
double WP[1000];
double OWP[1000];
double OOWP[1000];
int NG[1000];
int main() {
	int T;
	scanf("%d", &T);
	for (int _ = 0; _ < T; _++) {
		printf("Case #%d:\n", _+1);
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
			scanf(" %s", schedule[i]);
		for (int i = 0; i < N; i++) {
			NG[i] = 0;
			WP[i] = 0;
			for (int j = 0; j < N; j++) {
				if (schedule[i][j] == '1') {
					NG[i]++;
					WP[i] += 1.;
				} else if (schedule[i][j] == '0') {
					NG[i]++;
				}
			}
			WP[i] /= NG[i];
		}
		for (int i = 0; i < N; i++) {
			OWP[i] = 0;
			for (int j = 0; j < N; j++) {
				if (schedule[i][j] == '0') {
					OWP[i] += (WP[j]*NG[j] - 1)/(NG[j]-1);
				} else if (schedule[i][j] == '1') 
					OWP[i] += (WP[j]*NG[j])/(NG[j]-1);
			}
			OWP[i] /= NG[i];
		}
		for (int i = 0; i < N; i++) {
			OOWP[i] = 0;
			for (int j = 0; j < N; j++) {
				if (schedule[i][j] == '1' || schedule[i][j] == '0')
					OOWP[i] += OWP[j];
			}
			OOWP[i] /= NG[i];
		}
		for (int i = 0; i < N; i++) {
			printf("%.12f\n", 0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i]);
		}
	}
	return 0;
}
