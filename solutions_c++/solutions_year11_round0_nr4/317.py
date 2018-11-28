#include <cstdio>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#define MAXN 1000
using namespace std;

int a[MAXN+1],b[MAXN+1];
int n;

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int i,j,c,t,cnt,ans;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        scanf("%d",&n);
        for(i=1;i<=n;i++)
        {
            scanf("%d",&a[i]);
        }
        memset(b,0,sizeof(b));
        ans=0;
        for(i=1;i<=n;i++)
        {
            if((a[i]!=i)&&(b[i]==0))
            {
                b[i]=1;
                cnt=1;
                for(j=a[i];j!=i;j=a[j])
                {
                    b[j]=1;
                    cnt++;
                }
                ans=ans+cnt;
            }
        }
        printf("Case #%d: %d.000000\n",c+1,ans);
    }
    return 0;
}
