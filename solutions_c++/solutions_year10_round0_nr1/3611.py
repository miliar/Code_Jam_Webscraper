#include<stdio.h>
#include<stdlib.h>

int main()
{
    FILE* fin = fopen(  "A-large.in" , "r" );
    FILE* fout = fopen(  "A-large.out" , "w" ); 
    int i , t , n , k;
    fscanf( fin ,  "%d" , &t );
    i = 1;
    while( i <= t ){
        fscanf( fin, "%d%d" ,&n , &k );
        if( ( k + 1 ) % ( 1 << n ) ){
            fprintf( fout , "Case #%d: OFF\n" , i );
        }else{
            fprintf( fout , "Case #%d: ON\n" , i );
        }
        i++;
    }
    return 0;
}

