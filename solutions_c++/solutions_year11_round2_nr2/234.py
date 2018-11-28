#include <cstdio>
#include <cmath>
#include <vector>
#include <iostream>

using namespace std;

vector < double > v;

int N;
double D;

int ok ( double dist ){
    double last = v[0] - dist;

    for ( int i = 1; i < v.size(); ++i )
        if ( v[i] - ( last + D ) > dist ) last = v[i] - dist;
        else {
            last = last + D;
            if ( fabs ( last - v[i] ) > dist )return 0;
        }
    return 1;
}
void solve( int num ){
    scanf ( "%d%lf", &N, &D );

    for ( int i = 0; i < N; ++i ){
        double p;
        int cnt;

        scanf ( "%lf%d", &p, &cnt );

        while ( cnt -- )
            v.push_back ( p );
    }

    double l = 0, r = 1e+15;

    for ( int i = 0; i < 100; ++i ){
        double mid = ( l + r ) / 2;

        if ( ok ( mid ) ) r = mid;
        else l = mid;
    }

    printf ( "Case #%d: %.6f\n", num, ( l + r ) / 2. );
    v.erase ( v.begin(), v.end() );

}
int main(){
    int tests;

    scanf ( "%d", &tests );
    for ( int i = 0; i < tests; ++i )
    solve(i + 1);
}
