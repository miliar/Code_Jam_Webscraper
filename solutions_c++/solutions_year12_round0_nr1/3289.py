#include<stdio.h>
int main()
{
    int i=0,t=0,n=0,s=0,p=0,ti,tmax[2],count=0;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        scanf("%d %d %d",&n,&s,&p);
        count=0;
        for(;n>0;n--)
        {
            scanf("%d",&ti);
            if(ti>=28||ti<=2)
            {
                if(ti>=28)
                {
                    tmax[0]=10;
                    tmax[1]=10;
                }
                if(ti==2)
                {
                    tmax[0]=1;
                    tmax[1]=2;
                }
                if(ti==1||ti==0)
                {
                    tmax[0]=ti;
                    tmax[1]=ti;
                }

            }
            if(ti<28&&ti>2)
            {
                if(ti%3==0)
                {
                    tmax[0]=ti/3;
                    tmax[1]=ti/3+1;
                }
                if(ti%3==1)
                {
                    tmax[0]=ti/3+1;
                    tmax[1]=ti/3+1;
                }
                if(ti%3==2)
                {
                    tmax[0]=ti/3+1;
                    tmax[1]=ti/3+2;
                }
            }
            if(tmax[0]>=p)
            {
                count++;
            }
            if(s>0&&tmax[0]<p&&tmax[1]==p)
            {
                count++;
                s--;
            }
        }
        printf("\nCase #%d: %d",i+1,count);
    }
    return 0;
}
