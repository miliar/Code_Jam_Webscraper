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
void do_case ( )
// ****************************************************************************
{
int L , D , N , count = 0 ;

cin >> L >> D >> N ;

vector<string> dict (D) ;

for ( int i = 0 ; i < D; i ++ )
   cin >> dict[i] ;

system ( "/bin/rm -rf temp" ) ;
system ( "mkdir temp" ) ;
for ( int i = 0 ; i < D; i ++ )
   {
   FILE * f = fopen ( ("temp/"+dict[i]).c_str() , "w" ) ;
   fclose(f) ;
   }


string pat ;

for ( int cas = 0 ; cas < N ; cas ++ )
   {
   string regexp = "" ;
   cin >> pat;
   for ( int i = 0 ; i < pat.size() ; i ++ )
      if ( pat[i] == '(' )
         regexp.push_back ( '[' ) ;
      else if ( pat[i] == ')' )
         regexp.push_back ( ']' ) ;
      else 
         regexp.push_back ( pat[i] ) ;
   
   system ( ("/bin/ls temp/"+regexp+ " | wc > ans.txt").c_str() ) ;
   
   ifstream ansfile ( "ans.txt" ) ;
   ansfile >> count ;
   ansfile.close() ;
      
   cout << "Case #" << cas+1 << ": " ;
   cout << count << endl ;
   }
}
// ****************************************************************************
int main ( int argc , char ** argv )
// ****************************************************************************
{
do_case ( ) ;
}
// ****************************************************************************







