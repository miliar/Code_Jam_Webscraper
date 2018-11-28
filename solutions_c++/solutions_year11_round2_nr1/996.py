#include <cstdio>

char a[111][111];
double WP[111], OWP[111], OOWP[111];

int t, n, w[111], l[111];

int main(){
	scanf("%d", &t);
	for (int i = 0; i < t; i++){
		scanf("%d", &n);
		for (int j = 0; j < n; j++)
			for (int q = 0; q < n; q++)
				scanf(" %c", &a[j][q]);
		
		for (int j = 0; j < n; j++){
			w[j] = l[j] = 0;
			for (int q = 0; q < n; q++){
				if (a[j][q] == '0')
					l[j]++;
				if (a[j][q] == '1')
					w[j]++;
			}
			WP[j] = double(w[j]) / (w[j] + l[j]);
		}
		
		int tmp;
		for (int j = 0; j < n; j++){
			tmp = 0;
			OWP[j] = 0;
			for (int q = 0; q < n; q++)
				if (a[j][q] != '.'){
					OWP[j] += double(w[q] - (a[q][j] - '0')) / (w[q] + l[q] - 1);
					tmp++;
				}
			OWP[j] /= tmp;
		}
		
		for (int j = 0; j < n; j++){
			tmp = 0;
			OOWP[j] = 0;
			for (int q = 0; q < n; q++)
				if (a[j][q] != '.'){
					OOWP[j] += OWP[q];
					tmp++;
				}
			OOWP[j] /= tmp;
		}
		
		printf("Case #%d:\n", i + 1);
		for (int j = 0; j < n; j++)
			printf("%.09lf\n", 0.25 * WP[j] + 0.5 * OWP[j] + 0.25 * OOWP[j]);
	}
}
