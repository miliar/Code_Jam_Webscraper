#include <cstdio>
#include <string.h>
#include <memory.h>
double owp[110],oowp[110],wp[110],rpi[110];
int n,T;
int adj[110][110];
char str[110];
int main() {
	FILE *fi=fopen("input.txt","rt");
	FILE *fo=fopen("output.txt","wt");
	fscanf(fi,"%d",&T);
	int Ti;
	for(Ti=0;Ti<T;Ti++) {
		fscanf(fi,"%d ",&n);
		int i,j,cnt;
		for(i=1;i<=n;i++) {
			cnt=0;
			fscanf(fi,"%s",str+1);
			for(j=1;j<=strlen(str+1);j++) {
				if(str[j]=='.') adj[i][j]=-1;
				else {
					adj[i][j]=str[j]-'0';
					wp[i]+=adj[i][j];
					cnt++;
				}
			}
			if(cnt!=0) {
				wp[i]/=(double)cnt;
				cnt=0;
			} else wp[i]=0;
		}
		int k,rcnt=0;
		double wpsum,sum=0;
		for(k=1;k<=n;k++) {
			wpsum=0;
			rcnt=0;
			for(i=1;i<=n;i++) {
				if(adj[k][i]==-1) continue;
				rcnt++;
				if(i==k) continue;
				cnt=0;
				sum=0;
				for(j=1;j<=n;j++) {
					if(j==k) continue;
					if(adj[i][j]>-1) {
						cnt++;
						sum+=adj[i][j];
					}
				}
				wpsum+=sum/((double)(cnt));
			}
			owp[k]=wpsum/rcnt;
		}
		sum=0;
		wpsum=0;
		cnt=0;
		for(k=1;k<=n;k++) {
			sum=0;
			cnt=0;
			for(j=1;j<=n;j++) {
				if(adj[k][j]!=-1) {
					sum+=owp[j];
					cnt++;
				}
			}
			oowp[k]=sum/cnt;
		}
		fprintf(fo,"Case #%d:\n",Ti+1);
		for(i=1;i<=n;i++) {
			fprintf(fo,"%g\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
		}
		memset(wp,0,sizeof(wp));
		memset(owp,0,sizeof(owp));
		memset(oowp,0,sizeof(oowp));
	}
}