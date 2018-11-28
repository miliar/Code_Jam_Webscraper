#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <string>
#include <math.h>
#include <algorithm>
#include <queue>
using namespace	std;
const int max_size = 103;
char A[max_size][max_size];
double WP[max_size];
double OWP[max_size][max_size];
double SOWP[max_size], OOWP[max_size];
int main(){
#ifdef	xDx
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
	int T;
	int N;
	scanf("%d",&T);
	for(int i=0;i < T ; i++){
		scanf("%d",&N);
		getchar();
		for(int j=0; j < N ; j++){
			int all=0, win=0;
			for(int l=0; l < N ; l++){
				scanf("%c",&A[j][l]);
				if(A[j][l] == '1' || A[j][l] == '0'){
					all++;
					if(A[j][l] == '1')
						win++;
				}
			}
			WP[j] = (double)win/all;
			for(int l=0; l < N ; l++){			
				if(A[j][l] == '1' || A[j][l] == '0'){
					int k = win;
					if(A[j][l] == '1')
						k--;
					OWP[l][j] = (double) k/(all-1);
				}
			}
			getchar();
		}




		for(int j=0; j < N ; j++){
			int all=0;
			SOWP[j] = 0;
			for(int l=0; l < N ; l++){
				if(A[j][l] == '1' || A[j][l] == '0'){
					all++;
					SOWP[j]+= OWP[j][l];
				}
			}
			SOWP[j] /= (double)all;
		}

		for(int j=0; j < N ; j++){
			int all=0;
			OOWP[j] = 0;
			for(int l=0; l < N ; l++){
				if(A[j][l] == '1' || A[j][l] == '0'){
					all++;
					OOWP[j]+= SOWP[l];
				}
			}
			OOWP[j] /= (double)all;
		}
		printf("Case #%d:\n",i+1);
		for(int j =0; j<N; j++)
			printf("%.10lf\n",0.25 * WP[j] + 0.50 * SOWP[j] + 0.25 * OOWP[j]);
		
	}
	return 0;
}