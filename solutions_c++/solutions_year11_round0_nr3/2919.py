#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <cmath>
#include <math.h>
using namespace std;
int ca,T,n;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    scanf("%d",&T);
    for (int ca=1;ca<=T;ca++)
    {
        int Min=1<<22,dif=0,sum=0;
        scanf("%d",&n);
        for (int i=0;i<n;i++)
        {
            int a;
            scanf("%d",&a);
            sum+=a;
            dif^=a;
            Min=min(Min,a);
        }
        if (dif) printf("Case #%d: NO\n",ca);
        else
        {
            printf("Case #%d: %d\n",ca,sum-Min);
        }
    }
    return 0;
}
