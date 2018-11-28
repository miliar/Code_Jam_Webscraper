#include <cstdio>
using namespace std;

int main()
{
FILE *in = fopen("C-large.in","r");
FILE *out = fopen("C-large.out","w");
     
     long long a,b,t,n;
     fscanf(in,"%d",&t);
     
     for (long long i=0;i<t;i++)
     {
         n=0;
         fscanf(in,"%lld %lld",&a,&b);
         bool g[b+1];
         for (long long j=a;j<=b;j++)
             g[j]=false;
             
             printf("%lld %lld\n",a,b);
         
         long long tmp,rad;
         if (a<10) a=10;
         for (long long j=a;j<=b;j++)
             {
             rad=1;
             while (j>=rad) 
                   rad*=10;
             //rad/=10;     
                   
             tmp=j;
             tmp*=10;
             tmp=(tmp%rad)+(tmp/rad);
             
             g[j]=true;
             while(tmp!=j)
             {
                if ((tmp<=b)&&(tmp>=a)&&(tmp>=rad/10))
                   if (!g[tmp]) 
                      n++;

                
                tmp*=10;
                tmp=(tmp%rad)+(tmp/rad);
             }
             }
         
         fprintf(out,"Case #%lld: %lld\n",i+1,n);
     }
     
    return(0);
}
