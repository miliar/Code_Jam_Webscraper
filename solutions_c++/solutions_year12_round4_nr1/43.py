#include <vector>
#include <string>
#include <algorithm>
#include <list>
#include <set>
#include <queue>
#include <stack>
#include <sstream>
#include <numeric>
#include <functional>
#include <utility>
#include <bitset>
#include <iostream>
#include <cmath>
#include <map>
using namespace std;



int d[100000], l[100000], dp[100000];

int main()
{
    freopen("input.txt","r", stdin);
    freopen("output.txt","w", stdout);
    
    int TT, n, D;
    scanf("%d", &TT);
    for (int T=1;T<=TT;++T)
    {
        scanf("%d", &n);

        for (int i=1;i<=n;++i)
            scanf("%d%d", d + i, l + i);
        scanf("%d", &D);
        
        memset(dp, 0, sizeof(dp));
        dp[1] = d[1];
        
        int j = 2;
        
        for (int i = 1; i <= n && i < j; ++ i)
        {
            while (d[j] - d[i] <= dp[i] && j <= n)
            {
                dp[j] = min(l[j], d[j] - d[i]);
                ++ j;
            }
        }
        
        bool flag = 0;
        for (int i = 1; i < j; ++ i)
            if (d[i] + dp[i] >= D)
                flag = 1;
        if (flag)
            printf("Case #%d: YES\n", T);
        else
            printf("Case #%d: NO\n", T);
    }
}
