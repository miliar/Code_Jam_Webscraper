/*
    Title:
    Author: RudySnow
    Algorithm:
    Date:
    License:
    Quote: Night Gathers, and My Watch Begins, it shall Never End until My Death
*/

#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <memory.h>
#include <cstring>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <set>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>

using namespace std;

int weights[10];

int length(int x)
{
    int ans = 0;
    while(x > 0)
    {
        ++ans;
        x /= 10;
    }
    return ans;
}

int count(int a, int b, int n, int d)
{
    int i, tmp;
    set<int> s;
    for(i = 1; i < d; ++i)
    {
        tmp = n / weights[i] + ( n % weights[i] ) * weights[d - i];
        if (n < tmp && a <= tmp && tmp <= b) s.insert(tmp);
    }
    return s.size();
}

void Solve()
{
    int test, i, a, b, cas, n, ans;
    cas = 1;
    weights[0] = 1;
    for(i = 1; i < 10; ++i) weights[i] = weights[i-1] * 10;
    scanf("%d", &test);
    while(test--)
    {
        scanf("%d%d", &a, &b);
        ans = 0;
        n = length(a);
        for(i = a; i <= b; ++i)
        {
            ans += count(a, b, i, n);
        }
        printf("Case #%d: %d\n", cas, ans);
        cas++;
    }
}

int main()
{
    freopen( "C-large.in", "r", stdin );
    freopen( "C-large.out", "w", stdout );
    Solve();
    return 0;
}
