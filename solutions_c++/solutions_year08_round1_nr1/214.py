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
    int n;
    scanf("%d", &n);
    VI vi, vj;
    REP( i, n) {
        int t;
        scanf("%d", &t);
        vi.push_back( t);
    }
    REP( i, n) {
        int t;
        scanf("%d", &t);
        vj.push_back( t);
    }
    sort( ALL( vi));
    sort( ALL( vj));
    reverse( ALL( vj));
    LL sum = 0;
    REP( i, n) {
        sum+= (LL)vi[i]*vj[i];
    }
    printf("%lld\n", sum);
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
