#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int p(int n)
{
    int sum=0;
    while(n>0)
    {
        n/=10;
        sum++;
    }
    return sum;
}
int main()
{
    FILE *in=fopen("C-small-attempt0.in","r"),*out=fopen("out.out","w");
    int t;
    int pow[7]={1,10,100,1000,10000,100000,1000000};
    fscanf(in,"%d",&t);
    for(int i=1;i<=t;i++)
    {
        int a,b;
        fscanf(in,"%d%d",&a,&b);
        int sum=0;
        int r=p(a);
        for(int j=a;j<=b;j++)
        {
            for(int l=1;l<r;l++)
            {
                int tmp=j;
                tmp=tmp%pow[l]*pow[r-l]+tmp/pow[l];
                if(tmp>j&&tmp<=b) sum++;
            }
        }
        fprintf(out,"Case #%d: %d\n",i,sum);
    }
}
