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
void do_case ( int cas )
// ****************************************************************************
{
cout << "Case #" << cas << ": " ;
char n [1000];
char m [1000] ;
cin >> n ;
int len = strlen ( n ) ;

for ( int i = 0 ; i < len ; i ++ )
   m[i] = n[i] ;
m[len] = 0 ;

int zeros = 0 ;

for ( int i = 0 ; i < len ; i ++ )
   if ( n[i] == '0' )
      zeros ++ ;

int zerosend = 1 ;
for ( int i = 0 ; i < zeros ; i ++ )
   if ( n[i] != '0' )
      zerosend = 0 ;


sort ( m , m+len ) ;
for ( int i = 0 ; i < len ; i ++ )
   if ( n[i] != m[len-i-1] ) 
      {
      next_permutation ( n , n+len ) ;
      cout << n << endl ;
      return ;
      }


sort ( n , n+len ) ;
cout << n[zeros] ;
for ( int i = 0 ; i <= zeros ; i ++ )
   cout << "0" ;
cout << n+1+zeros ;
cout << endl ;
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
