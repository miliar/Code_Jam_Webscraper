#include <cstdio>
using namespace std;

int main ()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int T,N;
    scanf("%d",&T);
    for (int z=1;z<=T;++z)
    {
    scanf("%d",&N);
    int sum=0,xsum=0,min=2000000,x;
    for (int i=1;i<=N;++i)
    {
        scanf("%d",&x);
        sum+=x;
        xsum^=x;
        if (min>x) min=x;
    }
    if (!xsum) printf("Case #%d: %d\n",z,sum-min);
    else printf("Case #%d: NO\n",z);
    }
    return 0;
}
