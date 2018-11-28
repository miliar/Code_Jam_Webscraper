#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define N 1001
int r,k,n,g[N],next[N],flag[N];
long long num[N];
int main()
{
    int i,j,l,CASE=1,t,pre;
    long long temp,cycle,bpoint,blength,bsum;
    long long sum,stemp;
    FILE *in,*out;
    in=fopen("C-small-attempt0.in","r");
    out=fopen("C-small-attempt0.out","w");
    fscanf(in,"%d",&t);
    while(t--)
    {
              fscanf(in,"%d %d %d",&r,&k,&n);
              for(i=0; i<n; i++)
              fscanf(in,"%d",&g[i]);
              memset(flag,0,sizeof(flag));
              sum=0;
              i=0;
              j=0;
              pre=0;
              while(r--)
              {
                        while(j+g[i]<=k)
                        {
                                        j=j+g[i];
                                        i++;
                                        i=(i+n)%n;
                                        if(i==pre)break;
                        }
                        sum+=j;
                        pre=i;
                     //   printf("%d\n",sum);
                        j=0;
              }
                        
              fprintf(out,"Case #%d: %lld\n",CASE++,sum);
    }
    fclose(in);
    fclose(out);
   // system("pause");
    return 0;
}
    
