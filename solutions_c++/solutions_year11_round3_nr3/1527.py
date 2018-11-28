#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
 FILE *fp1,*fp2;
 int t,i,n,u,v,a[100],j,w,f;
 fp1=fopen("C-small-attempt0.in","r");
 fp2=fopen("harmony.out","w");
 fscanf(fp1,"%d",&t);
 for(i=1;i<=t;i++)
 {
  fscanf(fp1,"%d%d%d",&n,&u,&v);
  for(j=0;j<n;j++)
  {
   fscanf(fp1,"%d",&a[j]);
  }
  for(j=u;j<=v;j++)
  {
   f=0;
   for(w=0;w<n;w++)
   {
    if(((j%a[w])!=0)&&((a[w]%j)!=0))
    {
     f=1;
     break;
    }
   }
   if(f==0)
   break;
  }
  if(f==0)
  fprintf(fp2,"Case #%d: %d\n",i,j);
  else
  fprintf(fp2,"Case #%d: NO\n",i);
 }
 fclose(fp1);
 fclose(fp2);
 return(0);
}
