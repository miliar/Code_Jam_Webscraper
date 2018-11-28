#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <windows.h>
using namespace std;

#define le 20000005

bool vis[le];

int A , B;

int rec[20];

void solve ( int a , int b ){
     int i , cnt = 0 , k;
     char ar[20] , tmp[20] ; int  m;
     memset ( vis , 0 , sizeof ( vis ) );
     for ( i = a ; i <= b ; i++ ){
         memset ( ar , 0 , 20 );
         sprintf ( ar , "%d" , i );
         //puts(ar);
         int len = ( int ) strlen ( ar );
         k = 0;
         for ( int j = 0 ; j < len ; j++ ){
             ar[j + len] = ar[j];
             ar[j + len + 1] = 0;
             sscanf ( ar + j + 1 , "%d" , &m );
             //printf ( "%d\n" , m );
             if ( !vis[m] && m <= b && m > i) vis[m] = true , cnt++ , rec[k++] = m ;
         }
         for ( int j = 0 ; j < k ; j++ ){
             vis[rec[j]] = false;
         }
     }  
     printf ( "%d\n" , cnt );   
}

int main (void){
    freopen("C-large (1).in", "r", stdin);
    freopen("C.out", "w", stdout);
    int cas , i;
    scanf ( "%d" , &cas );
    for ( i = 1 ; i <= cas ; i++ ){
        scanf ( "%d%d" , &A , &B );
        printf ( "Case #%d: " , i );
        solve ( A , B );
    }
    //system ( "pause" );
    return 0;    
}
