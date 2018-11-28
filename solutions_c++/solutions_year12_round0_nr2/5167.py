#include<stdio.h>
#include<stdlib.h>
int main(){
 
int t,n,s,p,x,i,result,j;
 
scanf("%d",&t);
for(i=1;i<=t;i++){
scanf("%d %d %d",&n,&s,&p);
result=0;
for(j=0;j<n;j++){
scanf("%d",&x);
 
if(x>=3*p-2)result++;
else if(s>0&&(x>=3*p-4)&&((x>0)||p==0)){
result++;s--;
}
 
}
printf("Case #%d: %d\n",i,result);
 
}
return 0;
}
