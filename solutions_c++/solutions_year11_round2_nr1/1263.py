#include <stdio.h>
int k,n,tc,ti,i,j,w,g;
char s[1000][1000];
double wp[1000],owp[1000],oowp[1000];
int main(){
	scanf("%d",&tc);
	for (ti=1;ti<=tc;ti++){
		scanf("%d",&n);
		for (i=0;i<n;i++){
			scanf("%s",s[i]);
			w=g=0;
			for (j=0;s[i][j];j++){
				if (s[i][j]=='1')
					w++;
				if (s[i][j]!='.')
					g++;
			}
			wp[i]=w/(double)g;
		}
		for (i=0;i<n;i++){
			owp[i]=0;
			int x=0;
			for (j=0;j<n;j++)
				if (i!=j && s[i][j]!='.'){
					x++;
					w=g=0;
					for (k=0;k<n;k++){
						if (k!=i){
							if (s[j][k]=='1')
								w++;
							if (s[j][k]!='.')
								g++;
						}
					}
					owp[i]+=w/(double)g;
				}
			owp[i]/=x;
		}
		for (i=0;i<n;i++){
			oowp[i]=0;
			int x=0;
			for (j=0;j<n;j++)
				if (i!=j && s[i][j]!='.'){
					x++;
					oowp[i]+=owp[j];
				}
			oowp[i]/=x;
		}
		printf("Case #%d:\n",ti);
		for (i=0;i<n;i++)
			printf("%lf\n",0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
	}
	return 0;
}