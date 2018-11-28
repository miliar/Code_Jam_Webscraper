#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

template<typename T, typename U> inline void relaxmin( T &res, const U &x ) { if ( x < res ) res = x; }

int main(void) { 
    cin.sync_with_stdio(0);

    int CASES; cin >> CASES;
    for ( int tt=1; tt<=CASES; ++tt ) { // caret here
        int n; cin >> n;
        int x[n], y[n], r[n];
        for ( int i=0; i<n; ++i ) cin >> x[i] >> y[i] >> r[i];

        double ans = HUGE_VAL;
        if ( n == 1 ) ans = r[0];
        else if ( n == 2 ) ans = max(r[0], r[1]);
        else if ( n == 3 ) {
            relaxmin(ans, max(double(r[0]), 0.5*(hypot(x[1]-x[2], y[1]-y[2]) + r[1]+r[2])));
            relaxmin(ans, max(double(r[1]), 0.5*(hypot(x[0]-x[2], y[0]-y[2]) + r[0]+r[2])));
            relaxmin(ans, max(double(r[2]), 0.5*(hypot(x[0]-x[1], y[0]-y[1]) + r[0]+r[1])));
        }

        printf("Case #%d: %.6f\n", tt, ans);
    }

    return 0;
} 
