#include <iostream>
#include <iomanip>
#include <string>
#include <vector>

using namespace std ;

int docase ( int caseno )
{
int a [24*60] ;
int b [24*60] ;
char buff[1000] ;

int na , nb , ans_a , ans_b ;
int t ;

ans_a = ans_b = 0 ;

cin >> t ;
cin >> na >> nb ;
cin.getline ( &buff[0] , 1000 ) ;

for ( int i = 0 ; i < 24*60 ; i ++ )
   a[i] = b[i] = 0 ;


for ( int i = 0 ; i < na ; i ++ )
   {
   int st = 0 ;
   int en = 0 ;
   cin.getline ( &buff[0] , 1000 ) ;
   st = (buff[0]-'0' ) * 600 ;
   st += (buff[1]-'0' ) * 60 ;
   st += (buff[3]-'0' ) * 10 ;
   st += (buff[4]-'0' ) ;
   
   en = (buff[6]-'0' ) * 600 ;
   en += (buff[7]-'0' ) * 60 ;
   en += (buff[9]-'0' ) * 10 ;
   en += (buff[10]-'0' ) ;
   
   a[st] -- ;
   if ( en+t < 24*60 )
      b[en+t]++ ;
   }

for ( int i = 0 ; i < nb ; i ++ )
   {
   int st = 0 ;
   int en = 0 ;
   cin.getline ( &buff[0] , 1000 ) ;
   st = (buff[0]-'0' ) * 600 ;
   st += (buff[1]-'0' ) * 60 ;
   st += (buff[3]-'0' ) * 10 ;
   st += (buff[4]-'0' ) ;
   
   en = (buff[6]-'0' ) * 600 ;
   en += (buff[7]-'0' ) * 60 ;
   en += (buff[9]-'0' ) * 10 ;
   en += (buff[10]-'0' ) ;
   
   b[st] -- ;
   if ( en+t < 24*60 )
      a[en+t]++ ;
   }


int asum = 0 ;
int bsum = 0 ;
for ( int i = 0 ; i < 24*60 ; i ++ )
   {
   asum += a[i] ;
   if ( -asum > ans_a ) 
      ans_a = -asum ;
   bsum += b[i] ;
   if ( -bsum > ans_b ) 
      ans_b = -bsum ;
   }


cout << "Case #" << caseno+1 << ": " << ans_a << " " << ans_b << endl ;

}


int main ( int argc , char ** argv )
{
int cn ;

cin >> cn ;

for ( int c = 0 ; c < cn ; c ++ )
   docase ( c ) ;

}

