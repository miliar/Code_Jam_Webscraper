#include <stdio.h>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>

using namespace std;


int add(int a,int b)
{
    int ans=0,p=1;
    while (a || b)
    {
        ans+=p*(((a&1)+(b&1))&1);
        p*=2;
        a>>=1;
        b>>=1;
    }
    return ans;
}

int main()
{
    freopen("ccin","r",stdin);
    freopen("ccout","w",stdout);
    int i,t,cas,j,n,data[1000];
    scanf("%d",&t);
    for (cas=1; cas<=t; cas++)
    {
        scanf("%d",&n);
        for (i=0; i<n; i++)
        {
            scanf("%d",&data[i]);
        }
        int ans=-1;
        for (i=1; i<(1<<n)-1; i++)
        {
            int p1,p2,v1,v2;
            p1=p2=v1=v2=0;
            for (j=0; j<n; j++)
            {
                if ((i>>j)&1)
                {
                    p1=add(p1,data[j]);
                    v1+=data[j];
                    continue;
                }
                p2=add(p2,data[j]);
                v2+=data[j];
            }
            if (p1==p2) ans=max(ans,max(v1,v2));
        }
        if (ans==-1) printf("Case #%d: NO\n",cas);
        else printf("Case #%d: %d\n",cas,ans);
    }
	return 0;
}

