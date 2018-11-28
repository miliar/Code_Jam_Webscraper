#include<stdio.h>
#include<stdlib.h>
int N;
char schedule[121][121];
double WP[121];
double WPFO[121][121];
double OWP[121];
double OOWP[121];
int win[121];
int count[121];
int main(){
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++){
		scanf("%d",&N);
		for(int i=0;i<N;i++){
			win[i] = 0;
			count[i] = 0;
			WP[i] = OWP[i] = OOWP[i] = 0.0;
			for(int j=0;j<N;j++){
				WPFO[i][j] = 0.0;
			}
		}
		for(int i=0;i<N;i++){
			scanf("%s",schedule[i]);
			for(int j=0;j<N;j++){
				if(schedule[i][j] != '.'){
					count[i]++;
					if(schedule[i][j] == '1'){
						win[i]++;
					}
				}
			}
		}


		// for WP
		for(int i=0;i<N;i++){
			WP[i] = win[i];
			WP[i] /= count[i];
		}
		//for OWP
		for(int i=0;i<N;i++){
			OWP[i] = 0.0;
			for(int j=0;j<N;j++){
				int tmpw = win[j];
				if(schedule[i][j] == '.'){
					continue;
				}
				if(schedule[i][j] == '1'){
					OWP[i] += (tmpw) * 1.0 / (count[j] - 1);
				}
				if(schedule[i][j] == '0'){
					OWP[i] += (tmpw - 1) * 1.0 / (count[j] - 1);
				}
			}
			OWP[i] /= count[i];
		}
		// for OOWP
		for(int i=0;i<N;i++){
			OOWP[i] = 0.0;
			for(int j=0;j<N;j++){
				if(schedule[i][j] == '.'){
					continue;
				}
				OOWP[i] += OWP[j];
			}
			OOWP[i] /= count[i];
		}


		printf("Case #%d:\n",t + 1);
		for(int i=0;i<N;i++){
			printf("%.12lf\n",0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]);
		}
		
	}
	return 0;
}
