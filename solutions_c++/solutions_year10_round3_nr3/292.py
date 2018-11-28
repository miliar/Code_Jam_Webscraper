#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

long long table[50];
int mark[200][200];
int cnt[50];

int main() {
    int aa, nn, m ,n, mm, ms, mr, mc, lim, tcnt;
    int i, j, k, ok, a, b;
    int t1, t2, ans;
    long long p, tnum;
    scanf("%d",&nn);
    memset(mark,0,sizeof(mark));
    mm = 0;
    for ( aa = 1; aa <= nn; ++aa ) {
        ++mm;
        memset(cnt,0,sizeof(cnt));
        scanf("%d %d",&m,&n);
        for ( i = 0; i < m; ++i ) {
            scanf("%llx",&table[i]);
        }
        ans = 0;
        lim = min(m,n);
        while ( 1 ) {
            tcnt = 0;
            ms = -1;
            for ( i = 0; i < m; i++ ) {
                for ( j = 0; j < n; ++j ) {
                    if ( mark[i][j] == mm ) continue;
                    if ( ms < 0 ) {
                        ms = 1;
                        mr = i;
                        mc = j;
                        tcnt = 1;
                    } else if ( ms == 1 ) ++tcnt;
                    for ( k = 1; k < lim; ++k ) {
                        // check row /col
                        ok = 1;
                        if ( i+k >= m || j+k >= n ) ok = 0;
                        for ( a = i, b = 0; b <= k && ok; ++a, b++ ) {
                            if ( mark[a][j+k] == mm ) {
                                ok = 0;
                            }
                        }
                        for ( a = j, b = 0; b <= k && ok; ++a, ++b ) {
                            if ( mark[i+k][a] == mm ) ok = 0;
                        }
                        if ( !ok ) break;
                        p = (table[i] >> (n-j-k-1)) & ((1<<(k+1))-1);
                        t1 = p & 1;
                        t2 = (p>>1) & 1;
                        if ( !(t1^t2) ) ok = 0;
                        for ( a = i+1, b = 0; ok && b < k; a++, b++ ) {
                            tnum = (table[a] >> (n-j-k-1)) & ((1<<(k+1))-1);
                            t1 = tnum & 1;
                            t2 = (tnum >> 1) & 1;
                            if ( !(t1^t2) ) ok = 0;
                            if ( (tnum^p) ^ ((1<<(k+1))-1) ) ok = 0;
                            p = tnum;
                        }
                        if ( !ok ) break;
                        if ( k+1 > ms ) {
                            ms = k+1;
                            mr = i;
                            mc = j;
                            tcnt = 1;
                        } else if ( k+1 == ms ) ++tcnt;
                    }
                }
            }
            if ( ms < 0 ) break;
            if ( ms == 1 ) {
                ++ans;
                cnt[ms] = tcnt;
                break;
            }
            // clear
            if ( !cnt[ms] ) ++ans;
            cnt[ms]++;
            for ( a = mr, i = 0; i < ms; a++, i++ ) {
                for ( b = mc, j = 0; j < ms; b++, j++) {
                    mark[a][b] = mm;
                }
            }
        }
        printf("Case #%d: %d\n",aa, ans);
        for ( i = lim; i >= 1; i-- ) {
            if ( !cnt[i] ) continue;
            printf("%d %d\n",i,cnt[i]);
        }
    }

    return 0;
}

