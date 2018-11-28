#include<stdio.h>
int main(){
int T,n,t,k,a;
scanf("%d",&T);
for(t=1;t<=T;t++){
scanf("%d%d",&n,&k);
a=(1<<n)-1;
if(k-a>=0&&(k-a)%(1<<n)==0)printf("Case #%d: ON\n",t);
else printf("Case #%d: OFF\n",t);
}
} 
