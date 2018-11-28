#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
 FILE *fp1,*fp2;
 int t,i,c,d,j,n,w,u,f,g,v,h;
 char a[37][4],x[29][3],z[1000],b;
 fp1=fopen("B-large.in","r");
 fp2=fopen("magicka4.out","w");
 fscanf(fp1,"%d",&t);
 for(i=1;i<=t;i++)
 {
  fscanf(fp1,"%d",&c);
  for(j=0;j<c;j++)
  {
   fscanf(fp1,"%s",a[j]);
  }
  fscanf(fp1,"%d",&d);
  for(j=0;j<d;j++)
  {
   fscanf(fp1,"%s",x[j]);
  }
  fscanf(fp1,"%d",&n);
  fscanf(fp1,"%c",&b);
  w=0;
  for(j=0;j<n;j++)
  {
   fscanf(fp1,"%c",&b);
   if(w==0)
   {
    z[w]=b;
    w=w+1;
   }
   else
   {
    f=0;
    for(u=0;u<c;u++)
    {
     if(((a[u][0]==z[w-1])&&(a[u][1]==b))||((a[u][0]==b)&&(a[u][1]==z[w-1])))
     {
      f=1;
      break;
     }
    }
    if(f==1)
    {
     w=w-1;
     z[w]=a[u][2];
     w=w+1;
    }
    else if(f==0)
    {
     g=0;
     for(u=0;u<d;u++)
     {
      if(x[u][0]==b)
      {
       h=0;
       for(v=0;v<w;v++)
       {
        if(x[u][1]==z[v])
        {
         h=1;
         break;
        }
       }
       if(h==1)
       {
        g=1;
        break;
       }
      }
      else if(x[u][1]==b)
      {
       h=0;
       for(v=0;v<w;v++)
       {
        if(x[u][0]==z[v])
        {
         h=1;
         break;
        }
       }
       if(h==1)
       {
        g=1;
        break;
       }
      } 
     }
     if(g==1)
     w=0;
     else if(g==0)
     {
      z[w]=b;
      w=w+1;
     }
    }
   }
  }
  if(w==0)
  {
   fprintf(fp2,"Case #%d: []\n",i);
   continue;
  }
  if(w==1)
  {
   fprintf(fp2,"Case #%d: [%c]\n",i,z[0]);
   continue;
  }
  fprintf(fp2,"Case #%d: [%c,",i,z[0]);
  for(j=1;j<(w-1);j++)
  {
   fprintf(fp2," %c,",z[j]);
  }
  fprintf(fp2," %c]\n",z[j]);
 }
 fclose(fp1);
 fclose(fp2);
 return(0);
}
