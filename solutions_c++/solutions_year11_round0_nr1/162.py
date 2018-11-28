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

int n ;
cin >> n ;
// cout <<" n = " << n <<endl ;

vector<int> b ;
vector<char> c ;

b.resize(n) ;
c.resize(n) ;

string col ;
for ( int i = 0 ; i < n ; i ++ )
   {
   cin >> col >> b[i] ;
   c[i] = col[0] ;
   }

// for ( int i = 0 ; i < n ; i ++)
//    cout << b[i] << " " << (char)(c[i]) << endl ;

int op = 1 ;
int bp = 1 ;
int bn = 0 ;
int nextb = 0 ;
int nexto = 0 ;
int steps = 0 ;

while ( bn < n )
   {
   //   cout << "button " << bn << " pos " << bp << " " << op << endl ;
   for ( int i = bn ; i < n ; i ++ )
      if ( c[i] == 'O' )
         {
         nexto = b[i] ;
         break ;
         }
   for ( int i = bn ; i < n ; i ++ )
      if ( c[i] == 'B' )
         {
         nextb = b[i] ;
         break ;
         }
   //   cout << " next " << nextb << " " << nexto << endl ;
   
   if ( op == b[bn] && c[bn] == 'O' )
      {
      if ( nextb > bp ) bp ++ ;
      else if ( nextb < bp ) bp -- ;
      bn ++ ;
      }
   else if ( bp == b[bn] && c[bn] == 'B' )
      {
      if ( nexto > op ) op ++ ;
      else if ( nexto < op ) op -- ;
      bn ++ ;
      }
   else
      {
      if ( nextb > bp ) bp ++ ;
      else if ( nextb < bp ) bp -- ;
      if ( nexto > op ) op ++ ;
      else if ( nexto < op ) op -- ;
      }
   steps ++ ;
   }

cout << steps << endl ;
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
