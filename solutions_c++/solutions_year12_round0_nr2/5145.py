#include<iostream>
#include<algorithm>
using namespace std;

bool cmp(int x,int y)
{
    return x<y;
}
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int t,ans,n,s,p,tt;
    int a[150];
    scanf("%d",&t);
    for(int i = 1; i <= t; i++)
    {
        scanf("%d %d %d",&n,&s,&p);
        for(int j = 0; j < n; j++)
        {
            scanf("%d",&a[j]);
        }
        sort(a, a+n, cmp);
        ans = 0;
        for(int j = n-1; a[j] >= 3*p-4 && j >= 0; j--)
        {
            if(a[j] == 0)
            {
                if(p == 0)
                {
                    ans++;

                }
                continue;
            }
            if(a[j] % 3 == 0)
            {
                int tmp = a[j] / 3;
                if(tmp >= p)
                    ans++;
                else
                {
                    if(tmp+1 >= p && s)
                    {
                        ans++;
                        s--;
                    }
                }
            }
            else
            {
                int tmp = a[j] / 3 + 1;
                if(tmp >= p)
                    ans++;
                else
                {
                    if(a[j] % 3 == 2)
                    {
                        if(tmp+1 >= p && s)
                        {
                            ans++;
                            s--;
                        }
                    }
                }
            }
        }
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
