#include<stdio.h>
char A[109][109],B[109][109];
long cas,cas1,i,j,time,r,r1,x1,x2,y1,y2,flag;

int main()
{

  freopen("C-small-attempt0.in","r",stdin);
  freopen("C-small-out.out","w",stdout);

scanf("%ld",&cas);

for(cas1=1;cas1<=cas;cas1++)
{
for(i=0;i<=101;i++)
for(j=0;j<=101;j++)
{
A[i][j]='0';
B[i][j]='0';
}

scanf("%ld",&r);

for(r1=1;r1<=r;r1++)
{
scanf("%ld %ld %ld %ld",&x1,&y1,&x2,&y2);

for(i=x1;i<=x2;i++)
for(j=y1;j<=y2;j++)
A[i][j]='1';
}
time=0;
while(1)
{
flag = 0;

for(i=1;i<=100;i++)
for(j=1;j<=100;j++)
if(A[i][j]=='1')
flag = 1;

if(flag == 0)
break;

time++;

for(i=1;i<=100;i++)
for(j=1;j<=100;j++)
{
if(A[i][j]=='1')
{
if(A[i-1][j]=='1'||A[i][j-1]=='1')
B[i][j]='1';
else
B[i][j]='0';
}
else
{
if(A[i-1][j]=='1' && A[i][j-1]=='1')
B[i][j]='1';
else
B[i][j]='0';
}
}

for(i=1;i<=100;i++)
for(j=1;j<=100;j++)
A[i][j]=B[i][j];

}


printf("Case #%ld: %ld\n",cas1,time);


}

return 0;
}
