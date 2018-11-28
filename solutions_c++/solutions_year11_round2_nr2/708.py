#include <iostream>
#include <cstdio>

using namespace std;

pair<int, int> vendors [ 300 ];
int c, d;

bool sol ( double md ){
    double left = vendors [ 0 ].first - md, cr;
    int i, j;
    for ( i = 0; i < c; ++ i ){
        for ( j = ( i == 0 ? 1 : 0 ); j < vendors [ i ] . second; ++ j ){
            cr = max ( left + d, vendors [ i ] . first - md );
            if ( cr - vendors [ i ] . first > md )
                return 0;
            left = cr;
        }
    }
    return true;
}

int main(){
    freopen ( "input.txt", "rt", stdin );
    freopen ( "output.txt", "wt", stdout );
    int k, t, i;
    double pas;
    cin >> t;
    for ( k = 1; k <= t; ++ k ){
        cin >> c >> d;
        for ( i = 0; i < c; ++ i ){
            cin >> vendors [ i ] . first >> vendors[ i ] . second;
        }
        sort ( vendors, vendors + c );
        for ( pas = 1; ! sol ( pas ); pas *= 2.0 );
        double l, r;
        l = 0; r = pas;
        while ( r - l > 0.00000001 ){
            double m = l + ( r - l )/2.0;
            if ( sol ( m ) ){
                r = m - 0.000000001;
            }
            else l = m + 0.000000001;
        }
        printf ( "Case #%d: %.9lf\n", k, l );
    }
    return 0;
}
