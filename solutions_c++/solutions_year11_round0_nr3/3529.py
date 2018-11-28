#include <stdio.h>
#include <cstring>
#include <algorithm>
using namespace std;

int main()
{
    int test, cas(1), n, a, t, sum, Min;
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    scanf("%d",&test);
    while(test--)
    {
        scanf("%d",&n);
        t = 0;  sum = 0;  Min = 10000000;
        for(int i = 1; i <= n; ++i)
        {
            scanf("%d",&a);
            t ^= a;
            Min = min(Min,a);
            sum += a;
        }
        if(t == 0)  printf("Case #%d: %d\n",cas++,sum-Min);
        else   printf("Case #%d: NO\n",cas++);
    }
    return 0;
}
