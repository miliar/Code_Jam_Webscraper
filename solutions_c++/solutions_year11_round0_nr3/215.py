#include<stdio.h>
#include<iostream>
using namespace std;
FILE *fpin=fopen("C-large.in","r");
FILE*fpout=fopen("c.out","w");
int a[1000];
int main()
{
   int i,j,n,m,k,l,o,p;
   fscanf(fpin,"%d",&p);
   for(o=1;o<=p;o++)
   { 
       memset(a,0,sizeof(a));
       fprintf(fpout,"Case #%d: ",o);
       fscanf(fpin,"%d",&n);
       int min=100000000;
       int sum=0;
       for(i=1;i<=n;i++)
       {
          fscanf(fpin,"%d",&k);
          if(k<min) min=k;
          sum+=k;
          j=0;
          while(k>0)
          {
             if(k%2==1) a[j]++;
             k/=2;
             j++;
          }
       }
       int flag=0;
       for(i=0;i<=100;i++)
        if(a[i]%2==1) flag=1;
       if(flag==1) fprintf(fpout,"NO\n");
       else fprintf(fpout,"%d\n",sum-min);
   }
   fclose(fpin);
   fclose(fpout);
}
