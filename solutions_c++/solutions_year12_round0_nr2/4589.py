#include<cstdio>
using namespace std;
int main()
{
    //freopen("BB.in","r",stdin);
    //freopen("BBB.out","w",stdout);
    int t,n,s,p,a,ans;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        ans=0;
        printf("Case #%d: ",i);
        scanf("%d%d%d",&n,&s,&p);
        if(p==0)
        {
            for(int j=0;j<n;j++)
                scanf("%d",&a);
            printf("%d\n",n);
            continue;
        }
        for(int j=0;j<n;j++)
        {
            scanf("%d",&a);
            if(!a)continue;
            if(a==1)
            {
                if(a>=p)
                    ans++;
                continue;
            }
            if(a/3>=p)
            {
                ans++;
                continue;
            }
            if(a%3==0)
            {
                if(s&&(a/3+1>=p))
                {
                    ans++;
                    s--;
                }
                continue;
            }
            if(a/3+1>=p)
            {
                ans++;
                continue;
            }
            if(s&&(a%3==2)&&a/3+2>=p)
            {
                ans++;
                s--;
                continue;
            }
        }
        printf("%d\n",ans);
    }
}
