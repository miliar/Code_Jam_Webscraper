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
int totallen , walk , run , maxrun , n ;
cin >> totallen >> walk >> run >> maxrun >> n ;
vector<int> st (n);
vector<int> en (n) ;
vector<int> sp (n) ;

for ( int i = 0 ; i < n ; i ++ )
   cin >> st[i] >> en[i] >> sp[i] ;


int p = 0 ;
double z = 0 ;
double time = 0 ;
for ( int i = 0 ; i < n ; i ++ )
   {
   z += st[i] - p;
   p = en[i] ;
   }
z += totallen - en[n-1] ;


double mrun = maxrun ;
double runt ;
double zrunt ;
zrunt = z/(double)run ;

if ( mrun >= zrunt )
   runt = zrunt ;
else
   runt = maxrun ;

//cerr << z << " runt 0 = " << runt <<endl ;

time += runt ;

//cerr << "walk time = " << (z - (runt*run)) / walk << endl ;
time += (z - (runt*run)) / walk ;

mrun -= runt ;

//cerr << "time = " << time << endl ;
//cerr << "---------"  << endl ;

for ( int s = 0 ; s <= 100 ; s ++ )
   {
   z = 0 ;
   for ( int i = 0 ; i < n ; i ++ )
      if ( sp[i] == s )
         {
         z += en[i]-st[i] ;
         }
   zrunt = z/((double)run+s) ;
   
   if ( mrun >= zrunt )
      runt = zrunt ;
   else
      runt = mrun ;
   

   if ( z > 0 )  
      {
      //cerr << "z = " << z << " mrun = " << mrun << endl ;
      
      //cerr << z << " runt " << s << " = " << runt <<endl ;
      time += runt ;
      //cerr << "walk time = " << (z-(runt*(run+s))) / (walk+s) << endl ;
      
      time += (z-(runt*(run+s))) / (walk+s) ;
      mrun -= runt ;
      //cerr << "time = " << time << endl ;
      }
   
   }

char buf [1000] ;
sprintf ( buf , "%25.7f" , time ) ;
char * b = & buf[0] ;

while ( *b == ' ' ) b++ ;


cout << b << endl ;
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
