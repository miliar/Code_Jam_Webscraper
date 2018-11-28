#include <stdio.h>
int t[110];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int ii=1;ii<=T;ii++)
    {
        int n,s,p;
        scanf("%d%d%d",&n,&s,&p);
        int ans=0;
        for (int i=0;i<n;i++)
        {
            scanf("%d",&t[i]);
            if (t[i]%3==1)
            {
                if (t[i]/3+1>=p) ans++;
            }
            else if (t[i]%3==2)
            {
                if (t[i]/3+1>=p) ans++;
                else if (t[i]/3+2>=p&&s>0)
                {
                    s--;
                    ans++;
                }
            }
            else
            {
                if (t[i]/3>=p) ans++;
                else if (t[i]!=0&&t[i]/3+1>=p&&s>0)
                {
                    s--;
                    ans++;
                }
            }
        }
        printf("Case #%d: %d\n",ii,ans);
    }
    return 0;
}
