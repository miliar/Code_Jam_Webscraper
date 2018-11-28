#include <stdio.h>

int main()
{
    int i,j,k,t,T,n,s,p,r,h,m;

    freopen("B-large.in","r",stdin);
    freopen("b-out.txt","w",stdout);

    scanf("%d",&T);

    for(t=1;t<=T;t++)
    {
        scanf("%d %d %d",&n,&s,&p);

        if(p==0)
        {
            h=0;
            m=0;
        }

        else if(p==1)
        {
            h=1;
            m=1;
        }

        else
        {
            h=3*p-2;
            m=3*p-4;
        }

        for(r=0,i=0;i<n;i++)
        {
            scanf("%d",&k);

            if( k >= h) r++;

            else if( k>=m && s) s--,r++;
        }

        printf("Case #%d: %d\n",t,r);
    }

    return 0;
}




