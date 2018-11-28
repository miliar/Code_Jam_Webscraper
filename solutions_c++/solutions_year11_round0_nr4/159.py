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
double f(int n )
// ****************************************************************************
{
int a = 1 ;
while ( n > 1 )
   {
   a *= n ;
   n -- ;
   }
return a ;
}
// ****************************************************************************
double choose ( int n , int k )
// ****************************************************************************
{
return f(n)/(f(k)*f(n-k)) ;
}
// ****************************************************************************
double derangements ( int n ) 
// ****************************************************************************
{
double p = 0 ;
double s = 1 ;
for ( int k = 0 ; k <= n ; k ++ )
   {
   p += s / f(k) ;
   s = -s ;
   }
return f(n)*p ;
}
// ****************************************************************************
void do_case ( int cas )
// ****************************************************************************
{
cout << "Case #" << cas << ": " ;
int n ;
cin >> n ;
vector<int> perm (n) ;

for ( int i = 0 ; i < n ; i ++ )
   cin >> perm[i] ;

// for ( int i = 0 ; i < n ; i ++ )
//    cout << perm[i] << endl ;

double ans = 0 ;

vector<int> cycle ( n ) ;

for ( int i = 0 ; i < n ; i ++ )
   cycle[i] = -1 ;


for ( int st = 0 ; st < n ; st ++ )
   if ( cycle[st] == -1 )
      {
      int p = st ;
      int c = 1 ;
      while ( perm[p] != st+1 )
         {
         p = perm[p]-1 ;
         cycle[p] = 0 ;
         c ++ ;
         }
      cycle[st] = ((c==1) ? 0 : c) ;
      }

// for ( int i = 0 ; i < n ; i ++ )
//    cout << cycle[i] << " " ;
// cout << endl ;
for ( int i = 0 ; i < n ; i ++ )
   ans += cycle[i] ;

cout << ans << ".000000" << endl ;
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
