#include <cstdio>
#include <algorithm>
#define MAXN 105
using namespace std;

int T, N;
char W[MAXN][MAXN];
int GP[MAXN];
int GW[MAXN];

double OWP[MAXN];
double OOWP[MAXN];

int main() {
	scanf("%d ", &T);
	for(int i = 0; i < T; i++) {
		scanf("%d ", &N);
		for(int j = 0; j < N; j++) {
			scanf("%s ", &W[j][0]);
			GP[j] = 0;
			GW[j] = 0;
		}
		for(int j = 0; j < N; j++) {
			for(int k = 0; k < N; k++) {
				GP[j] += W[j][k] != '.';
				GW[j] += W[j][k] == '1';
			}
		}
		for(int j = 0; j < N; j++) {
			double wp_sum = 0;
			int opp = 0;
			for(int k = 0; k < N; k++) {
				if(W[j][k] != '.') {
					opp++;
					int gp = GP[k] - 1;
					int gw = GW[k] - (W[k][j] == '1');
					wp_sum += double(gw)/double(gp);
				}
			}
			OWP[j] = wp_sum / double(opp);
		}
		for(int j = 0; j < N; j++) {
			double owp_sum = 0;
			int opp = 0;
			for(int k = 0; k < N; k++) {
				if(W[j][k] != '.') {
					opp++;
					owp_sum += OWP[k];
				}
			}
			OOWP[j] = owp_sum / double(opp);
		}
		printf("Case #%d:\n", i+1);
		for(int j = 0; j < N; j++) {
			printf("%.10lf\n", 0.25 * (double(GW[j])/double(GP[j])) + 0.5 * OWP[j] + 0.25 * OOWP[j]);
		}
	}
	return 0;
}
