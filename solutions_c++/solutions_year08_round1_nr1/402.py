#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std ;


void do_case ( int c )
{
cout << "Case #" << c+1 << ": " ;

int n ;
cin >> n ;
vector<int> v1 (n) ;
vector<int> v2 (n) ;

for ( int i = 0 ; i < n ; i ++ )
   cin >> v1[i] ;
for ( int i = 0 ; i < n ; i ++ )
   cin >> v2[i] ;

sort(v1.begin(),v1.end()) ;
sort(v2.begin(),v2.end()) ;

long long s = 0 ;
for ( int i = 0 ; i < n ; i ++ )
   s += (long long) v1[i] * (long long )v2[n-i-1] ;

cout << s << endl ;
}



int main ( int argc , char ** argv )
{
int n ;

cin >> n ;

for ( int i = 0 ; i < n ; i ++ )
   {
   do_case ( i ) ;
   }
}
