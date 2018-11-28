#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
using namespace std;

const int MAXN = 1005;

int R, k, N;
int g[MAXN];
int next[MAXN];
int earn[MAXN];

int main() {
    int t, casN, i, curr, pos, st, cycle_len;
    long long cycle_sum, ans;
    
    scanf("%d", &t);
    for ( casN=1; casN<=t; casN++ ) {
        
        scanf("%d%d%d", &R, &k, &N);
        for ( i=0; i<N; i++ ) {
            scanf("%d", &g[i] );
            earn[i] = -1;
        }
        
        curr = -1;
        pos = 0;
        i = 0;
        while ( true ) {
            if ( curr + g[i] > k || i == pos ) {
                next[pos] = i;
                earn[pos] = curr;
                curr = 0;
                pos = i;
                if ( earn[pos] != -1 ) break;
            }
            curr += g[i];
            if ( curr > k ) {
                next[i] = -1;
                earn[i] = 0;
                break;
            }
            i++;
            if ( i == N ) i = 0;
        }
        
        if ( next[i] == -1 ) {
            ans = 0LL;
            pos = 0;
            while ( R > 0 && next[pos] != -1 ) {
                ans += earn[pos];
                R--;
                pos = next[pos];
            }
            printf("Case #%d: %lld\n", casN, ans);
        } else {
            ans = 0LL;
            st = pos;
            pos = 0;
            while ( R > 0 && pos != st ) {
                ans += earn[pos];
                R--;
                pos = next[pos];
            }
            if ( R > 0 ) {
                cycle_len = 0;
                cycle_sum = 0LL;
                do {
                    cycle_sum += earn[pos];
                    cycle_len++;
                    pos = next[pos];
                } while ( pos != st );
                ans += cycle_sum * (long long)( R / cycle_len );
                R %= cycle_len;
                pos = st;
                while ( R > 0 ) {
                    ans += earn[pos];
                    pos = next[pos];
                    R--;
                }
            }
            printf("Case #%d: %lld\n", casN, ans);
        }
        
    }

    //system("Pause");
    return 0;
}
