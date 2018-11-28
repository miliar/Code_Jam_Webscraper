#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define len 120
char s[len][len];
int wp[len][2],n;
double owp[len],oowp[len];
void init(){
	int i,j,sum,num;
	scanf("%d",&n);
	memset(wp,0,sizeof(wp));
	for(i=0;i<n;i++){
		scanf("%s",s[i]);
		for(j=sum=num=0;j<n;j++)
			if(s[i][j]!='.'){
				if(s[i][j]=='1')
					sum++;
				num++;
			}
		wp[i][0]=sum;   wp[i][1]=num;
	}
}
void find_owp(){
	int i,j,num;
	double sum;
	for(i=0;i<n;i++){
		for(j=num=0,sum=0.;j<n;j++)
			if(s[i][j]!='.'){
				if(s[i][j]=='0')
					sum+=(double)(wp[j][0]-1)/(wp[j][1]-1);
				else if(s[i][j]=='1')
					sum+=(double)wp[j][0]/(wp[j][1]-1);
				num++;
			}
		owp[i]=sum/num;
	}
}
void find_oowp(){
	int i,j,num;
	double sum;
	for(i=0;i<n;i++){
		for(j=num=0,sum=0.;j<n;j++)
			if(s[i][j]!='.'){
				sum+=owp[j];
				num++;
			}
		oowp[i]=sum/num;
	}
}
int main(void){
	//freopen("12.in","r",stdin);
	//freopen("12.out","w",stdout);
	int ncase,i,j;
	scanf("%d",&ncase);
	for(i=1;i<=ncase;i++){
		init();
		find_owp();
		find_oowp();
		printf("Case #%d:\n",i);
		for(j=0;j<n;j++)
			printf("%.6lf\n",0.25 * (double)wp[j][0]/wp[j][1] + 0.50 * owp[j] + 0.25 * oowp[j]);
	}
	return 0;
}