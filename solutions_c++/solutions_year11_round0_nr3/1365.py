#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;

int main()
{
    freopen("b.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    int n,i,j;
    scanf("%d",&t);
    int a[1005];
    int k;
    for(k = 1;k <= t;k ++)
    {
        scanf("%d",&n);
        int sum = 0;
        int temp = 0;
        for(j = 0;j < n;j ++)
        {
            scanf("%d",&a[j]);
            sum ^= a[j];
        }

        printf("Case #%d: ",k);
        if(sum == 0)
        {
            temp = 0;
            sort(a,a + n);
            for(i = 1;i < n;i ++)
            temp += a[i];
            printf("%d\n",temp);
        }
        else printf("NO\n");

    }
    return 0;
}
