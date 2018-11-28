#include<cstdio>

int main(){
    int t,pd,pg;
    long long n;

    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        scanf("%lld %d %d",&n,&pd,&pg);
        int ch = 0;
        if(n<=100)
        {
            for(int j=1;j<=n;j++)
            {
                for(int k=0;k<=j;k++)
                {
                    double tt=(100.0*k)/j;
                    //printf("%lf - ",tt);
                    tt-=pd;
                    if(tt<0)    tt*=-1;
                    if(tt<10E-5)
                        ch=1;
                    //printf("%d %d %lf\n",j,k,tt);
                }
            }
        }else
        {
            ch=1;
        }
        if(!ch)
        {
            printf("Case #%d: Broken\n",i+1);
        }else
        {
            if((pg==100&&pd<100)||pg==0&&pd>0)
                printf("Case #%d: Broken\n",i+1);
            else
                printf("Case #%d: Possible\n",i+1);
        }
    }
    return 0;
}
