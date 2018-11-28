#include <iostream>
#include "math.h" 

using namespace std ;

typedef long double LD ;

LD pi = atan(1.0)*4.0 ;

LD primX( LD x )
{
  if( x >= 1.0 )
    return pi/4.0 ;
  
  return asin(x)/2.0 + x*sqrt(1.0-x*x)/2.0 ;
}

LD arc( LD R, LD x0, LD x1 , LD y0 )
{
  return R*R*( primX( x1/R ) - primX( x0/R ) ) - y0*( x1 - x0 ) ;
}

LD norm( LD a, LD b )
{
  return a*a + b*b ;
}



int main()
{
  int N = 0 ;
  scanf("%d", &N );
  
  for( int n = 0 ; n < N ; n ++ )
    {
      LD f,R,t,r,g ;
      cin >> f >> R >> t >> r >> g ;

      R = R - t - f ;
      g -= 2*f ;
      r += f ;

      LD aire = 0 ;

      for( LD x = r ; x < R ; x += g+2*r )
        for( LD y = r ; y < R ; y += g+2*r )
          if( norm(x,y) < R*R )
            {
              LD x1,y1,x2,y2 ;
              x2 = x+g ;
              y2 = y+g ;

              if( norm(x2,y2) < R*R ) 
                aire += g*g ;
              else
                {
                  
                  if( norm( x2,y) < R*R && norm( x,y2) < R*R )
                    {
                      y1 = sqrt(R*R - x2*x2) ;
                      x1 = sqrt(R*R - y2*y2) ;
                      
                      aire += g*(y1-y) + (x1-x)*(y2-y1) ;
                      aire += arc( R , x1,x2,y1 ) ;
                    }
                  else if( norm( x2,y) < R*R && norm( x,y2) > R*R )
                    {
                      y1 = sqrt(R*R - x2*x2) ;
                      aire += g*(y1-y) ;
                      aire += arc( R , x , x2 , y1 ) ;
                    }
                  else if( norm( x2,y) > R*R && norm( x,y2) < R*R )
                    {
                      x1 = sqrt(R*R - y2*y2) ;
                      LD x2p = sqrt(R*R - y*y) ;
                      
                      aire += g*(x1-x) ;
                      aire += arc( R , x1 , x2p , y ) ;

                      //cout << "---- " << aire << " " << x1 << " " << x2p << endl ;
                    }
                  else 
                    {
                      x1 = sqrt(R*R - y*y) ;
                      
                      //cout << aire << endl ;
                      //cout << x << " " << x1 << endl ;
                      //cout << endl ;
                      aire += arc( R , x, x1 , y ) ;
                      }
                }
                  
            }

      LD result = 1 - (aire*4.0)/(pi*(R+t+f)*(R+t+f)) ;

      printf("Case #%d: %f\n", n+1 ,(float) result );
    }
 
}
