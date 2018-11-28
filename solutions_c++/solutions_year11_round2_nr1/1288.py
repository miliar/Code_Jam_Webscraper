#include<cstdio>

using namespace std;

int main() {
	int t;
	scanf("%d",&t);
	for(int caso=1;caso<=t;caso++) {
		int n;
		scanf("%d",&n);
		char T[n][n+1];
		for(int i=0;i<n;i++)
			scanf("%s",T[i]);
		long double OWP[n];
		for(int i=0;i<n;i++) {
			int to,wi;
			long double owp=0;
			int cant=0;
			for(int j=0;j<n;j++) {
				to=0,wi=0;
				if(j!=i && T[i][j]!='.') {
					for(int k=0;k<n;k++) {
						if(k!=i && T[j][k]!='.') {
							wi+=T[j][k]=='1';
							to++;
						}
					}
					cant++;
				}
				else
					to=1;
				owp+=(long double)wi/to;
			}
			OWP[i]=owp/cant;
		}
		printf("Case #%d:\n",caso);
		for(int i=0;i<n;i++) {
			long double wp=0;
			int wi=0,to=0;
			for(int j=0;j<n;j++)
				if(T[i][j]!='.') {
					wi+=T[i][j]=='1';
					to++;
				}
			wp=(long double)wi/to;
			long double owp=OWP[i];
			long double oowp=0;
			int cant=0;
			for(int j=0;j<n;j++)
				if(j!=i && T[i][j]!='.') {
					oowp+=OWP[j];
					cant++;
				}
			oowp/=(cant);
	//		printf("#%lf\n",oowp);
			long double rpi=0.25*wp+0.5*owp+0.25*oowp;
			printf("%llf\n",rpi);
		}
	}
}
