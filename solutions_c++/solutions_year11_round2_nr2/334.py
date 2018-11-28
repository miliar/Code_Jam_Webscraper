#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <queue>
#include <math.h>

using namespace std;

struct par{
    int f, s;
    par( int a, int b ) : f(a), s(b){};
    par(){};
};


const long long inf = (long long)1e16;
const double eps = 1e-13;

vector <par> G;

int n,D;

bool ok( long long vreme ){

    long long min_pos = -inf;

    for(int i = 0; i < G.size(); ++i ){
     long long mogu = G[i].f - vreme;
     min_pos  = max( mogu, min_pos );
     for(int j = 0; j < G[i].s; ++j ){
       long long need = abs( min_pos - G[i].f );
       if( need > vreme ) return 0;
       min_pos += D;
    }
  }
    return 1;
}



int main(){

    freopen("B-large.IN", "r", stdin );
    freopen("sol.txt", "w", stdout );

    int test;
    scanf("%d", &test );

    for(int t = 1; t <= test; ++t ){
        scanf("%d %d", &n, &D );
        G.clear(); D *= 2;

        long long sumv = 0.;
        for(int i = 0; i < n; ++i ){
          int p, v;
          scanf("%d %d", &p, &v ); p *= 2;
          G.push_back( par( p, v ) );
          sumv += v;
        }

        long long sol = 0.;
        long long lo  = 0, hi = sumv * D;

        while( lo <= hi ){
            long long mid = (lo + hi) / 2.;
            if( ok( mid ) ) hi = mid - 1, sol = mid;
            else lo = mid + 1;
        }

        printf("Case #%d: %.6lf\n", t, sol / 2. );
    }

    return 0;
}
