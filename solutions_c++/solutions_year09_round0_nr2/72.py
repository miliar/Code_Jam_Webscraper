// ****************************************************************************
// Code developed starting from Rustyoldman's Google Code jam template
// ****************************************************************************
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <cmath>
#include <algorithm>
#define enld endl
using namespace std ;
// watershed problem google code jam 2009 qual
// ****************************************************************************
void do_case ( int cas )
// ****************************************************************************
{
cout << "Case #" << cas << ": " ;
cout << endl ;

int h , w ;
cin >> h >> w ;

int * alt = new int [h*w] ;
int * down = new int [h*w] ;
char * b = new char [h*w] ;

for ( int i = 0 ; i < h*w ; i ++ )
   {
   cin >> alt [i] ;
   down[i] = i ;
   b[i] = '#' ;
   }


for ( int yi = 0 ; yi < h ; yi ++ )
   for ( int xi = 0 ; xi < w ; xi ++ )
      {
      int x = xi ;
      int y = yi ;
      int lowest ;
      int bottom ;
      int here ;
      
      
      if ( down[x+y*w] == x+y*w )
         {
         do 
            {
            lowest = alt[x+y*w] ;
            
            // north
            if ( y > 0 && alt[x+y*w-w] < lowest )
               {
               lowest = alt[x+y*w-w] ;
               down [x+y*w]= x+y*w-w ;
               }
            // west
            if ( x > 0 && alt[x+y*w-1] < lowest )
               {
               lowest = alt[x+y*w-1] ;
               down [x+y*w]= x+y*w-1 ;
               }
            // east
            if ( x < w-1 && alt[x+y*w+1] < lowest )
               {
               lowest = alt[x+y*w+1] ;
               down [x+y*w]= x+y*w+1 ;
               }
            // north
            if ( y < h-1 && alt[x+y*w+w] < lowest )
               {
               lowest = alt[x+y*w+w] ;
               down [x+y*w]= x+y*w+w ;
               }
            here = x+y*w ;
            x = down[here]%w ;
            y = down[here]/w ;
            } while ( lowest < alt[here] ) ;
         bottom = x+y*w ;
         x = xi ;
         y = yi ;
         do 
            {
            lowest = alt[x+y*w] ;
            
            // north
            if ( y > 0 && alt[x+y*w-w] < lowest )
               {
               lowest = alt[x+y*w-w] ;
               down [x+y*w]= x+y*w-w ;
               }
            // west
            if ( x > 0 && alt[x+y*w-1] < lowest )
               {
               lowest = alt[x+y*w-1] ;
               down [x+y*w]= x+y*w-1 ;
               }
            // east
            if ( x < w-1 && alt[x+y*w+1] < lowest )
               {
               lowest = alt[x+y*w+1] ;
               down [x+y*w]= x+y*w+1 ;
               }
            // north
            if ( y < h-1 && alt[x+y*w+w] < lowest )
               {
               lowest = alt[x+y*w+w] ;
               down [x+y*w]= x+y*w+w ;
               }
            here = x+y*w ;
            x = down[here]%w ;
            y = down[here]/w ;
            down[here] = bottom ;
            } while ( lowest < alt[here] ) ;
         }
      }



char cur = 'a' ;

for ( int yi = 0 ; yi < h ; yi ++ )
   for ( int xi = 0 ; xi < w ; xi ++ )
      {
      if ( b[down[xi+yi*w]] == '#' )
         b[down[xi+yi*w]] = (cur++) ;
      b[xi+yi*w] = b[down[xi+yi*w]] ;
      }


for ( int y = 0 ; y < h ; y ++ )
   {
   for ( int x = 0 ; x < w ; x ++ )
      {
      if ( x > 0 ) cout << " " ;
      cout << b[x+y*w] ;
      }
   cout << endl ;
   }
}
// ****************************************************************************
int main ( int argc , char ** argv )
// ****************************************************************************
{
int n ;
cin >> n ;
for ( int i = 1 ; i <= n ; i ++ )
   do_case ( i ) ;
}
// ****************************************************************************
