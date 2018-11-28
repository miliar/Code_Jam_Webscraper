#include<stdio.h>
#include<conio.h>
int main()
{
int t,n,sur,req,num,count=0,sur2=0,i,j,chk,surchk,clv;
scanf("%d",&t);
for(i=0;i<t;i++)
{
scanf("%d",&n);
scanf("%d",&sur);
scanf("%d",&req);
clv=req-2;
surchk=req-4;
count=0;
sur2=0;
 
for(j=0;j<n;j++)
{
scanf("%d",&num);
chk=num/req;
if(chk>=3)
count++;
else if(chk==2)
        {
        if((num%req)>=clv)
        count++;
        else if((num%req)>=surchk)
        sur2++;
        }
}
if(sur>=sur2)
count+=sur2;
else if(sur2>sur)
count+=sur;
printf("Case #%d: %d",i+1,count);
}
return 0;
getch();
}
