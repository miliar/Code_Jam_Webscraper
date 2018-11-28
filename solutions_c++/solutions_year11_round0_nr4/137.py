#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

const int maxn = 1024;

int n, cas;
double ans;

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    scanf("%d",&cas);
    for (int run = 1; run<=cas; run++ )
    {
        scanf("%d",&n);
        ans = 0;
        int a;
        for (int i = 1; i<=n; i++ )
        {
            scanf("%d",&a);
            if (a!=i) ans++; // f[i] = i , i > 1
        }
        printf("Case #%d: %.6lf\n",run,ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
