#include <iostream>
#include <fstream>
#include <cstring>
#include <climits>
#include <cstdio>
#include <cmath>
#include <algorithm>




using namespace std;

typedef long long LL;


LL gcd(LL a, LL b)
{
    LL tmp;

    while(b)
    {
        tmp = a % b;
        a = b;
        b = tmp;
    }

    return a;
}

LL lcm(LL a, LL b)
{
    return a * b /gcd( a, b);
}

LL Max(LL a, LL b)
{
    if(a > b)
    return a;
    return b;
}

LL Min(LL a, LL b)
{
    if(a < b)
    return a;
    return b;
}


LL prime[2100000];
int cnt;

bool vis[2100000];

LL record[2100000];

void init()
{
    for(LL i = 2; i <= 1500010; i++)
    {
        if(vis[i])
        continue;
        prime[cnt++] = i;
        for(LL j = 1; j <= 1500010 / i; j++)
        {
            vis[i * j] = true;
        }
    }
//    for(int i =0; i < cnt; i++)
//    {
//        printf("%I64d\n",prime[i]);
//    }
}



int main()
{
    freopen("C-large (1).in", "r", stdin);
//freopen("input.txt", "r", stdin);
    freopen("output.out", "w", stdout);
    init();


    int T;
    scanf("%d", &T);
    LL N;
    LL a, b;
    for(int loop = 1; loop <= T; loop++)
    {
        scanf("%I64d", &N);
        if(N == 1)
        {
            printf("Case #%d: %I64d\n", loop, 0LL);
            continue;
        }

        memset(record, 0, sizeof(record));

        for(int i = 0; i < cnt; i++)
        {
            LL tmp = N;
            while(tmp >= prime[i])
            {
                record[i]++;
                tmp /= prime[i];
            }
        }
        a = 1 , b= 0;
        for(int i = 0; i < cnt; i++)
        {
            if(record[i])
            {
                a += record[i];
                b++;
            }
            else
            break;
        }

        LL res = a - b;
        printf("Case #%d: %I64d\n", loop, res);


    }
















    return 0;
}
