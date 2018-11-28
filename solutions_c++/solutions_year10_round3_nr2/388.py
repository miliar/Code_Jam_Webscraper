#include <iostream>
using namespace std;
int t;
int l,p,c;
int main()
{
    int cnt1,cnt2,tmp1,tmp2;
    int ans,k;
    int i;
    freopen("B-large.in","r",stdin);
    freopen("b.out","w",stdout);
    while(scanf("%d",&t)!=EOF)
    {
        int case_t = 1;
        while(t--)
        {
            scanf("%d%d%d",&l,&p,&c);
            cnt1 = 0;
            if(p%c!=0)
                p = p/c + 1;
            else
                p = p/c;
            while(p>l)
            {
                cnt1++;
                if(p%c!=0)
                    p = p/c + 1;
                else
                    p = p/c;
            }
            if(cnt1 == 0)
                ans = 0;
            else{
            ans = 1;
            while(cnt1!=1)
            {
                cnt1/=2;
                ans++;
            }
            }
            printf("Case #%d: %d\n",case_t++,ans);
        }
    }
    return 0;
}
