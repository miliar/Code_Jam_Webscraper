#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int main()
{
 FILE *fp1,*fp2;
 int t,i,n,a[4],j,u,s;
 char c;
 fp1=fopen("A-large.in","r");
 fp2=fopen("bottrust1.out","w");
 fscanf(fp1,"%d",&t);
 for(i=1;i<=t;i++)
 {
  fscanf(fp1,"%d",&n);
  fscanf(fp1,"%c",&c);
  a[0]=0;
  a[1]=1;
  a[2]=0;
  a[3]=1;
  s=0;
  for(j=0;j<n;j++)
  {
   fscanf(fp1,"%c",&c);
   fscanf(fp1,"%d",&u);
   if(c=='O')
   {
    if(((int)fabs(u-a[1])+a[0])<=s)
    {
     s=s+1;
     a[0]=s;
     a[1]=u;
    }
    else
    {
     s=(int)fabs(u-a[1])+a[0]+1;
     a[0]=s;
     a[1]=u;
    }
   }
   else if(c=='B')
   {
    if(((int)fabs(u-a[3])+a[2])<=s)
    {
     s=s+1;
     a[2]=s;
     a[3]=u;
    }
    else
    {
     s=(int)fabs(u-a[3])+a[2]+1;
     a[2]=s;
     a[3]=u;
    }
   }
   fscanf(fp1,"%c",&c);
  }
  fprintf(fp2,"Case #%d: %d\n",i,s);
 }
 fclose(fp1);
 fclose(fp2);
 return(0);
}
