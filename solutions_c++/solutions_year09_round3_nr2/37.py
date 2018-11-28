#include <cstdio>
#include <cmath>

int main( void ) {

 int test; scanf( "%d", &test );

 for( int cs = 0; cs < test; ++cs ) {

    int n; scanf( "%d", &n );
    int x[500], y[500], z[500], vx[500], vy[500], vz[500];

    for( int i = 0; i < n; ++i )
        scanf( "%d%d%d%d%d%d", x+i, y+i, z+i, vx+i, vy+i, vz+i );

    double Ax = 0., Ay = 0., Az = 0.;
    double Bx = 0., By = 0., Bz = 0.;

    for( int i = 0; i < n; ++i ) {
        Ax += vx[i];
        Ay += vy[i];
        Az += vz[i];

        Bx += x[i];
        By += y[i];
        Bz += z[i];
    }

    double t = (  - Ax * Bx - Ay * By - Az * Bz ) / ( Ax * Ax + Ay * Ay + Az * Az );
    if( ( Ax * Ax + Ay * Ay + Az * Az ) < 1e-9 ) t = 0;
    if( t < 0 ) t = 0;

    double Cx = 0., Cy = 0., Cz = 0.;
    for( int i = 0; i < n; ++i ) {
        Cx += x[i] + t * vx[i];
        Cy += y[i] + t * vy[i];
        Cz += z[i] + t * vz[i];
    }
    Cx /= n; Cy /= n; Cz /= n;

    printf( "Case #%d: %0.8lf %0.8lf\n", cs+1, sqrt( Cx*Cx + Cy*Cy + Cz * Cz ), t );
 }

 return 0;
}
