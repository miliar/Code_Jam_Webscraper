#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    FILE *in=fopen("B-large.in","r"),*out=fopen("out.out","w");
    int t;
    fscanf(in,"%d",&t);
    for(int i=1;i<=t;i++)
    {
        int n,s,p,ti;
        int sum=0;
        fscanf(in,"%d%d%d",&n,&s,&p);
        for(int j=0;j<n;j++)
        {
            fscanf(in,"%d",&ti);
            if(ti>=3*p) sum++;
            else if(ti%3==2)
            {
                if(ti/3+1>=p)sum++;
                else if(ti/3+2>=p&&s>0){sum++;s--;}
            }
            else if(ti%3==1)
            {
                if(ti/3+1>=p)sum++;
            }
            else if(ti%3==0)
            {
                if(ti/3+1>=p&&s>0&&ti/3-1>=0){sum++;s--;}
            }
        }
        fprintf(out,"Case #%d: %d\n",i,sum);
    }
}
