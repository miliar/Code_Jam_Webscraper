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

// 记得初始化，记得long long 

int d[10000], q[10000], l[10000];

bool cmp(int i, int j)
{
// d[i]/l[i] > d[j]/l[j]
    if (d[i] * l[j] == d[j] * l[i])
        return i < j;
    else
        return d[i] * l[j] > d[j] * l[i];
}

int main()
{
    freopen("input.txt","r", stdin);
    freopen("output.txt","w", stdout);
    
    int TT, n;
    scanf("%d", &TT);
    for (int T=1;T<=TT;++T)
    {
        scanf("%d", &n);
        for (int i = 0; i < n; ++ i)
            scanf("%d", l+i);
        for (int i = 0; i < n; ++ i)
            scanf("%d", d+i);
        for (int i = 0; i < n; ++ i)
            q[i] = i;
        sort(q, q+n, cmp);
        printf("Case #%d:", T);
        for (int i = 0; i < n; ++ i)
            printf(" %d", q[i]);
        printf("\n");
    }
}
