#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <cmath>

using namespace std ;

double tri ( double x1 , double y1 , double x2 , double y2 )
{
return abs ( x1*y2-x2*y1 ) / 2.0 ;
}


double getprob ( int caseno )
{
double fly ;
double outside ;
double inside ;
double gap ;
double stringr ;
double thickness ;
double prob = 0 ;
double area  ;
double open = 0 ;


cin >> fly >> outside >> thickness >> stringr >> gap ;

area = M_PI * outside * outside ;

inside = outside - thickness ;
if ( inside <= fly + stringr * sqrt(2) + fly * sqrt(2) )
   return 1 ;
if ( gap <= fly * 2 ) 
   return 1 ;


gap -= fly*2 ;
double hole = gap*gap * 4 ;
inside -= fly ;
double inside2 = inside*inside ;
stringr += fly ;


for ( double x = stringr ; x < inside ; x += stringr*2+gap )
   {
   for ( double y = stringr ; y < inside ; y += stringr*2+gap )
      {
      if ( (y+gap)*(y+gap) + (x+gap)*(x+gap) < inside2 )
         {
         open += hole ;
         }
      else if ( (y)*(y) + (x)*(x) >= inside2 )
         {
         break ;
         }
      else
         {
         double yintercept = sqrt ( inside2 - x*x ) ;
         if ( yintercept > y+gap ) 
            yintercept = y+gap ;
         double xintercept = sqrt ( inside2 - y*y ) ;
         if ( xintercept > x+gap ) 
            xintercept = x+gap ;
         

         if ( xintercept >= x+gap )
            {
            if ( yintercept >= y+gap )
               {       // both sides whole
               xintercept = sqrt ( inside2 - (y+gap)*(y+gap) ) ;
               yintercept = sqrt ( inside2 - (x+gap)*(x+gap) ) ;
//               cout << xintercept << " " << yintercept << endl ;

               double a = 
                  gap*(yintercept-y) 
                  + gap*(xintercept-x) -
                  (xintercept-x)*(yintercept-y) ;
               
//               cout << "a = " << a << endl ;
               double a1 = atan2 ( yintercept , x+gap ) ;
               double a2 = atan2 ( y+gap , xintercept ) ;
               double arc = abs ( a1-a2 ) * inside ;
               double sector = arc * inside / 2 ;

//                cout << "sector = " << sector << endl ;
//                cout << "triangles " 
//                     << tri ( xintercept , yintercept , xintercept , y+gap ) 
//                     << " " 
//                     << tri ( xintercept , yintercept , x+gap , yintercept )  
//                     << endl ;
               
               a += sector 
                  - tri ( xintercept , yintercept , xintercept , y+gap ) 
                  - tri ( xintercept , yintercept , x+gap , yintercept )  ;
               
               open += 4*a ;
               }
            else
               {       // 
               double yintercept2 = sqrt ( inside2 - (x+gap)*(x+gap) ) ;
               double a1 = atan2 ( yintercept , x ) ;
               double a2 = atan2 ( yintercept2 , x+gap ) ;
               double arc = abs ( a1-a2 ) * inside ;
               double sector = arc * inside / 2 ;
               
               double a = sector 
                  - tri ( x , yintercept2 , x+gap , yintercept2 ) 
                  - tri ( x , yintercept2 , x , yintercept ) ;
               
               a += (yintercept2-y)*gap ;

               open += a * 4 ;
               }
            }
         else
            {
            if ( yintercept >= y+gap )
               {
               double xintercept2 = sqrt ( inside2 - (y+gap)*(y+gap) ) ;
               double a1 = atan2 ( y , xintercept ) ;
               double a2 = atan2 ( y+gap , xintercept2 ) ;
               double arc = abs ( a1-a2 ) * inside ;
               double sector = arc * inside / 2 ;
               
               double a = sector 
                  - tri ( xintercept2 , y , xintercept2 , y+gap ) 
                  - tri ( xintercept2 , y , xintercept , y ) ;
               
               a += (xintercept2-x)*gap ;
               
               open += a * 4 ;
               }
            else
               {           // neither side whole
               double a1 = atan2 ( y , xintercept ) ;
               double a2 = atan2 ( yintercept , x ) ;
               double arc = abs ( a1-a2 ) * inside ;
               double sector = arc * inside / 2 ;
               
               double a = sector - tri ( x , y , x , yintercept ) 
                  - tri ( x , y , xintercept , y ) ;
               
               open+= a * 4 ;
               //cout << endl << "a = " << a << " hole = " << hole << endl ;
               
               }
            }
         
         }
      }
   }
// cout << "gap = " << gap << " inside = " << inside 
//      << " stringr = " << stringr 
//      << " area = " << area << " open = " << open
//      << endl ;
// cout << endl ;

return (area-open)/area ;
}


void docase ( int caseno ) 
{
double prob = getprob(caseno) ;
prob += 0.0000005 ;
cout << "Case #" << caseno+1 << ": " ;
if ( prob < 0 ) cout << prob << endl ;


int ip = (int) prob ;
ip = (int) prob ;
cout << ip ;
prob -= ip ;
prob *= 10 ;
cout << "." ;
for ( int j = 0 ; j < 6 ; j ++ )
   {
   ip = (int) prob ;
   cout << ip ;
   prob -= ip ;
   prob *= 10 ;
   }
cout << endl ;
}


int main ( int argc , char ** argv )
{
int cn ;

cin >> cn ;

for ( int c = 0 ; c < cn ; c ++ )
   docase ( c ) ;
}

