#include <iostream>
#include <stdio.h>
#include <cstring>
#include <algorithm>
using namespace std;

#define MaxN 110

int score[MaxN];
int n, s, p;
int T;

int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);

    scanf("%d",&T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d%d%d",&n,&s,&p);
        for (int i = 0; i < n; ++i)
            scanf("%d",&score[i]);

        sort( score, score+n );

        int ret = 0;
        for (int i = 0; i < n; ++i) {
            if ( score[i] >= 29 ) { ret++; continue; }
            if ( score[i] == 1 )  { ret += p <= 1; continue; }
            if ( score[i] == 0 )  { ret += p == 0; continue; }

            int moze = -1;
            for (int jedan = 0; jedan <= 10; ++jedan)
                for (int dva = jedan; dva <= jedan+2; ++dva) {
                    int tri = score[i] - jedan - dva;
                    if ( abs( tri - jedan ) > 2 || abs( tri - dva ) > 2 ) continue;
                    if ( jedan < p && dva < p && tri < p ) continue;

                    if ( abs( tri - jedan ) == 2 || abs( tri - dva ) == 2 || abs( dva - jedan ) == 2 ) {
                        if ( moze == -1 ) moze = 1;
                    }
                    else {
                        moze = 2;
                    }
                }


            if ( moze == 2 ) ret++;
            if ( moze == 1 && s > 0 ) {
                ret++;
                s--;
            }
        }

        printf("Case #%d: %d\n",t,ret);
    }

    return 0;
}
