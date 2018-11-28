#include "stdio.h"
#include "stdlib.h"
#include "memory.h"
#include "assert.h"
#define DATA_SIZE 2000001

int group[DATA_SIZE];
int test[DATA_SIZE];

void build()
{
    int i = 0;
    int gid = 1;
    memset( group, 0, sizeof(group));
    for( i=1; i<DATA_SIZE; i++)
    {
        if( group[i] > 0 ) continue;
        bool ok = false;
        int p = i % 10;
        int s = i;
        int h = 1;
        while(s > 0)
        {
            if( p != (s%10))
            {
                ok = true;
            }
            s = s/10;
            h *= 10;
        }
        if( ok == false) continue;
        int l = 0;
        int k = 0;
        int t = 1;
        s = i;
        group[s] = gid;
        while( s > 0)
        {
            if( h == 10)
                break;
            h /= 10;
            if( s % 10 )
            {
                k = (s % 10) * t + k;
                s = s/10;
                int ss = h * k + s;
                if( ss < DATA_SIZE)
                {
                    group[ss] = gid;
                }
            }
            else
            {
                s = s/10;
            }
            t *= 10;
        }
        gid ++;
    }
    return ;
}

int main()
{
    build();
    int cas;
    //freopen("C-small.in", "r", stdin);
    //freopen("C-small.out", "w", stdout);
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    scanf("%d",&cas);
    int t = 0;
    while(cas--)
    {
        int i, a, b;
        scanf("%d %d",&a, &b);
        memset(test, 0, sizeof(test));
        for( i = a; i <= b; i++)
        {
            int gid = group[i];
            if( gid > 0)
                test[gid]++;
        }
        int sum = 0;
        for( i = 0; i <= DATA_SIZE; i++)
        {
            sum += ( test[i] * (test[i] - 1) )/ 2;
        }
        printf("Case #%d: %d\n",++t, sum);
    }
}