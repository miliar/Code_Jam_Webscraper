#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

int n,num[1005],mark[1005][25];

int main()
{
    int i,j,k,t,T,r,ans;

    freopen("c.in","r",stdin);
    freopen("cnew.txt","w",stdout);

    scanf("%d",&T);

    for(t=1;t<=T;t++)
    {
        j=0;

        scanf("%d",&n);

        for(i=0;i<n;i++)
        {
            scanf("%d",&num[i]);

            if(i==0) k=num[i];

            else k=min(k,num[i]);

            j+=num[i];
        }

        r=j-k;

        for(i=0;i<n;i++)
        {
            k=num[i];

            for(j=0;j<25;j++)
            {
                mark[i][j]=k%2;
                k/=2;
            }
        }

        ans=1;

        for(j=0;j<25;j++)
        {
            k=0;
            for(i=0;i<n;i++) k+=mark[i][j];

            if(k%2)
            {
                ans=-1;
                break;
            }
        }

       if(ans==-1) printf("Case #%d: NO\n",t);

        else printf("Case #%d: %d\n",t,r);
    }

    return 0;
}
