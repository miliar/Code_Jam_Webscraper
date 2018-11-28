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
// ****************************************************************************
char * pat = "welcome to code jam" ;
int ways [500][27] ;
// ****************************************************************************
void do_case ( int cas )
// ****************************************************************************
{
char in [1000] ;
cout << "Case #" << cas << ": " ;

char ch = 'x' ;
int c = 0 ;

while ( ch > 20 )
   {
   cin.get(ch) ;
   in[c++] = ch ;
   }
in [c-1] = 0 ;
c-- ;

for ( int j = 0 ; j < 500 ; j ++ )
   for ( int i = 0 ; i < 20 ; i ++ )
      ways[j][i] = 0 ;


ways[0][0] = 1 ;
if ( in[0] == 'w' )
   ways[0][1] = 1 ;

for ( int pos = 1 ; pos < c ; pos ++ )
   {
//    cout << "pos = " << pos << ":  " ;
//    for ( int k = 0 ; k < 20 ; k ++ )
//       cout << ways[pos-1][k] << " " ;
//    cout << endl ;
   ways[pos][0] = 1 ;
   for ( int ml = 1 ; ml < 20 ; ml ++ )
      {
      ways[pos][ml] = ways[pos-1][ml] ;
      if ( in[pos] == pat[ml-1] )
         ways[pos][ml] = ( ways[pos][ml] + ways[pos][ml-1] ) % 10000 ;
      }
   }


   
cout << ways[c-1][19]/1000 
     << ways[c-1][19]/100 % 10 
     << ways[c-1][19]/10 % 10 
     << ways[c-1][19] % 10 
 ;

cout << endl ;
}
// ****************************************************************************
int main ( int argc , char ** argv )
// ****************************************************************************
{
int n ;
cin >> n ;
char ch ;
cin.get(ch) ;

for ( int i = 1 ; i <= n ; i ++ )
   do_case ( i ) ;
}
// ****************************************************************************
