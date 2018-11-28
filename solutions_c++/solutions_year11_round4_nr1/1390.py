#include <iostream>
#include <cstring>
#include <algorithm>
#include <stdio.h>
#include <math.h>
using namespace std;

#define MaxN 1010
#define ll long long

struct put {
   double x1,x2;
   int v;

   put() {}
   put( double _x1, double _x2, int _v ) {
       x1 = _x1;
       x2 = _x2;
       v = _v;
   }

   bool operator < ( const put& b ) const {
       return x1 < b.x1;
   }
};

put a[2*MaxN];
int T,s,r,n,x;
double t;
int w,x1,x2;
double ret;

double minT;

double maxDob;
int maxID;

int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);

    scanf("%d",&T);
    for (int t3 = 0; t3 < T; ++t3) {
        scanf("%d%d%d%lf%d",&x,&s,&r,&t,&n);
        for (int i = 0; i < n; ++i) {
            scanf("%d%d%d",&x1,&x2,&w);
            a[i] = put( x1, x2, w );
        }
        sort( a, a+n );

        int N = n;
        if ( a[0].x1 > 0 ) {
            a[N++] = put( 0, a[0].x1, 0 );
        }
        for (int i = 1; i < n; ++i) {
            if ( a[i].x1 != a[i-1].x2 ) {
                a[N++] = put( a[i-1].x2, a[i].x1, 0 );
            }
        }
        if ( a[n-1].x2 != x ) {
            a[N++] = put( a[n-1].x2, x, 0 );
        }
        n = N;


        ret = 0;

        while ( t > 0 ) {
            bool kraj = true;

            minT = 2000000000;
            for (int i = 0; i < n; ++i) {
                if ( a[i].x2 == a[i].x1 ) continue;

                kraj = false;
                double tmp = ( a[i].x2 - a[i].x1 ) / double( a[i].v + r );
                minT = min( minT, tmp );
            }

            if ( kraj ) break;

            minT = min( minT, t );

            maxDob = -1;
            for (int i = 0; i < n; ++i) {
                if ( a[i].x2 == a[i].x1 ) continue;

                double tmp = ( a[i].x2 - a[i].x1 ) / double( a[i].v + s );
                double pobo = ( ( a[i].x2 - a[i].x1 ) - ( a[i].v + r )*minT ) / double( a[i].v + s ) + minT;
                double pob = tmp - pobo;

                if ( maxDob < pob ) {
                    maxDob = pob;
                    maxID = i;
                }
            }

            //a[ maxID ] = put( a[ maxID ].x1 + minT*( a[ maxID ].v + r ), a[ maxID ].x2, a[ maxID ].v );
            double tmp = ( a[ maxID ].v + r )*t;
            if ( tmp > a[ maxID ].x2 - a[ maxID ].x1 ) {

                double tp = ( a[ maxID ].x2 - a[ maxID ].x1 ) / double( a[ maxID ].v + r );

                ret += tp;
                t -= tp;
                a[ maxID ] = put( a[ maxID ].x1 + tp*( a[ maxID ].v + r ), a[ maxID ].x2, a[ maxID ].v );

            }
            else {
                a[ maxID ] = put( a[ maxID ].x1 + tmp, a[ maxID ].x2, a[ maxID ].v );

                ret += t;
                t = 0.0;
            }

        }

        for (int i = 0; i < n; ++i)
            ret += ( a[i].x2 - a[i].x1 ) / double( a[i].v + s );

        printf("Case #%d: %.9lf\n",t3+1,ret);
    }

    return 0;
}
