#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int d[10000],l[10000],dp[10000];
int st[10000];
int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for (int cas=1;cas<=t;cas++)
    {
        int n,len;
        scanf("%d",&n);
        for (int i=0;i<n;i++)
            scanf("%d%d",&d[i],&l[i]);
        scanf("%d",&len);
        dp[0]=d[0];
        bool ans=(d[0]*2>=len);
        int top=1;
        st[0]=0;
        for (int i=1;i<n;i++)
        {
            int idx=st[top-1];
            if (d[idx]+dp[idx]<d[i])
            {
                dp[i]=-1;
                continue;
            }
            int le=0,ri=top-1;
            while (le<ri)
            {
                int mid=st[le+ri>>1];
                if (d[mid]+dp[mid]>=d[i])
                    ri=(le+ri)/2;
                else
                    le=(le+ri)/2+1;
            }
            dp[i]=min(d[i]-d[st[le]],l[i]);
            if (dp[i]+d[i]>dp[idx]+d[idx])
                st[top++]=i;
            if (dp[i]+d[i]>=len)
                ans=1;
        }
        printf("Case #%d: ",cas);
        if (ans)
            puts("YES");
        else
            puts("NO");
    }
    return 0;
}
