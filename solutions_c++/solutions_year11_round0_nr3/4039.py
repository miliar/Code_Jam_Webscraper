#include<iostream.h>
#include<fstream.h>
#include<conio.h>
#include<math.h>
void l2b(long);
void sbadd();
long b2l();
long sp(long,long);
int ans[20];
int ans1[20];

void main()
{
clrscr();
int x=0,n=0,b[1000],temp1,temp2,count=0;
long seq[1000],sum1,sum2,asum1,asum2,large;
ifstream fin("test.txt");
ofstream fout("csmall.txt");
fin>>x;
while(count<x)
{
fin>>n;
for(int i=0;i<n;i++)
{
  b[i]=0;
  fin>>seq[i];
}
large=0;
for(int j=1;j<(pow(2,n)-1);j++)
{
   temp1=j;
   temp2=0;
   for(int p=0;i<n;i++)
     b[p]=0;
   while(temp1>0)
   {
     b[temp2]=temp1%2;
     temp1=temp1/2;
     temp2++;
   }
   sum1=0;
   sum2=0;
   asum1=0;
   asum2=0;
   for(int i=0;i<n;i++)
   {
      if(b[i]==0)
	sum1=sp(sum1,seq[i]);
      else
	sum2=sp(sum2,seq[i]);
   }
   if((sum1==sum2)&&(sum1>0)&&(sum2>0))
   {

     for(int i=0;i<n;i++)
     {
      if(b[i]==0)
	asum1=asum1+seq[i];
      else
	asum2=asum2+seq[i];
     }
     if(asum1>large)
       large=asum1;
     if(asum2>large)
       large=asum2;
   }
}
if (large==0)
  fout<<"Case #"<<count+1<<": "<<"NO\n";
else
  fout<<"Case #"<<count+1<<": "<<large<<"\n";
count++;
}
getch();
}

void l2b(long a)
{
  int i=0;
  while(a>0)
  {
    ans[i]=a%2;
    a=a/2;
    i++;
  }
  while(i!=20)
    ans[i++]=0;
}

void sbadd()
{
  for(int i=0;i<20;i++)
  {
    if(ans[i]==ans1[i])
      ans[i]=0;
    else
      ans[i]=1;
  }
}

long b2l()
{
  long a=0;
  for(int i=0;i<20;i++)
  {
     a=a+(ans[i]*pow(2,i));
  }
  return a;
}

long sp(long a,long b)
{
  long d;
  l2b(a);
  for(int i=0;i<20;i++)
  ans1[i]=ans[i];
  l2b(b);
  sbadd();
  d=b2l();
  return d;
}