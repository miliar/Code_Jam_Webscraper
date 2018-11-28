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
class Foo {
public:
double prob ;
string name ;
Foo * gotit ;
Foo * aintgotit ;
} ;
// ****************************************************************************
// ****************************************************************************
string gettoken ( )
// ****************************************************************************
{
int ch ;

ch = cin.get() ;

while ( ! cin.eof () && (ch == ' ' || ch == '\n') )
   ch = cin.get ( ) ;

if ( cin.eof() )
   return "error" ;

if ( ch == '(' )
   {
//    cout <<"(" <<endl ;;
   return "(" ;
   }
if ( ch == ')' )
   {
//    cout <<")" <<endl ;;
   return ")" ;
   }

string ans = "" ;
while ( ch == '.' || ch >= '0' && ch <= '9'
        || ch >= 'a' && ch <= 'z'
        || ch >= 'A' && ch <= 'Z' )
   {
   ans.push_back((char) ch) ;
   ch = cin.get ( ) ;
   }
// cout << ans << endl ;
return ans ;
}
// ****************************************************************************
Foo * parse ( ) 
// ****************************************************************************
{
Foo * me = new Foo ( ) ;
me-> gotit = me->aintgotit = NULL ;
me -> name = "NONE" ;


cin >> me -> prob ;
// cout << "Prob " << me->prob << endl ;

string toke = gettoken ( ) ;
//      cout << " open or name " << toke << endl ;

if ( toke==")" ) 
     return me ;

//      cout << " name " << toke << endl ;
     me->name = toke ;
     toke = gettoken ( ) ;
//      cout << " open " << toke << endl ;
     me->gotit = parse ( ) ;

     toke = gettoken ( ) ;
//      cout << " open " << toke << endl ;
     
     me->aintgotit = parse ( ) ;
     gettoken ( ) ;
     
     return me ;
     
}
// ****************************************************************************
void print ( Foo * here , string indent )
// ****************************************************************************
{
 cout << indent << "( " << here->prob ;

if ( here-> gotit )
   {
    cout << " " << here-> name << endl ;
   print ( here->gotit , indent + "    " ) ;
   print ( here->aintgotit , indent + "    " ) ;
   }
cout << indent << ")" << endl ;
}
// ****************************************************************************
void do_case ( int cas )
// ****************************************************************************
{
int lines ;
cin >> lines ;
// cout << " lines = " << lines << endl ;

cout << "Case #" << cas << ": " ;
cout << endl ;

string start = gettoken ( ) ;
// cout << " start token " << start << endl ;

Foo * tree = parse ( ) ;
// print ( tree , "") ;


Foo * here ;
//start = gettoken ( ) ;
// cout << "crap" << endl ;


int n ;
cin >> n ;
// cout << "n=" << n << endl ;;

vector<string> props (100);

for (  int i = 0 ; i < n ; i ++ )
   {
   start = gettoken ( ) ;
   if ( start == ")" ) start = gettoken() ;
   
// cout << "example= " << start << endl ;
   int k ;
   cin >> k ;
//    cout << "k=" << k << endl ;
//       cout << k << endl ;
   for ( int j = 0 ; j < k ; j ++ )
      {
//       cout << j << endl ;
      
      props[j] = gettoken ( ) ;
//       cout << "prop" << j << "  " << props[j] << endl ;      
      }
   

   here = tree ;
   double prob = 1.0 ;
   
   while ( here )
      {
      prob *= here -> prob ;
//       cout << "testing " << here->name << "  " << here->prob << endl ;
      if ( here->gotit )
         {
//          cout << "testing " << here->name << endl ;
         int found = 0 ;
         for ( int j = 0 ; j < k ; j ++ )
            if ( props[j] == here->name )
               found = 1 ;
         
         if ( found ) here = here->gotit ;
         else here = here->aintgotit ;
         }
      else
         here = NULL ;
      }

   if( prob > 0.9999995 ) 
      cout << "1.0" ;
   else
      {
      cout << "0." ;
      int pr = (int) ( prob * 10000000 + 0.5 ) ;
      printf ( "%07d" , pr ) ;
      }
   cout << endl ;
   }
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
