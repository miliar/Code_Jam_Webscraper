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
#include <set>
#include <map>
#include <queue>
#include <list>
#include <cstdlib>
#define enld endl
using namespace std ;
// ****************************************************************************
int getchar ( )
// ****************************************************************************
{
if ( cin.eof() )
   return -1 ;
int ch = cin.get() ;
if ( cin.fail() )
   return -1 ;
return ch ;
}
// ****************************************************************************
string tokenstartchars 
    = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" ;
string tokenchars 
    = ".0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" ;
// ****************************************************************************
string gettoken ( )
// ****************************************************************************
{
int ch ;

ch = cin.get() ;

while ( ! cin.eof () && (ch == ' ' || ch == '\n') )
   ch = getchar ( ) ;

if ( ch == -1 )
   return "ERROR" ;

string ans = "" ;
if ( tokenstartchars.find( (char) ch ) != string::npos ) 
   {
   while ( tokenchars.find ( (char) ch ) != string::npos)
      {
      ans.push_back((char) ch) ;
      ch = getchar ( ) ;
      }
   cin.putback((char)ch) ;
   return ans ;
   }

ans = "" ;
ans.push_back ( (char) ch ) ;
return ans ;
}
// ****************************************************************************
double getdouble ( ) 
// ****************************************************************************
{
double a ;
cin >> a ;
return a ;
}
// ****************************************************************************
int getint ( ) 
// ****************************************************************************
{
while ( cin.peek ( ) == ' ' || cin.peek ( ) == '\n' )
   getchar ( ) ;
int sign = 1 ;
if ( cin.peek ( ) == '-' )
   {
   sign = -1 ;
   getchar ( ) ;
   }
string toke = gettoken ( ) ;
if ( sign == -1 && toke == "2147483648" )
   return -2147483648 ;

return sign * atoi ( toke.c_str() ) ;
}
// ****************************************************************************
long long d [1000] ;
// ****************************************************************************
long long gcd ( long long a , long long b ) 
// ****************************************************************************
{
if ( a > b ) return gcd ( b , a ) ;
if ( b % a == 0 ) return a ;
return gcd ( b%a , a ) ;
}
// ****************************************************************************
void do_case ( int cas )
// ****************************************************************************
{
cout << "Case #" << cas << ": " ;
int n ;
cin >> n ;

for ( int i = 0 ; i < n ; i ++ )
   cin >> d[i] ;

sort ( d , d+n ) ;

int m = 0 ;
while ( d[m+1] == d[0] )
   m++ ;
for ( int i = m ; i > 0 ; i-- )
   d[i] = d[m+1] ;


long long g ;

if ( n == 2 )
   
   g = d[1] - d[0] ;
else
   {
   for ( int i = 1 ; i < n ; i ++ )
      d[i] -= d[0] ;

   g = gcd ( d[1] , d[2] ) ;

   for ( int i = 3 ; i < n ; i ++ )
      g = gcd ( g , d[i] ) ;
   }

long long now = d[0] % g ;

if ( now == 0 )
   cout << 0 ;
else
   cout << g-now ;

cout << endl ;
}
// ****************************************************************************
int main ( int argc , char ** argv )
// ****************************************************************************
{
int n ;
cin >> n ; getchar() ;
for ( int i = 1 ; i <= n ; i ++ )
   do_case ( i ) ;
}
// ****************************************************************************
