#include <stdio.h>
#include <string.h>

#define N 1000

int T,n;
char t[N][N];
double wp[N],owp[N],oowp[N];
int k[N];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int lT,i,j;
	scanf("%d",&T);
	for(lT=1;lT<=T;lT++){
		memset(wp,0,sizeof(wp));
		memset(owp,0,sizeof(owp));
		memset(oowp,0,sizeof(oowp));
		memset(k,0,sizeof(k));

		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%s",t[i]);

		for(i=0;i<n;i++){
			for(j=0;j<n;j++){
				if(t[i][j]=='1'){
					wp[i]++;
					k[i]++;
				}else if(t[i][j]=='0'){
					k[i]++;
				}
			}
		}

		for(i=0;i<n;i++){
			for(j=0;j<n;j++){
				if(t[i][j]=='1'){
					owp[i]+=wp[j]/(k[j]-1);
				}else if(t[i][j]=='0'){
					owp[i]+=(wp[j]-1)/(k[j]-1);
				}
			}
			if(k[i])owp[i]/=k[i];
		}

		for(i=0;i<n;i++){
			for(j=0;j<n;j++){
				if(t[i][j]!='.'){
					oowp[i]+=owp[j];
				}
			}
			if(k[i]){
				wp[i]/=k[i];
				oowp[i]/=k[i];
			}
		}

		printf("Case #%d:\n",lT);
		for(i=0;i<n;i++)
			printf("%.7lf\n",0.25*wp[i]+0.50*owp[i]+0.25*oowp[i]);
	}
	return 0;
}
