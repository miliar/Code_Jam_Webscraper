#include <stdio.h>

int T,N;
char P[100][101];
int Win[100];
int Count[100];
double WP[100];
double OWP[100];
double OOWP[100];

FILE *in = fopen("input.txt","r");
FILE *out = fopen("output.txt","w");

int main(void){
	int t,i,j;
	fscanf(in,"%d",&T);
	for(t=1;t<=T;t++){
		fscanf(in,"%d",&N);
		for(i=0;i<N;i++){
			Win[i]=0;
			Count[i]=0;
			fscanf(in,"%s",P[i]);
			for(j=0;j<N;j++){
				if(P[i][j]=='.')continue;
				Count[i]++;
				if(P[i][j]=='1')Win[i]++;
			}
			WP[i]=(double)Win[i] / Count[i];
		}
		for(i=0;i<N;i++){
			OWP[i]=0;
			for(j=0;j<N;j++){
				if(P[i][j]=='.')continue;
				OWP[i]+=(double)(Win[j]-P[j][i]+'0')/(Count[j]-1)/Count[i];
			}
		}
		fprintf(out,"Case #%d:\n",t);
		for(i=0;i<N;i++){
			OOWP[i]=0;
			for(j=0;j<N;j++){
				if(P[i][j]=='.')continue;
				OOWP[i]+=OWP[j]/Count[i];
			}
			double pr=0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
			fprintf(out,"%.6lf\n",pr);
		}
	}
	return 0;
}
