#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;

int main ()
{
    int t,n;
    int a[1001];
    freopen("2.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(int i = 1;i <= t;++i)
    {
        scanf("%d",&n);
        int sum = 0;
        for(int k = 0;k < n;++k)
            scanf("%d",&a[k]),sum ^= a[k];
        if(sum)
        printf("Case #%d: NO\n",i);
        else
        {
            sort(a,a+n);
            for(int k = 1;k < n;++k)
                sum += a[k];
            printf("Case #%d: %d\n",i,sum);
        }
    }
    return 0;
}
