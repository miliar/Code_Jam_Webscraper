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
int trans ;
cin >> trans ;
vector<string> tran ( trans ) ;
for ( int i = 0  ; i < trans ; i ++ )
   cin >> tran[i] ;

int opos ;
cin >> opos ;
vector<string> opo ( opos ) ;
for ( int i = 0 ; i < opos ; i ++ )
   cin >> opo[i] ;


int spells ;
cin >> spells ;
string ispell ;
cin >> ispell ;

string spell ;



int e ;
int good = 1 ;

spell.push_back ( ispell[0] ) ;
for ( int el = 1 ; el < spells ; el ++ )
   {
   spell.push_back ( ispell[el] ) ;
   
   good = 1 ;
   while ( good )
      {
      good = 0 ;
      for ( int t = 0 ; t < trans ; t ++ )
         if ( spell.size() >= 2 )
            {
            e = spell.size() - 1 ;
            if ( spell[e] == tran[t][0] && spell[e-1] == tran[t][1] ||
                 spell[e-1] == tran[t][0] && spell[e] == tran[t][1] )
               {
               spell.resize(e) ;
               spell[e-1] = tran[t][2] ;
               good = true ;
               }
            }
      }
   
   e = spell.size() - 1 ;
   for ( int i = 0 ; i <= e ; i ++ )
      for ( int j = 0 ; j <= e ; j ++ )
         for ( int o = 0 ; o < opos ; o ++ )
            if ( spell[i] == opo[o][0] && spell[j] == opo[o][1] )
               {
               spell.clear() ;
               goto done ;
               }
   done:
   continue ;
   }

cout << "[" ;
for ( int i = 0 ; i < spell.size() ; i ++ )
   if ( i == 0 )
      cout << spell[i] ;
   else
      cout << ", " << spell[i] ;
cout << "]" << endl ;
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
