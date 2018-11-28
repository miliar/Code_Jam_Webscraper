#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;
int t,n;
int a[1005];
int main()
{
//    freopen("C-large.in","r",stdin);
//    freopen("C-large.out","w",stdout);
    int i;
    scanf("%d",&t);
    int tem;
    int minn;
    int cases = 1;
    int sum;
    while(t--)
    {
        scanf("%d",&n);
        scanf("%d",&a[0]);
        tem = a[0];
        minn = a[0];
        sum = a[0];
        for(i=1;i<n;i++)
        {
            scanf("%d",&a[i]);
            tem ^= a[i];
            if(minn>a[i]) minn = a[i];
            sum += a[i];
        }
        if(tem) printf("Case #%d: NO\n",cases++);
        else
        {
            printf("Case #%d: %d\n",cases++,sum-minn);
        }
    }
	return 0;
}
