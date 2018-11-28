#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std ;


void do_case ( int c )
{
cout << "Case #" << c+1 << ": " ;

int f , d ;
cin >> f >> d ;
//cout <<  "f = " << f << " cust = " << d << endl ;
vector< vector<int> > likes ;
char sm [101][101] ;
char su [101][101] ;
char sat [101] ;
for ( int g =  0 ; g < d ; g ++ )
   {
   for ( int i = 0 ; i < f+1 ; i ++ )
      su[g][i] = sm [g][i] = 0 ;
   int s ;
   cin >> s ;
   //   cout << "s = " << s << endl ;
   int malted ;
   int fl ;
   for ( int i = 0 ; i < s ; i ++ )
      {
      cin >> fl >> malted ;
      if ( malted ) 
         {
         //         cout << g << " " << fl << " malted" << endl ;
         sm[g][fl] = 1 ;
         }
      else
         {
         //         cout << g << " " << fl << " unmalted" << endl ;
         su[g][fl] = 1 ;
         }
      }
   }
// for ( int g = 0 ; g < d ; g ++ )
//    {
//    cout << g << "u: " ;
//    for ( int i = 0 ; i < f ; i ++ )
//       cout << (int)su[g][i+1] << ", " ;
//    cout << endl ;
//    cout << g << "m: " ;
//    for ( int i = 0 ; i < f ; i ++ )
//       cout << (int)sm[g][i+1] << ", " ;
//    cout << endl ;
//    }

int best = -1 ;
int leastm = 100 ;

int p = (1<<f) ;
//cout << f << " " << p << endl ;

for ( int b = 0 ; b < p ; b ++ )
   {
   for ( int g = 0 ; g < d ; g ++ )
      sat[g] = (char) 0 ;
   int mask = 1 ;
   for ( int bit = 0 ; bit < f ; bit ++ )
      {
      if ( ( mask & b ) != 0 )      
         {
         for ( int st = 0 ; st < d ; st ++ )
            if ( sm[st][bit+1] )
               sat[st] = 1 ;
         }
      else
         {
         for ( int st = 0 ; st < d ; st ++ )
            if ( su[st][bit+1] )
               sat[st] = 1 ;
         }
      mask += mask ;
      }
   int full = 1 ;
//    cout << b << ": " ;
   
//    for ( int g = 0 ; g < d ; g ++ )
//       cout << (int) sat[g] << " " ;
//    cout << endl ;
   for ( int g = 0 ; g < d ; g ++ )
      if ( ! sat[g] )
         {
         full = 0 ;
         break ;
         }
   if ( full )
      {
      int bc = 0 ;
      int tb = b ;
      while ( tb )
         {
         bc ++ ;
         tb = tb & ( tb-1 ) ;
         }
      if ( bc < leastm )
         {
         leastm = bc ;
         best = b ;
         }
      }
   
   }

if ( best == -1 )
   cout << "IMPOSSIBLE" ;
else
   for ( int i = 0 ; i < f ; i ++ )
      if ( (best & (1<<i)) != 0 )
         cout << "1 " ;
      else
         cout << "0 " ;

cout << endl ;
   }



int main ( int argc , char ** argv )
{
int n ;

cin >> n ;

for ( int i = 0 ; i < n ; i ++ )
   {
   do_case ( i ) ;
   }
}
