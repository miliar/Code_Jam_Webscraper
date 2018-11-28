#include <iostream>
#include <cstring>
using namespace std;

int n,a;

int main()
{
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++)
    {
        scanf("%d",&n);
        int min=2147483647,sum=0,x=0;
        for (int i=1;i<=n;i++)
        {
            scanf("%d",&a);
            sum+=a; x^=a; min<?=a;
        }
        printf("Case #%d: ",cas);
        if (x==0) printf("%d\n",sum-min);
        else printf("NO\n");
    }
    return 0;
}
