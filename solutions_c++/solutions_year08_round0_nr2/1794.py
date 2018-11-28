#include<cstdio>
#include<cstring>
#include<cstdlib>
#define MAXNUM 110
struct TM
{
    int st;
    int ed;
    int which;
    bool tk;
} schd[ MAXNUM ];

int wtt , abn , ban , alln , result;

int cmp( const void *a , const void *b )
{
    const TM * arg1 = ( TM* ) a;
    const TM * arg2 = ( TM* ) b;
    if ( arg1-> ed != arg2-> ed )
        return arg1->ed - arg2->ed;
    else
        return arg1->st - arg2-> st;
}
            
void readTm()
{
    int i , j , k  , hr1 , mn1 , hr2 , mn2;
    for( i = 0; i < alln; i++ ){
        scanf( "%d:%d%d:%d" , &hr1 , &mn1 , &hr2 , &mn2 );
        schd[ i ].st = hr1 * 60 + mn1;
        schd[ i ].ed= hr2 * 60 + mn2 + wtt;
        schd[ i ].which = ( i >= abn ) ? 1:0;
        schd[ i ].tk = 0;
    }
    
}
    
int main()
{
    int nCase, aCase , i , j , k , allLeft , current , bus[ 2 ];
    freopen( "quali_2_small.in" , "r"  , stdin );
    freopen( "quali_2_small.out" , "w" , stdout );
    scanf( "%d" , &nCase );
    for( aCase = 1; aCase <= nCase; aCase++ ){
        scanf( "%d" , &wtt );
        scanf( "%d%d" , &abn , &ban );
        alln = abn + ban;
        readTm();
        qsort( schd , alln , sizeof( TM ) , cmp );
        bus[ 1 ] = bus[ 0 ] = 0;
        for( allLeft = alln , result = 0  ; allLeft > 0 ; result ++ ){
            for( current = 0; schd[ current ].tk && current < alln ; current++ );
            if( current == alln ) break;
            bus[ schd[ current ].which ]++;
            allLeft--;
            schd[ current ].tk = 1;
            for( i = current +1 ; i < alln; i++ ){
                if( schd[ i ].tk == 0 && schd[ i ].which + schd[ current  ].which == 1 && schd[ i ].st >= schd[ current ].ed  ){
                    allLeft--;
                    schd[ i ].tk = 1;
                    current = i;
                }
            }
        }
        printf( "Case #%d: %d %d\n" , aCase , bus[ 0 ] , bus[ 1 ] );
    }
    return 0;
}

    
        

                
                
                
            
        
        



    
