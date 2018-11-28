#include <cstdio>
#include <cmath>

double sqr( double x )
{
    return x*x;
}

double dist2(double x1, double y1, double x2, double y2 )
{
    return sqr(x1-x2) + sqr(y1-y2);
}

double f2(double x1, double x2, double xc, double yc, double R)
{
    double a, b;
    a = x1 - xc;
    b = x2 - xc;
    double res = R*R / 2.0 * (asin(b/R) - asin(a/R)) + 
                 (b*sqrt(R*R-b*b) - a*sqrt(R*R-a*a)) / 2.0;
    return res;
}

double f1(double xc, double yc, double g, double R)
{
    if ( dist2(g,g, xc,yc) <= R*R )
        return g*g;

    double x1, x2;
    if ( dist2(0,g, xc,yc) >= R*R )
        x1 = 0;
    else
        x1 = xc + sqrt(R*R - sqr(g-yc));

    if ( dist2(g,0, xc,yc) <= R*R )
        x2 = g;
    else
        x2 = xc + sqrt(R*R - sqr(yc));

    double res = yc * (x2-x1) + x1 * g + f2(x1, x2, xc, yc, R);

    return res;
}

int main()
{
    int T, i, j;
    double f, R, t, r, g, mx, my, xc, yc, Pi = 3.1415926535897932384626433832795;
    scanf( "%d", &T );
    for ( int cas = 1 ; cas <= T ; cas++ )
    {
        scanf( "%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g );
        double res = 0.0;
        for ( i = 1 ; i < 10000 ; i++ )
            for ( j = 1 ; ; j++ )
            {
                mx = r+f + (i-1) * (g + 2.0*r);
                my = r+f + (j-1) * (g + 2.0*r);

                if ( mx*mx + my*my > sqr(R-t-f) )
                    break;

                xc = -mx;
                yc = -my;
                res += f1(xc, yc, g-2.0*f, R-t-f);
            }

        res *= 4.0 / (Pi * sqr(R));

        printf( "Case #%d: %.6lf\n", cas, 1.0 - res );
    }
    return 0;
}
