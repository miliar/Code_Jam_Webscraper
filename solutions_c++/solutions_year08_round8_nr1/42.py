#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#pragma warning( disable : 4244 4267 4018 4996 4800 )
//#pragma comment( linker, "/stack:10000000" )
using namespace std; 
typedef vector< int > vi; typedef vector< vector< int > > vvi; typedef vector< string > vs; typedef vector< double > vd;
typedef vector< vd > vvd; typedef long long ll; typedef vector< ll > vll; typedef vector< vll > vvll; typedef pair< int, int > pii;
#define all( v ) (v).begin( ), (v).end( )

ifstream in( "a.in" );
ofstream out( "a.out" );

void main() {
    int ntests;
    in >> ntests;
    for ( int ntest = 1; ntest <= ntests; ++ntest ) {
        out << "Case #" << ntest << ": ";

        vd x1, y1, x2, y2;
        x1 = y1 = x2 = y2 = vd( 3 );
        for ( int i = 0; i < 3; i++ ) {
        	in >> x1[i] >> y1[i];
        }
        for ( int i = 0; i < 3; i++ ) {
        	in >> x2[i] >> y2[i];
        }

        double a = x1[1] - x1[0] - ( x2[1] - x2[0] );
        double b = x1[2] - x1[0] - ( x2[2] - x2[0] );
        double c = x2[0] - x1[0];
        double d = y1[1] - y1[0] - ( y2[1] - y2[0] );
        double e = y1[2] - y1[0] - ( y2[2] - y2[0] );
        double f = y2[0] - y1[0];

        double t1, t2;
        t1 = t2 = 0;

        if ( a == 0 ) {
            if ( b == 0 ) {
                t1 = 0;
                if ( d == 0 ) {
                    t2 = f / e;                    
                } else 
                    t2 = 0;
            } else {
                t2 = c / b;
                if ( d == 0 )
                    t1 = 0;
                else
                    t1 = ( f - e * t2 ) / d;
            }
        } else {
            double t = e - d * b / a;
            if ( t == 0 ) 
                t2 = 0;
            else
                t2 = ( f - d * c / a ) / t;
            t1 = c / a - b / a * t2;

        }

        double eps = 1e-10;
        bool b1 = ( fabs( a * t1 + b * t2 - c ) <= eps );
        bool b2 = ( fabs( d * t1 + e * t2 - f ) <= eps  );
        assert( b1 && b2 );

        out.setf( ios::fixed );
        out.precision( 10 );

        if ( !( b1 && b2 ) ) {
            out << "No Solution\n";
        }
        else {
            out << x1[0] + ( x1[1] - x1[0] ) * t1 + ( x1[2] - x1[0] ) * t2;
            out << ' ';
            out << y1[0] + ( y1[1] - y1[0] ) * t1 + ( y1[2] - y1[0] ) * t2;
            out << endl;
        }
    }
}