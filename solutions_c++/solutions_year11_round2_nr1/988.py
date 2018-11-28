#include <stdio.h>
#include <string.h>

#define MAX 110

char results[MAX][MAX];
double WP[MAX], OWP[MAX], OOWP[MAX];

double calcWP(int n,char *games) {
	int total=0, score=0;
	for(int j=0;j<n;++j) {
		total += games[j] != '.';
		score += games[j] == '1';
	}
	return total==0 ? 0 : ((double)score)/total;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;++test) {
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;++i)
			scanf("%s",&results[i]);
		for(int i=0;i<n;++i) {
			WP[i]=calcWP(n,results[i]);
		}
		for(int i=0;i<n;++i) {
			double sumWP=0;
			int total=0;
			for(int j=0;j<n;++j) {
				if(results[i][j] != '.') {
					++total;
					char t=results[j][i];
					results[j][i]='.';
					sumWP+=calcWP(n, results[j]);
					results[j][i]=t;
				}
			}
			OWP[i]=total==0 ? 0 : sumWP/total;
		}
		for(int i=0;i<n;++i) {
			double sumOWP=0;
			int total=0;
			for(int j=0;j<n;++j) {
				if(results[i][j]!='.') {
					++total;
					sumOWP+=OWP[j];
				}
			}
			OOWP[i]=total==0 ? 0 : sumOWP/total;
		}
		printf("Case #%d:\n",test);
		for(int i=0;i<n;++i) {
//			printf("%0.20lf %0.20lf %0.20lf\n",WP[i], OWP[i], OOWP[i]);
			printf("%0.20lf\n",0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);
		}
	}
	return 0;
}
