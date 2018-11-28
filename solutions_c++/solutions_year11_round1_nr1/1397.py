#include <cstdio>
int t,pd,pg,n,val,win;
int revisa()
{
    for (int i=1; i<=n; i++)
    {
        //n==100%,x=pd%
        int x=(i*pd);
        if ((x%100)==0)
        {
            x/=100;
            win=x;
            return(i);
        }
    }
    return(-1);
}
int revisa2()
{
    for (int i=val; i<=100; i++)
    {
        //i==100%, x=pg%
        int x=(i*pg);
        if ((x%100)==0)
        {
            x/=100;
            if (x>=win)
                return(i);
        }
    }
    return(-1);
}
int main()
{
    scanf("%d",&t);
    for (int i=1; i<=t; i++)
    {
        scanf("%d%d%d",&n,&pd,&pg);
        if (pd!=100 && pg==100)
            printf("Case #%d: Broken\n",i);
        else
        {
            val=revisa();
            if (val==-1)
                printf("Case #%d: Broken\n",i);
            else
            {
                val=revisa2();
                if (val==-1)
                    printf("Case #%d: Broken\n",i);
                else
                    printf("Case #%d: Possible\n",i);
            }
        }
    }
}
