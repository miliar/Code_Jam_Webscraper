#include <stdio.h>
#include <cstring>
#include <iostream>

using namespace std;

const int V = 20000;

long long n, D;
long long d[V], I[V];
long long f[V];

int main()
{
    int test;
    scanf("%d",&test);
    for (long long cas=1;cas<=test;cas++)
    {
        cin >> n;
        for (int i=0;i<n;i++)
            cin >> d[i] >> I[i];
        cin >> D;
        
        memset(f, 0, sizeof(f));
        f[0] = d[0];
        int now = 1;
        for (int i=0;i<n;i++)
        {
            for (int j=now;j<n;j++)
            if (d[j] - d[i] <= f[i])
            {
                f[j] = max(f[j], min(I[j], d[j] - d[i]));
                now = j+1;
            }
        }
        bool find = false;
        for (int i=0;i<n;i++)
        if (f[i] + d[i] >= D)
        {
            find = true;
            break;
        }
        printf("Case #%d: ",cas);
        if (find)
            puts("YES");
        else
            puts("NO");
    }
}
