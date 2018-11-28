#include<stdio.h>
#include<string.h>

int temp[ 15 ] ,ini[ 15 ] , num1[ 15 ] ,num2[ 15 ] ,tem[ 15 ] , ini1[ 15 ];


int _judge( int * a , int *b ,int num )
{
    for( int i = 0 ;i < num ;i++ )
    if( a[i] != b[i] )
        return 0;
    return 1;
}
int judge( int a , int b )
{
    memset( temp , 0 , sizeof( temp ) );
    memset( tem , 0 , sizeof( tem ) );
    memset( ini , 0 , sizeof( ini ) ) ;
    memset( ini1 , 0 , sizeof( ini1 ) ) ;
    memset( num1 , 0 , sizeof( num1 ) ) ;
    memset( num2 , 0 , sizeof( num2 ) ) ;
    int c1 = 0 ,c2 = 0;
    while( a )
    {
        temp[ c1++ ] = a % 10;
        num1[ a % 10 ] ++;
        a /= 10;
    }
    while( b )
    {
        ini[c2++] = b % 10;
        num2[ b % 10 ]++;
        b /= 10;
    }
    for( int i = 0 ;i < c2 ;i++ )
        ini1[i] = ini[ c2 - i - 1];
    if( c1 != c2 )
        return 0 ;

    for( int i = 0 ;i < 10 ;i++ )
        if( num1[i] != num2[i] )
        return 0;

    for( int i = c1 - 1 ;i >= 0 ; i-- )
    {
        int j = 0 ,k = i;
        while( j < c1 )
        {
            tem[j++] = temp[k];
            k --;
            if( k < 0  )
            k = c1 - 1;
        }
        if( _judge( tem , ini1 , c1 ) )
        return 1;
    }
    return 0;
}
int main()
{
    int A , B ,cnt ,cases ;
    freopen("C-small-attempt0.in" ,"r" ,stdin );
    freopen("C.txt" ,"w" ,stdout );
    scanf("%d" ,& cases );
    for( int t = 1 ; t <= cases ; t++ )
    {
        scanf("%d%d" , &A , &B );
        cnt = 0;
        printf("Case #%d: ", t );
        for( int i = A ; i <= B ;i++ )
        for( int j = i + 1 ;j <= B ; j++ )
        if( judge( i , j ) )
        cnt ++;
        printf("%d\n" ,cnt );
    }
    return 0;
}
