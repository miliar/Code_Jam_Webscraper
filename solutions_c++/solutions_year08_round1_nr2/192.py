#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdarg.h>

#include <string>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;
#define LL long long


#define REP(i,n) for( int i = 0; i<int(n); i++)
#define REPD(i,n) for( int i = int(n)-1; i>=0; i--)
#define VI vector<int>
#define VS vector<string>
#define RESET(a,ch) memset( a, ch, sizeof( a))
#define COND if
#define PII pair<int,int>
#define VPII vector<PII>
#define MP(a,b) make_pair( a, b)
#define ALL(x) (x).begin(), (x).end()
#define SZ size()

void problem() {
    int shakes;
    int consumers;
    scanf("%d%d", &shakes, &consumers);

    VPII cons[100];
    REP( i, consumers) {
        int t;
        scanf("%d", &t);
        REP( j, t) {
            int a, b;
            scanf("%d%d", &a, &b);
            cons[i].push_back( MP( a-1, b));
        }
    }
    int best = 100;
    int bestval;
    REP( mask, 1<<shakes) {
        bool good = true;
        REP( i, consumers) {
            bool ok = false;
            REP( j, cons[i].SZ) {
                int pos = cons[i][j].first;
                int value = cons[i][j].second;
                if( (mask >> pos & 1) == value) {
                    ok = true;
                    break;
                }
            }
            if( !ok) {
                good = false;
                break;
            }
        }
        if( !good)
            continue;
        int bc = 0;
        int v = mask;
        while( v) {
            v&= v-1;
            bc++;
        }
        if( bc<best) {
            best = bc;
            bestval = mask;
        }
    }
    if( best==100) {
        printf("IMPOSSIBLE\n");
        return ;
    }
    REP( i, shakes)
        printf("%d%c", bestval >> i & 1, i+1==shakes ? '\n' : ' ');
}
int main() {
    int n;
    scanf("%d", &n);
    REP( i, n) {
        printf("Case #%d: ", i+1);
        problem();
    }
    return 0;
}
