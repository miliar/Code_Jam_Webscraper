#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>

using namespace std ;

int docase ( int caseno )
{
char buff [1000] ;

map<string,int> tab ;

int nserver , nquery , ans , active ;
active = ans = 0 ;
cin >> nserver ;
vector<string> server ( nserver ) ;
vector<int> start ( nserver ) ;
cin.getline ( &buff[0] , 1000 ) ;
for ( int s = 0 ; s < nserver ; s ++ )
   {
   cin.getline ( &buff[0] , 1000 ) ;
   server[s] = buff ;
   start[s] = 0 ;
   tab[server[s]] = s ;
   //   cerr << "storing " << server[s] << endl ;
   }

cin >> nquery ;
cin.getline ( &buff[0] , 1000 ) ;

active = nserver ;
for ( int q =  0 ; q < nquery ; q ++ )
   {
   string query ;
   cin.getline ( &buff[0] , 1000 ) ;
   query = buff ;

   int s ;
   s = tab[query] ;
   //cout << "found " << server[s] << " " << s << " --  "  ;
   if ( start[s] == 0 )
      {
      active -- ;
      if ( active == 0 )
         {
         for ( int ss = 0 ; ss < nserver ; ss ++ )
            start[ss] = 0 ;
         active = nserver - 1 ;
         ans ++ ;
         }
      start[s] = q + 1 ;
      }
   //cout << active << endl ;
   }


cout << "Case #" << caseno+1 << ": " << ans << endl ;

}


int main ( int argc , char ** argv )
{
int cn ;

cin >> cn ;

for ( int c = 0 ; c < cn ; c ++ )
   docase ( c ) ;

}

