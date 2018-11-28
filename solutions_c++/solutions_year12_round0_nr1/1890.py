#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <windows.h>
using namespace std;

#define le 200

char tb[] = "yhesocvxduiglbkrztnwjpfmaq";

char str[le];

void solve ( char *sr ){
     int i , n = ( int ) strlen ( sr );
     for ( i = 0 ; i < n ; i++ ){
         if ( sr[i] >= 'a' && str[i] <= 'z' ) putchar ( tb[sr[i] - 'a'] );
         else putchar ( sr[i] );    
     }
     puts ( "" );
}
     
int main (void){
    freopen ( "A-small-attempt4.in" , "r" , stdin );
    freopen ( "A-small-attempt4.out" , "w" , stdout );
     int cas , i;
     scanf ( "%d" , &cas );
     getchar();
     for ( i = 1 ; i <= cas ; i++ ){
         gets ( str );
         printf ( "Case #%d: " , i );
         solve ( str );
     } 
  //   system ( "pause" ); 
     return 0;
}
