#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
	int t,k=0;
	freopen("A-large.in","r",stdin);
	freopen("result.txt","w",stdout);
	scanf("%d",&t);
	while(k++<t){
		int n;
		int i,j,l;
		double WP[110]={0};
		double OWP[110]={0};
		double OOWP[110]={0};
		double win[110]={0};
		double num[110]={0};
		char match[105][105];
		
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf(" %s",match[i]);
			for(j=0;j<n;j++){
				if(match[i][j]=='1'){
					win[i]+=1;
					num[i]+=1;
				}
				else if(match[i][j]=='0'){
					num[i]+=1;
				}
			}
		}
		for(i=0;i<n;i++)
			WP[i]=win[i]/num[i];
		for(i=0;i<n;i++){
			double temp[110]={0};
			for(j=0;j<n;j++){
				if(match[i][j]=='.')
					temp[j]=0;
				else if(match[i][j]=='1')
					temp[j]=win[j]/(num[j]-1);
				else
					temp[j]=(win[j]-1)/(num[j]-1);
				
			}
			for(j=0;j<n;j++)
				OWP[i]+=temp[j];
			OWP[i]/=num[i];
		}
		for(i=0;i<n;i++){
			for(j=0;j<n;j++)
				if(match[i][j]!='.')
					OOWP[i]+=OWP[j];
			OOWP[i]/=num[i];
		}
		printf("Case #%d:\n",k);
		for(i=0;i<n;i++)
			printf("%.8lf\n",0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);
	}
	return 0;
}