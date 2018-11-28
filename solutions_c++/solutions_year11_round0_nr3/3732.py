#include<stdio.h>
#include<algorithm>
using namespace std;
FILE *f1=fopen("C-large can.in","r");
FILE *f2=fopen("Candysp.out","w");
int ar[1005];
int main()
{
    int t,a,n,i,sum=0,xs=0,mn=10000000;
    fscanf(f1,"%d",&t);
    for(a=1;a<=t;a++)
    {
      fscanf(f1,"%d",&n);
      xs=0;
      sum=0;
      mn=10000000;
      for(i=0;i<n;i++)
      {
       fscanf(f1,"%d",&ar[i]);
       xs=xs^ar[i];
       sum+=ar[i];
       mn=min(mn,ar[i]);
      }
      if(xs != 0)
       fprintf(f2,"Case #%d: NO\n",a);
      else
       fprintf(f2,"Case #%d: %d\n",a,sum-mn);       
      
    }
    //scanf("%*d");
}
