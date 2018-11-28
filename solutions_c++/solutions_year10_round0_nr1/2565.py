#include<stdio.h>
int main()
{
freopen("1.in","r",stdin);
freopen("1.out","w",stdout);
int t,n,k;
int min,num;
scanf("%d",&t);
num=1;
while(t--)
{
scanf("%d%d",&n,&k);
min=(1<<n)-1;
if ( (k-min)%(min+1) == 0 )
		printf("Case #%d: ON\n",num);
else
		printf("Case #%d: OFF\n",num);
num++;
}
return 0;
}