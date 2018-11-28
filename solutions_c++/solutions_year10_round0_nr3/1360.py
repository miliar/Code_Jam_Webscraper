#include<iostream>

typedef unsigned long long ull;

using namespace std;

ull r, k, n;
ull t[1000];
ull memo[1000], qwe[1000];

ull g(ull a, ull x)
{
    if(x == r)
        return 0;
    ull i = a, sum = 0;
    do
    {
        sum += t[i++];
        i %= n;
    } while(i != a && sum + t[i] <= k);
    return sum + g(i, x + 1ull);
}

ull f(ull a, ull x)
{
    if(x == r)
        return memo[a];
    qwe[a] = x;
    ull i = a, sum = 0;
    do
    {
        sum += t[i++];
        i %= n;
    } while(i != a && sum + t[i] <= k);
    sum += memo[a];
    
    if(memo[i] == -1)
    {
        memo[i] = sum;
        return f(i, x + 1ull);
    }
    ++x;
    ull cl = x - qwe[i];
    ull cn = (r - x) / cl;
    ull cc = sum - memo[i];
    return memo[i] + cc * cn + cc + g(i, x + cn * cl);
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("task2.out.txt", "w", stdout);
    int T, Ti;
    scanf("%d", &T);
    for(Ti = 1; Ti <= T; ++Ti)
    {
        int i, j;
        scanf("%llu %llu %llu", &r, &k, &n);
        memset(memo+1, -1, n * 8 - 8);
        memset(qwe+1, -1, n * 8 - 8);
        for(i = 0; i < n; ++i)
            scanf("%llu", t+i);
        printf("Case #%d: %llu\n", Ti, f(0, 0));
    }
    return 0;
}
