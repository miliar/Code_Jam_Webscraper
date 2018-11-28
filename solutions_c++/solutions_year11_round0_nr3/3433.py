#include <iostream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;
int a[1000];
int main()
{
    int tc,n;
  //  freopen("C-large.in", "r", stdin);
   // freopen("output.txt", "w", stdout);
    scanf("%d", &tc);
    for (int cas=1;cas<=tc;++cas)
    {
        scanf("%d", &n);
        int x = 0, sum=0;
        for (int i=0;i<n;++i) scanf("%d", &a[i]), x^=a[i], sum+=a[i];
        if (x==0)
        {
                sort(a,a+n);
                printf("Case #%d: %d\n", cas, sum-a[0]);
        }
        else
        {
            printf("Case #%d: NO\n", cas);
        }
    }
    return 0;
}
