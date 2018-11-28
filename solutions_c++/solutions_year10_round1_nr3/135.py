#include<stdio.h>
#include<math.h>
int a[1000010]={},k=0;
int main(){
int j,T,t,A,A1,B,B1,y;
long long ans;
double p=(1.0+sqrt(5.0))/2,i,e; 
for(i=1;;i++){
	e=ceil(i*p);
	if(e>1000000)break;
	else a[(int)e]=1;
	}
a[0]=1;
for(j=1;j<=1000000;j++)a[j]+=a[j-1];
scanf("%d",&T);
for(t=1;t<=T;t++){
scanf("%d%d%d%d",&A,&A1,&B,&B1);
ans=(long long)(A1-A+1)*(B1-B+1);
for(j=B;j<=B1;j++){
	k=a[j];
	if(A>k)k=A;
	y=a[j]+j-1;
	if(A1<y)y=A1;
	if(y<k)continue;
	ans-=(long long)y-k+1;
	}
printf("Case #%d: %I64d\n",t,ans);
}
scanf(" ");
}
