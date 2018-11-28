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
void do_case ( int cas )
// ****************************************************************************
{
cout << "Case #" << cas << ": " ;
int n , k ;
cin >> n >> k ;


int p = (1<<(n)) ;
//cerr << "period " << p << endl ;

if ( k%p == p-1 )
    cout << "ON" ;
else
    cout << "OFF" ;

//cerr << " modulus = " << (k%p) << endl ;


// char state [32] ;
// char next [32] ;
// char power [32] ;
// for ( int i = 0 ; i <= n ; i ++ )
//    power[i] = state[i] = 0 ;
// power[0] = 1 ;

// // cerr << 0 << ":: " ;
// // for ( int j = 0 ; j < n ; j ++ )
// //    cerr << (int) state[j] << " " ;
// // cerr << endl ;

// for ( int i = 0 ; i < k ; i ++ )
//    {
//    int a = 1 ;
//    next[0] = ! state[0] ;
//    while ( state[a-1] )
//       {
//       next[a] = ! state[a] ;
//       a ++ ;
//       }
//    while ( a < n )
//       {
//       next[a] = state[a] ;
//       a ++ ;
//       }
//    for ( int j = 0 ; j < n ; j ++ )
//       state[j] = next[j] ;
   

//     cerr << (i+1) << ":: " ;
//     for ( int j = 0 ; j < n ; j ++ )
//        cerr << (int) state[j] << " " ;
//     cerr << endl ;
   
//    }
// // cerr << enld ;

// int answer = 1 ;
// for ( int i = 0 ; i < n ; i ++ )
//    if ( state[i] == 0 )
//       answer = 0 ;

// cout << ( answer ? "ON" : "OFF" ) ;


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
