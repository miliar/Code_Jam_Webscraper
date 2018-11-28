#include<stdio.h>
#define MAX 1000000000
#define MM 260
int a[300],b[300];
int main(){
int T,t,D,I,M,n,i,x,j,d,k,e,p,ans;
scanf("%d",&T);
for(t=1;t<=T;t++){
scanf("%d%d%d%d",&D,&I,&M,&n);
for(i=0;i<MM;i++)a[i]=0;
for(i=0;i<n;i++){
	scanf("%d",&x);
	for(j=0;j<MM;j++){
		b[j]=MAX;
		e=x-j;
		if(e<0)e*=-1;
		for(k=0;k<MM;k++){
			p=j-k;
			if(p<0)p*=-1;
			if(p<=M)d=0;
			else if(M==0)d=MAX;
			else d=(p-1)/M*I;
			if(d+D+a[k]<b[j])b[j]=a[k]+d+D;
			if(d+e+a[k]<b[j])b[j]=a[k]+d+e;
			}
		}
	ans=MAX;
	for(j=0;j<MM;j++){a[j]=b[j];if(ans>b[j])ans=b[j];}
	}
printf("Case #%d: %d\n",t,ans);
}
}
