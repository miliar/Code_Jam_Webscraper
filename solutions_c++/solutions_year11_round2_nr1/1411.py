#include <stdio.h>

void run() {
	int n;
	char game[200][200];
	scanf("%d",&n);
	for (int i = 0 ; i < n ; ++i) {
		scanf("%s",game[i]);
	}
	// show
	double wp[200];
	double owp[200];
	double oowp[200];
	int nrm[200];
	for (int i = 0 ; i < n ; ++i) {
		double w=0,l=0;
		nrm[i] = 0;
		for (int j = 0 ; j < n ; ++j) {
			if (game[i][j] == '1') w+=1;
			if (game[i][j] == '0') l+=1;
			if (game[i][j] != '.') nrm[i]++;
		}
		wp[i] = w/(w+l);
	}
	for (int k = 0 ; k < n ; ++k) {
		owp[k]=0;
		for (int i = 0 ; i < n ; ++i) {
			if (i == k) continue; // self is not opponent of k
			if (game[i][k]=='.') continue; // i is not opponent of k
			double w=0,l=0;
			for (int j = 0 ; j < n ; ++j) {
				if (j == k) continue; // exclude games against k
				if (game[i][j] == '1') w+=1;
				if (game[i][j] == '0') l+=1;
			}
			//printf(" team %d, ignoring %d  wp %f\n",i,k,w/(w+l));
			owp[k] += w/(w+l);
		}
		owp[k]/=nrm[k];
	}
	for (int k = 0 ; k < n ; ++k) {
		oowp[k] = 0;
		for (int i = 0 ; i < n ; ++i) {
			if (i == k) continue; // self is not opponent of k
			if (game[i][k]=='.') continue; // i is not opponent of k
			oowp[k] += owp[i];
		}
		oowp[k]/=nrm[k];
	}
	for (int i = 0 ; i < n ; ++i) {
		//printf("%d %d %f %f %f   ",i,nrm[i],wp[i],owp[i],oowp[i]);
		printf("%.8f\n",0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
	}
}
int main() {
	int runs;
	scanf("%d",&runs);
	for (int i=0;i<runs;++i) {
		printf("Case #%d:\n",i+1);
		run();
	}
	return 0;
}