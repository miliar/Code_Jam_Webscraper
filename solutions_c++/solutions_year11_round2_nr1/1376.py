#include <stdio.h>
#include <string.h>
char w[200][200];
double wp[200];
double owp[200];
double oowp[200];
int main () {
	freopen ("A-large.in","r",stdin);
	freopen ("a-large.out","w",stdout);
	int t;
	scanf ("%d",&t);
	for (int ca=1;ca<=t;ca++) {
		
		int n;
		scanf ("%d",&n);
		for (int i=0;i<n;i++) {
			scanf ("%s",w[i]);
		}
		for (int i=0;i<n;i++) {
			double sum=0,mm=0;
			for (int j=0;j<n;j++) {
				if (w[i][j] == '1') {
					mm++;
				}
				if (w[i][j]!='.') {
					sum++;
				}
			}
			if (sum!=0) 
			wp[i] = mm/sum;
		}
		for (int i=0;i<n;i++) {
			double sum=0,num=0;
			for (int j=0;j<n;j++) {
				if (j==i || w[i][j]=='.')continue;
				
				num++;
				double p=0,q=0;
				for (int k=0;k<n;k++) {
					if (k==i)continue;
					if (w[j][k]=='1') {
						p++;
					}
					if (w[j][k]!='.') {
						q++;
					}
				}
				sum+=p/q;
			}
			if (num!=0) {
				owp[i] = sum/num;
			}
		}
		for (int i=0;i<n;i++) {
			double sum=0,num=0;
			for (int j=0;j<n;j++) {
				if (w[i][j]!='.') {
					num++;
					sum+=owp[j];
				}
			}
			if (num != 0) {
				oowp[i] = sum/num;
			}
		}
		
	
		printf ("Case #%d:\n",ca);
		
		for (int i=0;i<n;i++ ) {
			printf ("%lf\n",0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
		}
	}
	return 0;
}
