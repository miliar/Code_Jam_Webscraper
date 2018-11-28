#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

long long n, k;
long long Num;

long long Exp(long long a, long long r)
{
    long long ret = 1;

    while(r)
    {
        if(r & 1)
            ret *= a;
        a *= a;

        r >>= 1;
    }

    return ret;
}

bool check(int r)
{
    int ret = 0;
    while(r)
    {
        if(r & 1)
            ret ++;
        r >>= 1;
    }

    if(ret == n)
        return true;

    return false;
}

int main()
{
    int T;
    scanf("%d", &T);

    for(int t = 1; t <= T; t ++)
    {
        printf("Case #%d: ", t);
        scanf("%I64d %I64d", &n, &k);
        Num = Exp(2, n);
        k %= Num;

        if(check(k))
            printf("ON\n");
        else
            printf("OFF\n");
    }

    return 0;
}
