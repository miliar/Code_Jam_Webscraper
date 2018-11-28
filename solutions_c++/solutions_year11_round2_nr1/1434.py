#include<stdio.h>
#include<vector>
#include<string>

using namespace std;

int main(){
	int T, tc = 1, N;
	for(scanf("%d ", &T); T; T--){
		printf("Case #%d:\n", tc++);
		scanf("%d ", &N);
		char g[N][N]; int wins[N], games[N];
		double WP[N], OWP[N], OOWP[N];
		for(int i = 0; i < N; i++){
			wins[i] = 0; games[i] = 0;
			for(int j = 0; j < N; j++){
				scanf("%c", &g[i][j]);
				if(g[i][j] == '1') wins[i]++;
				if(!(g[i][j] == '.')) games[i]++;
			}getchar();
			WP[i] = (double)wins[i] / (double)games[i];

		}
		for(int i = 0; i < N; i++){
			OWP[i] = 0;
			for(int j = 0; j < N; j++){
				if(j == i || g[i][j] == '.') continue;
				if(g[j][i] == '1'){
					OWP[i] += (WP[j]*(double)games[j] - 1.0)/
						((double)games[j] - 1);
				}
				else{
					OWP[i] += (WP[j] * (double)games[j]) / ((double)games[j] - 1);
				}
			}
			OWP[i] /= (double)(games[i]);
		}
		for(int i = 0; i < N; i++){
			OOWP[i] = 0;
			for(int j = 0; j < N; j++){
				if(i == j || g[i][j] == '.') continue;
				OOWP[i] += OWP[j];
			}
			OOWP[i] /= (double)(games[i]);
		}
		for(int i = 0; i < N; i++) 
			printf("%lf\n", 0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i]);
		
	}
	return 0;
}
