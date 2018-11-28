#include<stdio.h>
#include<algorithm>
using namespace std;
int main(){
    freopen("B-large.in","r",stdin);
   	freopen("out.out","w",stdout);
int t,s,p,i,c=0,j,k,n,f=0,y=0;
float temp;
scanf("%d",&t);
for(i=1;i<=t;i++){
    c=0;
scanf("%d %d %d",&n,&s,&p);
int goog[n];
for(j=0;j<n;j++)
scanf("%d",&goog[j]);
sort(goog,goog+n);
    y=0;
f=0;
for(k=0;k<n;k++){
    if(goog[k]>=p){
temp=goog[k]-p;
temp=temp/2;
if(f==1)
c++;
else if(temp>=p-1&&temp>=0){
c++;
f=1;
y=goog[k];
}
else if(temp>=p-2&&s>0&&temp>=0){
c++;
s--;
}}
}
printf("Case #%d: %d",i,c);
printf("\n");
}
return 0;
}
