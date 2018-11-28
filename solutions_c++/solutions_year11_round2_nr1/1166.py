#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
 FILE *fp1,*fp2;
 int t,i,n,j,u,s,s1,v,z;
 double x[101][3],y;
 char a[101][101];
 fp1=fopen("A-large.in","r");
 fp2=fopen("code3.out","w");
 fscanf(fp1,"%d",&t);
 for(i=1;i<=t;i++)
 {
  fscanf(fp1,"%d",&n);
  for(j=0;j<n;j++)
  {
   fscanf(fp1,"%s",a[j]);
  }
  for(j=0;j<n;j++)
  {
   s=0;
   s1=0;
   for(u=0;u<n;u++)
   {
    if((a[j][u]=='0')||(a[j][u]=='1'))
    {
     if(a[j][u]=='1')
     s1=s1+1;
     s=s+1;
    }
   }
   x[j][0]=((float)s1/(float)s);
  }
  for(j=0;j<n;j++)
  {
   z=0;
   y=0.0;
   for(u=0;u<n;u++)
   {
    if((a[u][j]=='0')||(a[u][j]=='1'))
    {
     s=0;
     s1=0;
     for(v=0;v<n;v++)
     {
      if(((a[u][v]=='0')||(a[u][v]=='1'))&&(v!=j))
      {
       if(a[u][v]=='1')
       s1=s1+1;
       s=s+1;
      }
     }
     y=y+((float)s1/(float)s);
     z=z+1;
    }
   }
   x[j][1]=(y/(float)z); 
  }
  for(j=0;j<n;j++)
  {
   z=0;
   y=0.0;
   for(u=0;u<n;u++)
   {
    if((a[u][j]=='0')||(a[u][j]=='1'))
    {
     y=y+x[u][1];
     z=z+1;
    }
   }
   x[j][2]=(y/(float)z);
  }
  fprintf(fp2,"Case #%d:\n",i);
  for(j=0;j<n;j++)
  {
   fprintf(fp2,"%.8f\n",(0.25*x[j][0]+0.50*x[j][1]+0.25*x[j][2]));
  }
 } 
 fclose(fp1);
 fclose(fp2);
 return(0);
}
 
