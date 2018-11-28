#include <cstdio>
using namespace std;

int main()
{
FILE *in = fopen("B-large.in","r");
FILE *out = fopen("B-large.out","w");

   int t,n,s,p;
   fscanf(in,"%d",&t);
   
   int a[100];
   
   for (int i=0;i<t;i++)
   {
       fscanf(in,"%d %d %d",&n,&s,&p);
       for (int j=0;j<n;j++)
           fscanf(in,"%d",&a[j]);
           
       int ok=0;
       for (int j=0;j<n;j++)
           {
           int prva=3*p-2;
           int druha=3*p-4;
           if (p==1) druha=1;
           if (p==0) prva=0;
           
           if (a[j]>=prva) ok++;
           else if (a[j]>=druha) 
                {
                if (s>0)
                   {
                   s--;
                   ok++;
                   }
                }
           }
       
       fprintf(out,"Case #%d: %d\n",i+1,ok);
   }
    
    fclose(out);
    return(0);
}
