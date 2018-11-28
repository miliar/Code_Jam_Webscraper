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



int d[100000], a[100000], tmp[10000];
int LIMIT = 1000000000;
bool flag;

int cal(long long A, long long B, long long C)
{
    long long R;
    R = a[B] * (C - A) - a[C] * (B - A);
    return R / (C - B);
}

void solve(int l, int r, int rr)
{
    if (l == r)
        return;
    int m = 0;
    tmp[0] = l;
    while (tmp[m] < r)
    {
        tmp[m + 1] = d[tmp[m]];
        ++ m;
    }
    
    if (tmp[m] > r)
    {
        flag = 0;
        return;
    }
    
    --a[l - 1];
    a[tmp[m - 1]] = min(cal(tmp[m - 1], l - 1, tmp[m]), cal(tmp[m - 1], tmp[m], rr));
    ++a[l - 1];

    for (int i = m-2; i>=0; -- i)
        a[tmp[i]] = cal(tmp[i], tmp[i+1], tmp[i+2]);

    for (int now = l; now < r; now = d[now])
    {
        int next1 = d[now], next2;
        if (next1 == r)
            next2 = rr;
        else
            next2 = d[next1];
        solve(now + 1, next1, next2);
    }    
}

int main()
{
    freopen("input.txt","r", stdin);
    freopen("output.txt","w", stdout);
    
    int TT, n, D;
    scanf("%d", &TT);
    for (int T=1;T<=TT;++T)
    {
        scanf("%d", &n);
        for (int i=1;i<n;++i)
            scanf("%d", d + i);

        a[0] = LIMIT + 1;
        a[n] = a[n+1] = LIMIT;
        
        flag = 1;
        solve(1, n, n + 1);
        
        if (flag)
        {
            printf("Case #%d:", T);
            for (int i = 1; i<=n; ++ i)
                printf(" %d", a[i]);
            printf("\n");
        }
        else
            printf("Case #%d: Impossible\n", T);
    }
}
