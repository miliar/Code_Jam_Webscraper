#include <iostream>
#include <stdio.h>
using namespace std;
int main()
{
   freopen("B-large.in","r",stdin);
   freopen("xxx.out","w",stdout);
    int t,n,s,p,ans,ii=1;
    int a[200];
    cin>>t;
    while(t--)
    {
        cin>>n>>s>>p;
        ans=0;
        for(int i=0;i<n;i++)
        {
            cin>>a[i];
            if(a[i]>=3*p-2) ans++;
            else
            if(s)
            {
                if(a[i]>=3*p-4&&a[i]>=p)
                {
                    ans++;
                    s--;
                }
            }
        }
        printf("Case #%d: %d\n",ii++,ans);

    }
    return 0;
}
