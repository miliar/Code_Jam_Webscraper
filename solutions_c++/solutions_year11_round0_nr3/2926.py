#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string.h>

using namespace std;

int coin[20], n;
int tot;

int rec(int a, int b, int turn, int mask)
{
    int ret;
    if(turn>=n)
    {
        if(a==b)
        {
            int i, ans=0;
            for(i=0;i<n;i++)
            {
                if(mask&(1<<i))
                    ans += coin[i];
            }
            if(ans!=0 && ans!=tot)
                return max(ans, tot-ans);
        }
        return ret=0;
    }
    int c = coin[turn];
    int af = a^c;
    int bf = b^c;
    ret = max(rec(af, b, turn+1, (mask|(1<<turn))), rec(a, bf, turn+1, mask));
    return ret;
}

int main()
{
    freopen("C-small-attempt3.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int test, cas=1;
    scanf("%d", &test);
    while(test--)
    {
        int i, j;
        tot=0;
        scanf("%d", &n);
        for(i=0;i<n;i++)
        {
            scanf("%d", &coin[i]);
            tot+=coin[i];
        }
        int ans = rec(0, 0, 0, 0);
        if(ans==0)
            printf("Case #%d: NO\n", cas++);
        else
            printf("Case #%d: %d\n", cas++, ans);
    }
    return 0;
}
