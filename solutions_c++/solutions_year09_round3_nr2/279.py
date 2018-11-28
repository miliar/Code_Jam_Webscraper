#include <cmath>
#include <cctype>
#include <ctime>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <map>
#include <sstream>
#include <algorithm>
#include <utility>

#define forn(a,b,c) for (int a=b; a < c; ++a)
#define x first
#define y second
#define pb push_back
#define mp make_pair
#define set(a,b) memset ((a) , b , sizeof(a) )

using namespace std;

typedef pair <int , int> pii;
typedef long long ll;
typedef vector <int> vi;

int t , brt , n;
double x, y, z, vx , vy , vz, speed, dist, time2;

double dist2 (double ax, double ay, double az)
{
    return sqrt ( (ax)*(ax) + (ay)*(ay) + (az)*(az) );
}

int main ()
{
    scanf ( "%d", &t );
    while ( t -- )
    {
        scanf ( "%d", &n );
        x = y = z = vx = vy = vz = dist = time2 = 0.;
        speed = 1.;
        int _vx = 0 , _vy = 0 , _vz = 0 , _x = 0, _y = 0, _z = 0;

        for (int i=0; i < n; ++i)
        {
            int tx,ty,tz, tvx,tvy,tvz;
            scanf ( "%d%d%d%d%d%d" , &tx, &ty , &tz, &tvx, &tvy, &tvz );
            _vx += tvx;
            _vy += tvy;
            _vz += tvz;
            _x += tx ;
            _y += ty ;
            _z += tz ;

            x += tx;
            y += ty;
            z += tz;
            //printf ( "vx before %lf" , vx );
            vx += tvx;
            //printf ( "  vx after %lf\n", vx );
            vy += tvy;
            vz += tvz;
        }
        //printf ( "x = %lf, y = %lf , z = %lf\nvx = %lf, vy = %lf , vz = %lf\n" , x,y,z,vx,vy,vz );
        x /= (double) n;
        y /= (double) n;
        z /= (double) n;
        dist = dist2 ( x , y , z );
        vx /= (double) n;
        vy /= (double) n;
        vz /= (double) n;
        //printf ( "x = %lf, y = %lf , z = %lf\nvx = %lf, vy = %lf , vz = %lf\n" , x,y,z,vx,vy,vz );
        //printf ( "%d %d %d\n" , _vx , _vy, _vz );

        if ( _vx == 0 && _vy == 0 && _vz == 0 )
        {
            printf ( "Case #%d: %.8lf %.8lf\n" , (++brt) , dist , 0.0 );
            continue;
        }
        if ( _x == 0 && _y == 0 && _x == 0 )
        {
            printf ( "Case #%d: %.8lf %.8lf\n" , (++brt) , dist , 0.0 );
            continue;
        }


        double l = 0.0 , r = 1e7;

        for ( int i=0; i < 10000; ++i)
        {
            double m1 = l + ( (r-l)/3. ) ;
            double m2 = l + ( 2.*(r-l)/3. );
            //cout << l << " " << m1 << " " << m2 << " " << r << endl;

            if ( dist2 ( x + m1*vx , y + m1 * vy , z + m1 * vz ) < dist2 ( x + m2*vx , y + m2*vy , z + m2*vz ) ) r = m2;
                else l = m1;
        }
        double sol = (l + r) / 2.;
        //cout << l << ' ' << r << endl;
        if ( dist < dist2 ( x + sol*vx , y + sol*vy , z + sol*vz ) ) printf ( "Case #%d: %.8lf %.8lf\n", (++brt) , dist , 0.0 );
            else printf ( "Case #%d: %.8lf %.8lf\n" , (++brt) , dist2 ( x + sol*vx , y + sol*vy , z + sol*vz ) , sol );
    }
    return 0;
}
