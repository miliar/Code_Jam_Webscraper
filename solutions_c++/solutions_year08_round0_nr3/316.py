#include <cstdio>
#include <cmath>

double f, R, t, r, g;

const double EPS = 1e-8;

void ReadData()
{
   scanf( "%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g );
}

double PolySqr( const double *x, const double *y, int n )
{
   double s = 0;
   for( int i = 0; i<n; ++i )
      s += (x[i]*y[(i+1)%n]-x[(i+1)%n]*y[i]);
   return s>=0 ? s/2 : -s/2;
}

double GetXPoint( double x, double y, double d, double r )
{
   double D = sqrt( r*r-y*y )*fabs( d );
   double t = (-x*d-D)/d/d;
   if( t>=-EPS && t<=1+EPS )
      return t;
   t = (-x*d+D)/d/d;
   if( t>=-EPS && t<=1+EPS )
      return t;
   return -1;
}

double GetYPoint( double x, double y, double d, double r )
{
   double D = sqrt( r*r-x*x )*fabs( d );
   double t = (-y*d-D)/d/d;
   if( t>=-EPS && t<=1+EPS )
      return t;
   t = (-y*d+D)/d/d;
   if( t>=-EPS && t<=1+EPS )
      return t;
   return -1;
}

double Intersect( double x, double y, double d, double r )
{
   if( d<=0 )
      return 0;
   if( (x+d)*(x+d)+(y+d)*(y+d)<=r*r )
      return d*d;
   if( x*x+y*y>=r*r )
      return 0;
   double X[5], Y[5], x1, y1, x2, y2, s;
   X[0] = x; Y[0] = y;
   double t = GetXPoint( x, y, d, r );
   if( t>-EPS )
   {
      x1 = X[1] = x+t*d;
      y1 = Y[1] = y;
      t = GetXPoint( x+d, y+d, -d, r );
      if( t>-EPS )
      {
         x2 = X[2] = x+d-t*d;
         y2 = Y[2] = y+d;
         X[3] = x;
         Y[3] = y+d;
         s = PolySqr( X, Y, 4 );
      }
      else
      {
         t = GetYPoint( x, y+d, -d, r );
         x2 = X[2] = x;
         y2 = Y[2] = y+d-t*d;
         s = PolySqr( X, Y, 3 );
      }
   }
   else
   {
      X[1] = x+d;
      Y[1] = y;
      t = GetYPoint( x+d, y, d, r );
      x1 = X[2] = x+d;
      y1 = Y[2] = y+t*d;
      t = GetXPoint( x+d, y+d, -d, r );
      if( t>-EPS )
      {
         x2 = X[3] = x+d-t*d;
         y2 = Y[3] = y+d;
         X[4] = x;
         Y[4] = y+d;
         s = PolySqr( X, Y, 5 );
      }
      else
      {
         t = GetYPoint( x, y+d, -d, r );
         x2 = X[3] = x;
         y2 = Y[3] = y+d-t*d;
         s = PolySqr( X, Y, 4 );
      }
   }
   double alp = acos( (2*r*r-(x2-x1)*(x2-x1)-(y2-y1)*(y2-y1))/2/r/r );
   X[0] = 0;
   Y[0] = 0;
   X[1] = x1;
   Y[1] = y1;
   X[2] = x2;
   Y[2] = y2;
   return s+alp*r*r/2-PolySqr( X, Y, 3 );
}

double Work()
{
   double P = 0, Q = 0;
   int n = static_cast<int>( R/(g+2*r)+1 );
   //printf( "%d\n", n );
   for( int i = 0; i<n; ++i )
   {
      double x = i*(g+2*r);
      for( int j = 0; j<n; ++j )
      {
         double y = j*(g+2*r);
         P += Intersect( x+r+f, y+r+f, g-2*f, R-t-f );
         Q += Intersect( x, y, g+2*r, R );
      }
   }
   return 1-P/Q;
}

void Output( int t, double ans )
{
   printf(  "Case #%d: %.6lf\n", t, ans );
}

int main()
{
   int n;
   scanf( "%d", &n );
   for( int i = 0; i<n; ++i )
   {
      ReadData();
      Output( i+1, Work() );
   }
   return 0;
}

