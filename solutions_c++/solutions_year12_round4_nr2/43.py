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



int r[100000], q[100000], ansX[100000], ansY[100000];

bool cmp(int i, int j)
{
    return r[i] > r[j];
}

int main()
{
    freopen("input.txt","r", stdin);
    freopen("output.txt","w", stdout);
    
    int TT, n, W, L;
    scanf("%d", &TT);
    for (int T=1;T<=TT;++T)
    {
        scanf("%d %d %d", &n, &W, &L);

        for (int i=0;i<n;++i)
            scanf("%d", r + i);
        
        for (int i=0;i<n;++i)
            q[i] = i;
        
        sort(q, q+n, cmp);
        
        int sum = - r[q[0]], h = 0, nexth = r[q[0]];
        for (int i = 0; i < n; ++ i)
        {
            int R = r[q[i]];
            if (sum + R > W)
            {
                h = nexth + R;
                nexth = h + R;
                sum = R;
            }
            else
                sum = sum + R + R;
            ansX[q[i]] = sum - R;
            ansY[q[i]] = h;
        }
        
        if (h <= L)
        {
            printf("Case #%d:", T);
            for (int i = 0; i < n; ++ i)
                printf(" %d %d", ansX[i], ansY[i]);
            printf("\n");
        }
        else
            printf("Case #%d: NO\n", T);
    }
}
