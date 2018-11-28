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
int mass [500][500] ;
// ****************************************************************************
void do_case ( int cas )
// ****************************************************************************
{
cout << "Case #" << cas << ": " ;
int r , c , d ;
cin >> r >> c >> d ;
for ( int i = 0 ; i < r ; i ++ )
   {
   string ln ;
   cin >> ln ;
   for ( int j = 0 ; j < c ; j ++ )
      mass[i][j] = ln[j]-'0' ;
   }

// cerr << endl ;
// for ( int i = 0 ; i < r ; i ++ )
//    {
//    for ( int j = 0 ; j < c ; j ++ )
//       cerr << mass[i][j];
//    cerr << endl ;
//    }


int biggest = 0 ;
int sstart = 3 ;

for ( int xc = 0 ; xc < r-1 ; xc ++ )
   for ( int yc = 0 ; yc < c-1 ; yc ++ )
      for ( int s = sstart ; xc+s <= c && yc+s <= r ; s ++ )
         {
         double cgx = 0 ;
         double cgy = 0 ;
         double px = xc+(s-1)*0.5 ;
         double py = yc+(s-1)*0.5 ;
         for ( int y = yc ; y < yc+s ; y ++ )
            for ( int x = xc ; x < xc+s ; x ++ )
               {
               cgx += mass[y][x]*(x-px) ;
               cgy += mass[y][x]*(y-py) ;
               }
         cgx -= mass[yc][xc] * ( xc-px) ;
         cgy -= mass[yc][xc] * ( yc-py) ;
         
         cgx -= mass[yc][xc+s-1] * ( xc+s-1-px) ;
         cgy -= mass[yc][xc+s-1] * ( yc-py) ;
         
         cgx -= mass[yc+s-1][xc] * ( xc-px) ;
         cgy -= mass[yc+s-1][xc] * ( yc+s-1-py) ;
         
         cgx -= mass[yc+s-1][xc+s-1] * ( xc+s-1-px) ;
         cgy -= mass[yc+s-1][xc+s-1] * ( yc+s-1-py) ;
         
         //cerr << xc << "," << yc << " s = " << s << " " << cgx << " " << cgy << endl ;
         
         if ( abs(cgx) < 0.001 && abs(cgy) < 0.001 && biggest < s )
            {
            biggest = s ;
            //sstart = s + 1 ;
            }
         }

if ( biggest > 0 ) 
   cout << biggest << endl ;
else
   cout << "IMPOSSIBLE" << endl ;
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
