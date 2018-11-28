#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <set>

using namespace std;

int cn, N;

double WP[200], OWP[200], OOWP[200],aux;
char team[200][200];

int main() {
	int cases;
	scanf("%d",&cases);
	while (cases--) {
		scanf("%d",&N);
		for (int i=0; i < N; ++i) {
			scanf("%s",team[i]);
		}
		
		int matches;
		int vict=0;
		for (int i=0; i < N; ++i) {
			matches=0;
			vict=0;
			for (int j=0; j < N; ++j) {
				if (i==j) continue;
				if (team[i][j]=='.') continue;
				++matches;
				if (team[i][j]=='1') ++vict;
			}
			WP[i] = (double)(vict)/(double)(matches);
			//printf("WP[%d]=%.6lf\n",i,WP[i]);
		}
		
		
		
		for (int i=0; i < N; ++i) {
			OWP[i]=0;
			aux=0;
			//printf("check OWP of %d\n",i);
			for (int j=0; j < N; ++j) {
				if (j == i) continue;
				if (team[i][j]=='.') continue;
				++aux;
				matches=0;
				vict=0;
				for (int k=0; k < N; ++k) {
					if (k == i) continue;
					if (team[j][k]=='.') continue;
					++matches;
					if (team[j][k]=='1') ++vict;
				}
				
				OWP[i]+=(double)(vict)/(double)(matches);
			}
			OWP[i] /= (double)(aux);
			//printf("OWP[%d]=%.6lf\n",i,OWP[i]);
		}
		
		for (int i=0; i < N; ++i) {
			OOWP[i]=0;
			matches=0;
			for (int j=0; j < N; ++j) {
				if (i==j) continue;
				if (team[i][j]=='.') continue;
				++matches;
				OOWP[i] += OWP[j];
			}
			OOWP[i] /= (double)matches;
			//printf("OOWP[%d]=%.6lf\n",i,OOWP[i]);
		}
		
		
		printf("Case #%d:\n",++cn);
		for (int i=0; i < N; ++i) {
			printf("%.10lf\n",0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i]);
		}
	}
	
	return 0;
}
