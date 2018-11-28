#include <iostream>
#include <vector>
#include <math.h>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
#include <string>
#include <string.h>
#include <stack>
#include <iomanip>
#include <cstdlib>
#include <cstdio>
using namespace std;

typedef long long ll;

const ll inf = 100000000000000000LL;

int n,d;
vector< int > x;

bool possible( ll m ){
    ll pos = -inf;
    for( int i = 0; i < x.size(); ++i ){
        ll range = pos + d;
        if( range > x[i] + m ) return false;

        pos = max( pos + d , x[i] - m );
    }
    return true;
}

int main(){
    freopen("Ulaz.txt","r",stdin);
    freopen("Izlaz.txt","w",stdout);
    int tests;
    scanf("%d",&tests);

    for( int t = 1; t <= tests; ++ t ){
        scanf("%d%d",&n,&d);
        d *= 2;

        x.clear();

        for( int i = 0; i < n; ++i ){
            int p,v; scanf("%d%d",&p,&v);
            p *= 2;
            for( int j = 0; j < v; ++j ) x.push_back( p );
        }
        sort( x.begin(), x.end() );

        ll sol = -1;
        ll lo = 0, hi = 100000000000000000LL;
        while( lo <= hi ){
            ll mid = (lo+hi)>>1;
            bool ok = possible(mid);
            if( ok ) hi = mid - 1 , sol = mid;
            else lo = mid + 1;
        }

        printf("Case #%d: %.1lf\n",t,sol/2.0);

    }

    return 0;
}
