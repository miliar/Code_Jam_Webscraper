#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <limits.h>
#define N_MAX 1000

int main (int argc, char * const argv[]) {
	FILE *fpi, *fpo;
	int num;
	int R, k, N;
	int grp[N_MAX];
	double g[N_MAX*2];
	
	double plis[N_MAX];
	int nidx[N_MAX], indx;
	double money, temp;
	char home[512];
	
	strcpy(home, getenv("HOME"));
	if ((fpi = fopen(strcat(home, "/temp/C-small-attempt2.in.txt"), "r")) == NULL){

		printf("error\n");
		exit(11);
	}
	strcpy(home, getenv("HOME"));
	if ((fpo = fopen(strcat(home, "/temp/out_C_small.txt"), "w")) == NULL){
		printf("error\n");
		exit(10);
	}
	
	
	fscanf(fpi, "%d", &num);
	for(int i=1; i<=num; i++){
		fscanf(fpi, "%d %d %d", &R, &k, &N);
		for(int j=0; j<N; j++) fscanf(fpi, "%d", &grp[j]);
		for(int j=0; j<N; j++){ g[j]=(double)grp[j]; g[j+N] = (double)grp[j]; }
		
		temp = 0; for(int j=0; j<N; j++) temp += g[j];
		if(temp <= k){
			money = temp * R;
		}else{
			for(int j=0; j<N; j++){
				temp = 0; indx = j;
				while(temp <= k && indx-j < N) {temp += g[indx]; indx++; }
				plis[j] = temp - g[--indx];
				if(indx < N) nidx[j] = indx; else nidx[j] = indx - N;
			}
			
			money = 0; indx = 0;
			for(int j=0; j<R; j++){
				money += plis[indx];
				indx = nidx[indx];
			}
		}
		
		fprintf(fpo, "Case #%d: %.0lf\n", i, money);
	}
	
	
    return 0;
}

