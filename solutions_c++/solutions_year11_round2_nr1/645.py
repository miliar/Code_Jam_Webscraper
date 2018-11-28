#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int ca=0; ca<t; ca++) {
		printf("Case #%d:\n", ca+1);
		int n;
		cin >> n;
		char a[100][100];
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				char ch;
				cin >> ch;
				a[i][j] = ch;
			}
		}
		
		double wp[100], owp[100], oowp[100];
		
		int ne[100];
		
		for (int i=0; i<n; i++) {
			int wins = 0, total = 0;
			for (int j=0; j<n; j++) {
				if (a[i][j] == '1') {
					wins++;
					total++;
				}
				else if (a[i][j] == '0') {
					total++;
				}
			}
			wp[i] = (double) wins / total;
			ne[i] = total;
		}
		
		for (int i=0; i<n; i++) {
			double fz = 0;
			int fm = 0;
			//printf("for %d\n", i);
			for (int j=0; j<n; j++) {
				if (a[i][j] != '.') {
					//printf("was %.4lf, %d, %d\n", wp[j], ne[j], a[j][i] - '0');
					//printf("fz %d += %.4lf\n", j, (wp[j] * ne[j] - (a[j][i] - '0')) / (ne[j] - 1));
					fz += (wp[j] * ne[j] - (a[j][i] - '0')) / (ne[j] - 1);
					fm++;
				}
			}
			owp[i] = fz / fm;
		}
		for (int i=0; i<n; i++) {
			double fz = 0;
			int fm = 0;
			for (int j=0; j<n; j++) {
				if (a[i][j] != '.') {
					fz += owp[j];
					fm++;
				}
			}
			oowp[i] = fz / fm;
			
			//printf("%.6lf %.6lf %.6lf\n", wp[i], owp[i], oowp[i]);
			printf("%.12lf\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
		}
		
	}
}	
