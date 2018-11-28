#include <cstdio>
#include <algorithm>
#include <vector>

#define REP(i, n) for ( int i = 0; i < (n); i++ ) 
#define FOR(i, a, b) for ( int i = (a); i < (b); i++ ) 

using namespace std;

void fun(int cs) {
    long long n, k;
    scanf("%lld %lld", &n, &k);

    long long m = 1ll << n;
    int is_on = 0;

    k %= m;
    if ( k == m-1 ) 
        is_on = 1;

    printf("Case #%d: %s\n", cs, is_on ? "ON" : "OFF");
}

int main() {
    int T;
    scanf("%d", &T);
    REP(i, T) fun(i+1);

    return 0;
}
