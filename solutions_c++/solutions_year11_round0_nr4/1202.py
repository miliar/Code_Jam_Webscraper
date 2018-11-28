#include<stdio.h>

int main( void ){
    
    int n,m,i,j,k,t,sum;
    FILE *fin = fopen( "in4.txt" , "r" );
    FILE *fout = fopen( "ans4.txt" , "w" );
    
    fscanf( fin , "%d" , &n );
    for( i = 0 ; i < n ; i++ ){
        
        fscanf( fin , "%d" , &m );
        sum = 0;
        for( j = 1 ; j <= m ; j++ ){
            fscanf( fin , "%d" , &t );
            if( t != j ) sum ++;
        }
        
        fprintf( fout , "Case #%d: %d.000000\n" , i+1 , sum );
        
    }
    
    return 0;
    
}
