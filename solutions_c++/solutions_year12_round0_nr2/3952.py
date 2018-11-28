#include<stdio.h>
#include<stdlib.h>
int main(){


int t,n,s,p,x,i,res,j;

scanf("%d",&t);
for(i=1;i<=t;i++){
scanf("%d %d %d",&n,&s,&p);
res=0;
for(j=0;j<n;j++){
scanf("%d",&x);

if(x>=3*p-2)res++;
else if(s>0&&(x>=3*p-4)&&((x>0)||p==0)){
res++;s--;
}

}
printf("Case #%d: %d\n",i,res);

}
return 0;
}
