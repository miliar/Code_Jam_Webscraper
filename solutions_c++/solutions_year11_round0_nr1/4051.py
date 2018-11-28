#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;

int main()
{
FILE *fp1,*fp2;

char ch,sp;
int n,T,l,i,pos;
int oldp1,curp1,oldp2,curp2;
int time=0,count1=0,count2=0;
fp1=fopen("A-large.in","r");
fp2=fopen("A-large.out","w");
fscanf(fp1,"%d",&T);
for (i=1;i<=T;i++)
{
fscanf(fp1,"%d",&n);
fscanf(fp1,"%c",&ch);
curp1=curp2=1;
oldp1=oldp2=0;

time=0;
count1=0,count2=0;
for (l=1;l<=n;l++)
{
fscanf(fp1,"%c",&ch);
fscanf(fp1,"%d",&pos);

if (ch=='O')
{
count1=((fabs(pos-curp1))+oldp1);
if (count1<=time)
{
time++;
oldp1=time;
curp1=pos;}
else
{
time=count1+1;
oldp1=time;
curp1=pos;
}
}
else if (ch=='B')
{
count2=((fabs(pos-curp2))+oldp2);
if (count2<=time)
{
time++;
oldp2=time;
curp2=pos;
}
else
{
time=count2+1;
oldp2=time;
curp2=pos;
}
}
fscanf(fp1,"%c",&sp);
}
fprintf(fp2,"Case #%d: %d\n",i,time);
}
fclose(fp1);
fclose(fp2);
return 0;
}


