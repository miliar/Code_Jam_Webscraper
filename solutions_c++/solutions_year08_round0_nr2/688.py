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

int linef( const char *format, ...) {
    char b[1024];
    gets( b);
    va_list ap;

    va_start(ap, format);
    return vsscanf( b, format, ap);
}
struct TV {
    VPII vec;
    int t;
    TV( int t_) : t(t_) { }
    void add_from( int time) {
        vec.push_back( MP( time, 1));
    }
    void add_to( int time) {
        vec.push_back( MP( time+t, -1));
    }
    int compute() {
        sort( ALL( vec));
        int level = 0;
        int ret = 0;
        REP( i, vec.SZ) {
//            printf("have %d %d\n", vec[i].first, vec[i].second);
            level-= vec[i].second;
            ret = max( ret, -level);
        }
//        printf("\n");
        return ret;
    }
};
int scan() {
    char b[16];
    scanf("%s", b);
    REP( i, 16) b[i]-='0';
    return b[0]*600+b[1]*60+b[3]*10+b[4];
}
void problem() {
    int t, aa, bb;
    scanf("%d%d%d", &t, &aa, &bb);
    TV t1( t), t2( t);
    REP( i, aa) {
        t1.add_from( scan());
        t2.add_to( scan());
    }
    REP( i, bb) {
        t2.add_from( scan());
        t1.add_to( scan());
    }
    printf("%d %d\n", t1.compute(), t2.compute());
}
int main() {
    int n;
    linef("%d", &n);
    REP( i, n) {
        printf("Case #%d: ", i+1);
        problem();
    }
    return 0;
}
