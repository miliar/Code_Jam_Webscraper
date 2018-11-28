#include <cstdio>
#include <algorithm>
#include <vector>

#define REP(i, n) for ( int i = 0; i < (n); i++ ) 
#define FOR(i, a, b) for ( int i = (a); i < (b); i++ ) 

using namespace std;

const int MAX_N = 15;
const int MAX_DATA = 1<<13;

int n, m;
long long data[MAX_DATA];
int M[MAX_DATA];

long long d[MAX_DATA][MAX_N];

long long licz(int v, int ile) {
//    printf("dla %d mam %d %lld\n", v, ile, data[v]);

    if ( v > (1<<n)-2 ) {
        int x = v - (1<<n) + 1;
//        printf("dla v = %d x = %d\n", v, x);
        if ( M[x] <= ile ) return 0;
        else return -1;
    }

    if ( d[v][ile] != -2 ) return d[v][ile];

    int v1 = v*2 + 1;
    int v2 = v*2 + 2;

    long long res = -1;

    long long r1 = licz(v1, ile+1);
    long long r2 = licz(v2, ile+1);
    if ( r1 != -1 and r2 != -1 ) {
        res = r1 + r2 + data[v];
    }

    r1 = licz(v1, ile);
    r2 = licz(v2, ile);
    if ( r1 != -1 and r2 != -1 ) {
        if ( res == -1 ) res = r1 + r2;
        else res = min(res, r1+r2);
    }

    d[v][ile] = res;
    return res;
}

void fun(int cs) {
    scanf("%d", &n);
    m = 1 << n;
    REP(i, m) scanf("%d", &M[i]);
    REP(i, m) M[i] = n - M[i];

    REP(i, n) {
        int w = (1 << (n-i-1)) - 1;
        int q = 1 << (n-i-1);
//        printf("%d %d\n", w, q);
        REP(j, q) {
            scanf("%lld", &data[w+j]);
            REP(c, n+2) d[w+j][c] = -2;
//            printf("%d = %lld\n", w+j, data[w+j]);
        }
    }

    long long res = licz(0, 0);

    printf("Case #%d: %lld\n", cs, res);
}

int main() {
    int T;
    scanf("%d", &T);
    REP(i, T) fun(i+1);

    return 0;
}
