#include<stdio.h>

char A[200][200];
double WINS[200];
double TOT[200];
double WP[200];
double OWP[200];
double OOWP[200];

int main() {
	int t,T,i,j,N;
	scanf("%d",&T);
	for(t=1;t<=T;t++) {
		scanf("%d",&N);
		for(i=0;i<N;i++) scanf("%s",A[i]);
		
		for(i=0;i<N;i++) {
			int tot=0;
			double sum = 0;
			for(j=0;j<N;j++) {
				if(A[i][j]=='.') continue;
				tot++;
				sum+=(A[i][j]=='1');
			}
			WP[i] = sum/tot;
			WINS[i] = sum;
			TOT[i] = tot;
		}

		for(i=0;i<N;i++) {
			int tot=0;
			double sum = 0;
			for(j=0;j<N;j++) {
				if(A[i][j]=='.') continue;
				tot++;
				sum+=(WINS[j] - (A[j][i]=='1'))/(TOT[j]-1);
			}
			OWP[i] = sum/tot;
		}
		
		for(i=0;i<N;i++) {
			int tot=0;
			double sum = 0;
			for(j=0;j<N;j++) {
				if(A[i][j]=='.') continue;
				tot++;
				sum+=OWP[j];
			}
			OOWP[i] = sum/tot;
		}
		
		printf("Case #%d:\n",t);
		for(i=0;i<N;i++) printf("%.9lf\n",0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
	}
	return 0;
}
