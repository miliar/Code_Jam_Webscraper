#include <iostream>
#include <cstdio>

char map[101][101];
double WP[101],COUNT[101],TOT[101],OWP[101],OOWP[101];

int main()
{
    int t, n;

    freopen("a.txt", "r", stdin);
	

	scanf("%d\n", &t);

	freopen("b.txt", "w", stdout);

	for (int q = 0; q < t; q++) {
		scanf("%d\n", &n);
		for (int i = 0; i < n; i++) 
			scanf("%s",map[i]);			
		for (int i = 0; i < n; i++) {
			WP[i] = 0;
			COUNT[i] = TOT[i] = 0;
			for (int j = 0; j < n; j++) {
				if (map[i][j] != '.') TOT[i]++;
				if (map[i][j] == '1') COUNT[i]++;
			}
			if (TOT[i] > 0) WP[i] = 1.0 * COUNT[i] / TOT[i]; else WP[i] = 0;
		}
		for (int i = 0; i < n; i++) {
			OWP[i] = 0;
			int tot = 0;
			for (int j = 0; j < n; j++) 
				if (map[i][j] != '.') {
					tot++;
					if (map[i][j] == '1') {
					    if (TOT[j] > 1) OWP[i] += COUNT[j] / (TOT[j] - 1);
					} else if (TOT[j] > 1) OWP[i] += (COUNT[j] - 1) / (TOT[j] - 1);
				}
            if (tot > 0) OWP[i] /= tot;
		}
        for (int i = 0; i < n; i++) {
			OOWP[i] = 0;
			int tot = 0;
			for (int j = 0; j < n; j++) 
				if (map[i][j] != '.') {
					tot++;
					OOWP[i] += OWP[j];
				}
            if (tot > 0) OOWP[i] /= tot;
		}
		printf("Case #%d: \n", q + 1);
		for (int i = 0; i < n; i++) 
			printf("%.6lf\n", 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]);
	}
}