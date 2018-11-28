#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("4.in","r",stdin);
    freopen("4.out","w",stdout);
    int c,cs,n,ans,i,x;
    cin>>cs;
    for (c=1;c<=cs;c++)
    {
        cin>>n;
        ans=0;
        for (i=1;i<=n;i++)
        {
            cin>>x;
            if (x!=i) ans++;
        }
        printf("Case #%d: %d.000000\n", c, ans);
    }
    return 0;
}
