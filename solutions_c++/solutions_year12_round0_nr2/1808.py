#include <cstdio>
#include <algorithm>

using namespace std;

int t,tt,i,n,m,dig,num[1001],ans,coun1,coun2;

int main()
{
    //freopen("Dancing.in","r",stdin);
    //freopen("Dancing.out","w",stdout);
    scanf("%d",&tt);
    for (t = 1;t<=tt;t++)
    {
        scanf("%d%d%d",&n,&m,&dig);
        for (i = 1;i<=n;i++) scanf("%d",&num[i]);
        coun1=coun2=0;
        for (i = 1;i<=n;i++)
        {
            if (num[i]>=(dig-1)*3+1) coun1++; else
                if (num[i]>1 && num[i]>=dig*3-4) coun2++;
        }
        ans=coun1+min(m,coun2);
        printf("Case #%d: %d\n",t,ans);
    }
}
