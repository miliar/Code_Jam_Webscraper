#include<cstdio>

int t,n,k,i,num;

int main()
{
scanf("%d",&t);
for(i=1; i<=t; ++i)
   {
   scanf("%d%d",&n,&k);
   printf("Case #%d: ",i);
   if(k==0) {printf("OFF\n"); continue;}
   if(k%(1<<n)==((1<<n)-1)) printf("ON\n"); else printf("OFF\n");
   }
return 0;
}
