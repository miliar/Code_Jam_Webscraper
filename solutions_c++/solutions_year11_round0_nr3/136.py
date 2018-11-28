#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

const int maxn = 1024;
const int inf  = 1000000000;

int cas;

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    scanf("%d",&cas);
    for (int run = 1; run<=cas; run++ )
    {
        int Sum = 0, minValue = inf, n, x, Sx = 0;
        for (scanf("%d",&n); n--; )
        {
            scanf("%d",&x);
            Sx ^= x;
            Sum += x;
            if (x<minValue) minValue = x;
        }
        if (Sx) printf("Case #%d: NO\n",run);
        else printf("Case #%d: %d\n",run,Sum-minValue);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
