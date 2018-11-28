#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<set>
#include<map>

using namespace std;

char mat[1000][1000];
int GW[1000];
int GP[1000];
double OWP[1000];

int main() {
	int T, N;
	
	scanf("%d\n", &T);
	
	for(int nCase = 1; nCase <= T; nCase++) {
		scanf("%d\n", &N);
		
		memset(GW, 0, sizeof(GW));
		memset(GP, 0, sizeof(GP));
		
		for(int i = 0; i < N; i++) {
			scanf("%s", mat[i]);
			
			int gp = 0, gw = 0;
			
			OWP[i] = 0;
			
			for(int j = 0; j < N; j++) {
				if(mat[i][j] == '.') continue;
				
				GP[i]++;
				GW[i] += (mat[i][j] == '1');
			}
		}
		
		for(int i = 0; i < N; i++) {
			OWP[i] = 0;
			int div = 0;
			for(int j = 0; j < N; j++) {
				if(mat[i][j] != '.' && j != i) {
					OWP[i] += (GW[j] - (mat[j][i] == '1')) / (double) (GP[j] - 1);
					div++;
				}
			}
			OWP[i] /= div;
		}
		
		printf("Case #%d:\n", nCase);
		
		// RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
		
		for(int i = 0; i < N; i++) {
			double rpi = 0;
			double OOWP = 0;
			int div = 0;
			
			for(int j = 0; j < N; j++) {
				if(mat[i][j] != '.') {
					OOWP += OWP[j];
					div++;
				}
			}
			OOWP /= div;
			
			rpi += GW[i] / (4.0 * GP[i]);
			rpi += OWP[i] / 2;
			rpi += OOWP / 4;
			
			//printf("\tWP = %f OWP = %f OOWP = %f\n", GW[i] / (double) GP[i], OWP[i], OOWP);
			
			printf("%.10f\n", rpi);
		}
	}
}
