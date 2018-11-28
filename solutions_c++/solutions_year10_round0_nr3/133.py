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
int g [ 1000 ] ;
// ****************************************************************************
void do_case ( int cas )
// ****************************************************************************
{
cout << "Case #" << cas << ": " ;
int runs , cap , groups ;
cin >> runs >> cap >> groups ;
for ( int i = 0 ; i < groups ; i ++ )
   cin >> g[i] ;

cerr << "doing " << cas << endl ;

long long tr = 0 ;
int onboard = 0 ;
long long cash = 0 ;
long long gon = 0 ;

do 
   {
   for ( int i = 0 ; i < groups ; i ++ )
      {
      if ( cap-onboard >= g[i] && gon < groups )
         {
         onboard += g[i] ;
         gon ++ ;
         }
      else
         {
         cash += onboard ;
         tr ++ ;
         onboard = g[i] ;
         gon = 1 ;
         }
      if ( tr == runs )
         {
         cout << cash << endl ;
         return ;
         }
      }
   }  while ( onboard + g[0] <= cap && gon < groups ) ;
cash += onboard ;
tr ++ ;

// if ( cas == 46 )
//    {
//    cerr << "runs = " << runs << " cap = " << cap << " groups = " << groups << endl ;
//    cerr << "cash = " << cash 
//         << " tr = " << tr 
//         << " gon = " << gon 
//         << " onbaord = " << onboard << " g[0] = " << g[0] 
//         << endl ;
//    }

long long full_cycles = runs / tr ;
tr *= full_cycles ;
cash *= full_cycles ;

// if ( cas == 16 )
//    {
//    cerr << "runs = " << runs << " cap = " << cap << " groups = " << groups << endl ;
//    cerr << "cash = " << cash 
//         << " tr = " << tr 
//         << " gon = " << gon 
//         << endl ;
//    }

gon = 0 ;
onboard = 0 ;

do 
   {
   for ( int i = 0 ; i < groups ; i ++ )
      {
      if ( cap-onboard >= g[i] && gon < groups )
         {
         onboard += g[i] ;
         gon ++ ;
         }
      else
         {
         cash += onboard ;
         tr ++ ;
         onboard = g[i] ;
         gon = 1 ;
         }
      if ( tr == runs )
         {
         cout << cash << endl ;
         return ;
         }
      }
   } while ( onboard + g[0] <= cap && groups ) ;




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
