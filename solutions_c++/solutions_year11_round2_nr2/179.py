#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <utility>
using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef long long LL;

#define REP(i, n) for(int i=0; i<n; ++i)
#define ST first
#define ND second
#define PB push_back
#define VAR(v,n) __typeof__(n) v=(n)
#define FE(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define ALL(c) (c).begin(),(c).end()

#define MAXN 300

vector<int> T;
int c, d;

inline long double mmax( long double a, long double b ){
    if ( a < b ) return b;
    return a;
}

inline bool ok(long double t){
//    cout << "ok? " << t << endl;
    long double rm;
    rm = T[0] - t;
    for(int i=1; i<T.size(); ++i){
        long double nt = mmax( rm + d, T[i] - t );
        if ( nt > T[i] + t ) return false;
        rm = nt;
    }
    return true;
}

double testcase(){
    T.clear();
    scanf("%d%d", &c, &d);
    REP(i, c){
        int p, v; scanf("%d%d", &p, &v);
        REP(i, v) T.PB( p );
    }
    
    sort( ALL(T) );
    long double low = 0, high = 10e13;
    while( low + 10e-8 < high ){
        long double check = ( low + high ) / 2.0;
        if ( ok(check) ){
            high = check;
        } else low = check;
    }
    return low;
}

int main(){
int z; scanf("%d", &z);
REP(i, z){
    printf("Case #%d: %.1lf\n", i+1, testcase());
}
return 0;
}

