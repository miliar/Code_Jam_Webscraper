#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int p[20000],l[11000],f[11000];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int Cas,cas,n,d;
    scanf("%d",&Cas);
    for (int cas=1; cas<=Cas; cas++)
    {
        scanf("%d",&n);
        memset(f,-1,sizeof(f));
        for (int i=0; i<n; i++)
            scanf("%d%d",&p[i],&l[i]);
        scanf("%d",&d);
        int ans=0;
        if(p[0]<=l[0])
        {
            f[0]=p[0];
            if(f[0]>=d-p[0])
                ans=1;
            else
            {
                for(int i=0; i<n; i++)
                {
                    if(f[i]>=d-p[i])
                    {
                        ans=1;
                        break;
                    }
                    for(int j=i+1; j<n; j++)
                    {
                        if(f[i]<p[j]-p[i]) continue;
                        if(p[j]-p[i]<l[j]  && p[j]-p[i]>f[j]) f[j]=p[j]-p[i];
                        if(p[j]-p[i]>=l[j] && l[j]>f[j]) f[j]=l[j];
                    }
                }
            }

        }
        if(ans)
            printf("Case #%d: YES\n",cas);
        else
            printf("Case #%d: NO\n",cas);
    }
    return 0;
}
