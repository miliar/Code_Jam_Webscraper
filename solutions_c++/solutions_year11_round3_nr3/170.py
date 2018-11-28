#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int prime[10010];
int table[10010];
int mark[10010];
int list[2][10010];
int pc;

void init()
{
    int i, j;
    memset(table,0,sizeof(table));
    pc = 0;
    table[0] = table[1] = 1;
    for ( i = 2; i <= 10000; i++ ) {
        if ( table[i] ) continue;
        prime[pc++] = i;
        for ( j = i*i; j <= 10000; j+=i )
            table[j] = 1;
    }
}

int n, l, h;
int ans;

int main()
{
    int aa, nn, i, t, j, c, pre, cur, tc;
    scanf("%d",&nn);
    for ( aa = 1; aa<= nn; ++aa ) {
        scanf("%d %d %d",&n,&l,&h);
        ans = l; c = 0;
        for ( i = 0, j = l; j <= h; j++, i++ ) {
            list[0][c++] = j;
        }
        pre = 0; cur = 1;
        for ( i = 0; i < n; i++ ) {
            scanf("%d",&t);
            tc = 0;
            for ( j = 0; j < c; j++ ) {
                if ( list[pre][j] % t == 0 || t % list[pre][j] == 0)
                    list[cur][tc++] = list[pre][j];
            }
            c = tc;
            pre = cur;
            cur = 1-cur;
        }
        if ( !c ) {
            printf("Case #%d: NO\n",aa);
        }
        else {
            printf("Case #%d: %d\n",aa,list[pre][0]);
        }
    }
    return 0;
}
