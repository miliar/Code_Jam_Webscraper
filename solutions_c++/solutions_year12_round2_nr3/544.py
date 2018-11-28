#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

#define INF 0x3fffffff
#define LL long long
const int N = 20;
const int M = (1 << 20);
int n, val[N], sum[M], bit[M];
void display(int mask)
{
    int i, j;
    for(i = 0, j = 0; i < n; i++)
    {
        if(mask & (1 << i))
        {
            if(j)   printf(" ");
            printf("%d", val[i]);
            j++;
        }
    }
    printf("\n");
}
int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int t, cas = 1, i, j;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d", &n);
        for(i = 0; i < n; i++)
        {
            scanf("%d", &val[i]);
        }
        for(i = 1; i < (1 << n); i++)
        {
            sum[i] = 0;
            bit[i] = 0;
            for(j = 0; j < n; j++)
            {
                if(i & (1 << j))
                {
                    sum[i] += val[j];
                    bit[i]++;
                }
            }
        }
        int flag = 0, seta, setb;
        for(i = 1; i < (1 << n); i++)
        {
            if(sum[i] & 1)  continue;
            for(j = (i - 1) & i; j > 0; j = (j - 1) & i)
            {
                if(sum[j] == sum[i] / 2)
                {
                    flag = 1;
                    seta = j;
                    setb = i ^ j;
                    break;
                }
            }
            if(flag)    break;
        }
        printf("Case #%d:\n", cas++);
        if(flag)
        {
            display(seta);
            display(setb);
        }
        else
        {
            printf("Impossible\n");
        }
    }
    return 0;
}
