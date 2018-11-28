#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
int a[1000],b[1000];
int i,n;

bool cmp(int a,int b)
{
    return (a > b);
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int Test;
    scanf("%d",&Test);
    for (int T = 1; T <= Test; ++T)
    {
        scanf("%d",&n);
        for (i = 1; i <= n; ++i)
            scanf("%d",a+i);
        for (i = 1; i <= n; ++i)
            scanf("%d",b+i);
        sort(a+1,a+n+1);
        sort(b+1,b+n+1,cmp);
        long long ans = 0;
        for (i = 1;i <= n; ++i)
            ans += (long long)a[i] * (long long)b[i];
        printf("Case #%d: ",T);
        printf("%I64d\n",ans);
    }
    return 0;
}
