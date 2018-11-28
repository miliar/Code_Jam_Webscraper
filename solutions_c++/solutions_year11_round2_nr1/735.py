# include <cstdio>
# include <cstring>
# include <string>
# include <vector>
# include <set>
# include <map>
# include <algorithm>
# include <queue>
# include <stack>
# include <cassert>
# include <ctime>
# include <cstdlib>

using namespace std;

int T;

int N;

char tab[128][128];
double wp[128], owp[128], oowp[128];
double wp2[128][128];

int main (void){
	scanf("%d", &T);
	for(int tc = 1; tc <= T; tc++){
		scanf("%d", &N);
		for(int i = 0 ; i < N; i++){
			scanf(" %s", tab[i]);
		}
		
		for(int i = 0 ; i < N; i++){
			int total = 0;
			int wins = 0;
			for(int j = 0; j < N; j++){
				if( tab[i][j] == '1' ) wins++;
				if( tab[i][j] != '.') total++;
			}
			wp[i] = (double) wins/total;
			for(int j = 0; j < N; j++){
				wp2[i][j] = wp[i];
				total = 0;
				wins = 0;	
				for(int k = 0 ; k < N; k++){
					if( j == k ) continue;
					if( tab[i][k] == '1' ) wins++;
					if( tab[i][k] != '.') total++;
				}
				wp2[i][j] = (double) wins/total;				
			}
		}
		
		for(int i = 0 ; i < N; i++){
			int total = 0;
			double soma = 0.0;
			for(int j = 0; j < N; j++){
				if( tab[i][j] != '.' ){
					soma += wp2[j][i];
					total++;
				}
			}
			owp[i] = soma/total;
		}
		
		for(int i = 0 ; i < N; i++){
			int total = 0;
			double soma = 0.0;
			for(int j = 0; j < N; j++){
				if( tab[i][j] != '.' ){
					soma += owp[j];
					total++;
				}
			}
			oowp[i] = soma/total;
		}
		
		printf("Case #%d:\n", tc);
		for(int i = 0 ; i < N; i++){
			printf("%.12f\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
		}
	}
	return 0;
}