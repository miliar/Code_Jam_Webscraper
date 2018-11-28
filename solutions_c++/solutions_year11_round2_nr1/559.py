#include <iostream>
#include <cstdio>
using namespace std;

const int maxn = 200;

int T;
int N;
char d[maxn][maxn];
double WP[maxn], OWP[maxn], OOWP[maxn];
int g[maxn], w[maxn];

double WPp[maxn];
          
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> T;
	for (int t = 1; t <= T; t++) {
		for (int i = 0; i < maxn; i++) {
			WP[i] = OWP[i] = OOWP[i] = 0;
			g[i] = w[i] = 0;
		}	
		cin >> N;
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				cin >> d[i][j];
			}
		}
		
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if (d[i][j] != '.') {
					g[i]++;
					w[i] += (d[i][j] == '1');
				}
			} 
		}

		//WP calc
		for (int i = 1; i <= N; i++) {
			WP[i] = (1.0 * w[i]) / (1.0 * g[i]);
		}

		//OWP calc
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if (d[i][j] != '.') {
					if (d[i][j] == '1') OWP[i] += 1.0 * w[j] / (1.0 * g[j] - 1);
					else OWP[i] += 1.0 * (w[j] - 1) / (1.0 * g[j] - 1);
				}
			}
			OWP[i] /= g[i];
		}

		//OOWP calc
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if (d[i][j] != '.') {
					OOWP[i] += OWP[j];
				}
			}
			OOWP[i] /= g[i];
		}

		printf("Case #%d:\n", t);
		for (int i = 1; i <= N; i++) {
			printf("%.9lf\n", 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
			//printf("%.9lf\n", WP[i]);
		}
	}
}