#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=0;cas<t;cas++)
    {
        int n;
        scanf("%d",&n);
        int d[10010],l[10010],len,avb[10010]={0};
        for(int i=0;i<n;i++)
        {
            scanf("%d%d",&d[i],&l[i]);
        }
        scanf("%d",&len);
        int ok=0;
        avb[0]=d[0];
        for(int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                if(d[j]-d[i]<=avb[i])
                {
                    avb[j]=max(avb[j],min(d[j]-d[i],l[j]));
                }
            }
            if(d[i]>=len-avb[i])
                ok=1;
         //   printf("%d\n",avb[i]);
        }
        if(ok)
            printf("Case #%d: YES\n",cas+1);
        else
            printf("Case #%d: NO\n",cas+1);
    }
    return 0;
}
