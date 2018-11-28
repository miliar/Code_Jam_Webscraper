#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int a[1024], b[1024];

int T=0, n=0;

int main()
{
    int t;
    scanf("%d", &T);
    for (t=1;t<=T;t++)
    {
        scanf("%d", &n);
        for (int i=0;i<n;i++)
        {
            scanf("%d%d", &a[i], &b[i]);
        }

        int sum = 0;
        for (int i=0;i<n;i++)
        {
            for (int j=i+1;j<n;j++)
            {
                if ((a[i]-a[j]>0 && b[i]-b[j]<0)||(a[i]-a[j]<0 && b[i]-b[j]>0)) sum++;
            }
        }
        printf("Case #%d: %d\n", t, sum);
    }
    return 0;
}
