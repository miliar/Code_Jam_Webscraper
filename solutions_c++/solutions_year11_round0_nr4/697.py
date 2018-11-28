#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int a[1002];
int main()
{
    freopen("data.in","r",stdin);
    freopen("out.txt","w",stdout);
    int n,i,k,t,sum;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        scanf("%d",&n);
        for(i=1;i<=n;i++)
        scanf("%d",&a[i]);
        if(n == 1) printf("Case #%d: 0.000000\n",k);
        else
        {
            sum = 0;
            for(i=1;i<=n;i++)
            {
                if(a[i] == i) sum++;
            }
            printf("Case #%d: %d.000000\n",k,n-sum);
        }
    }
    return 0;
}
