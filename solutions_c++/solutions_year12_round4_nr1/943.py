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
int best[10001] ;
int d [10001] ;
int L [10001] ;
// ****************************************************************************
void do_case ( int case_number )
// ****************************************************************************
{
int n , goal ;

cin >> n ;
for ( int i = 0 ; i < n ; i ++ )
   cin >> d[i] >> L[i] ;
cin >> goal ;

for ( int m = 0 ; m < n ; m ++ )
   best[m] = 0 ;
best[0] = d[0] ;

if ( d[0] * 2 >= goal )
   {
   cout << "Case #" << case_number << ": YES" ;
   cout << endl ;
   return ;
   }
for ( int i = 1 ; i < n ; i ++ )
   {
   if ( d[i]-d[0]<= best[0] )
      best[i] = min(d[i]-d[0],L[i]) ;
   else
      break ;
   }
for ( int m = 1 ; m < n ; m ++ )
   {
   if ( best[m] == 0 ) break ;
   if ( best[m] + d[m]>= goal )
      {
      cout << "Case #" << case_number << ": YES" ;
      cout << endl ;
      return ;
      }
   for ( int i = m+1 ; i < n ; i ++ )
      {
      if ( best[m] >= d[i]-d[m] && min(d[i]-d[m],L[i]) > best[i] )
         best[i] = min(d[i]-d[m],L[i]) ;
      }

   // for ( int i = 0 ; i < n ; i ++ )
   //    cout << best[i]<< " " ;
   // cout << endl ;
   }


cout << "Case #" << case_number << ": NO" ;
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
