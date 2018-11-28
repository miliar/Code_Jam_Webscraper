#include<stdio.h>
#include<malloc.h>
int main(){
long long int t,n;
long long int a[1000001];
long long int sum,yash,i;
long long int min1,sum1;
scanf("%lld",&t);
for(yash=1;yash<=t;yash++){
scanf("%lld",&n);
for(i=0;i<n;i++)
scanf("%lld",&a[i]);
sum=0;
sum1=0;
for(i=0;i<n;i++){
if(i==0)
min1=a[0];
sum^=a[i];
sum1+=a[i];
if(a[i]<min1)
min1=a[i];
}
if(sum!=0)
printf("Case #%lld: NO\n",yash);
else printf("Case #%lld: %lld\n",yash,sum1-min1);
}
return 0;
}
