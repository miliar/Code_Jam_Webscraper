#include <cstdio>
#include <cstdlib>
#include <algorithm>
#define MAX 200

using namespace std;

int main(){
	int T;
	scanf ("%d", &T);
	for (int t = 1; t <= T; t++){
		int N;
		scanf ("%d", &N);
		char m[MAX][MAX];
		for (int i = 0; i < N; i++)
			scanf (" %s", m[i]);
		double wp[MAX], owp[MAX], oowp[MAX];
		double w[MAX], p[MAX];
		double rpi[MAX];
		for (int i = 0; i < N; i++){
			w[i] = 0.0, p[i] = 0.0;
			for (int j = 0; j < N; j++){
				if (m[i][j] == '0')
					p[i]++;
				if (m[i][j] == '1'){
					p[i]++;
					w[i]++;
				}
			}
			wp[i] = p[i] > 0 ? w[i]/p[i] : 0;
		}
		for (int i = 0; i < N; i++){
			owp[i] = 0.0;
			for (int j = 0; j < N; j++){
				if (p[j] == 0.0)
					continue;
				if (m[i][j] == '0')
					owp[i] += (w[j]-1.0)/(p[j]-1.0);
				if (m[i][j] == '1')
					owp[i] += (w[j])/(p[j]-1.0);
			}
			owp[i] = p[i] > 0 ? owp[i]/p[i] : 0.0;
		}
		for (int i = 0; i < N; i++){
			oowp[i] = 0.0;
			for (int j = 0; j < N; j++){
				if (m[i][j] != '.')
					oowp[i] += owp[j];
			}
			oowp[i] = p[i] > 0 ? oowp[i]/p[i] : 0.0;
		}
		printf ("Case #%d:\n", t);
		for (int i = 0; i < N; i++)
			printf ("%.10lf\n", 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]);
	}
	return 0;
}
