#include<cstdio>
#include<cstdlib>


int main()
{
//    freopen(  "A-small-attempt0.in" , "r" , stdin );
//    freopen(  "A-small-attempt01.out" , "w", stdout );
    freopen(  "A-large.in" , "r" , stdin );
    freopen(  "A-large.out" , "w", stdout );
    int iCase , nCase;
    int nN , kN;
    scanf( "%d" , &nCase );
    for( iCase = 0; iCase < nCase; ++iCase ){
        scanf( "%d%d" ,&nN , &kN );
        if( ( kN + 1 ) % ( 1 << nN ) == 0 ){
            printf( "Case #%d: ON\n" , iCase + 1 );
        }else{
            printf( "Case #%d: OFF\n" , iCase + 1 );
        }
    }
    return 0;
}

