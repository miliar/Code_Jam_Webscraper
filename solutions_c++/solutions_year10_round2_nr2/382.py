#include<stdio.h>
int at[10000],speed[10000],pass[10000];
int main()
{
    int C,n,m;
    scanf("%d",&C);
    for(n=0;n<C;n++)
    {
        int in,im,io,ip,toskip=0,ok=0,cost=0;
        scanf("%d %d %d %d",&in,&im,&io,&ip);
        for(m=0;m<in;m++)
            scanf("%d",&at[m]);
        for(m=0;m<in;m++)
            scanf("%d",&speed[m]);
        for(m=0;m<in;m++)
        {
            if(speed[m]*ip+at[m]>=io)
                pass[m]=1;
            else
                pass[m]=0;
            //printf("%d ",pass[m]);
        }
        for(m=in-1;m>=0;m--)
        {
            if(pass[m]==0)
                toskip++;
            else
            {
                ok++;
                cost+=toskip;
                if(ok>=im)
                    break;
            }
        }
        if(ok>=im)
        {
            printf("Case #%d: %d\n",n+1,cost);
        }
        else
        printf("Case #%d: IMPOSSIBLE\n",n+1);
    }
}
