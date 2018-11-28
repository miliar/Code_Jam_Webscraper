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

int linef( const char *format, ...) {
    char b[1024];
    gets( b);
    va_list ap;

    va_start(ap, format);
    return vsscanf( b, format, ap);
}
void problem() {
    int n;
    linef( "%d", &n);
    map<string,int> ma;
    VS revma;
    REP( i, n) {
        char b[101];
        gets( b);
        ma[b] = i;
        revma.push_back( b);
    }
    int m;
    linef("%d", &m);
    int a[100] = {};
    REP( ii, m) {
        int a2[100];
        RESET( a2, 0x7f);
        char b[101];
        gets( b);
        int cur = ma[b];
        REP( i, n) COND( a[i]!=0x7f7f7f7f) REP( j, n) COND( j!=cur)
            a2[j] = min( a2[j], a[i]+(i!=j));
        memcpy( a, a2, sizeof( a));
    }
    int ret = 0x7f7f7f7f;
    REP( i, n)
        ret = min( ret, a[i]);
    printf("%d\n", ret);

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
