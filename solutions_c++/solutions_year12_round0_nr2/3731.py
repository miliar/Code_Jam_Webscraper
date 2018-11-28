#include<stdio.h>

int N , S , p  ,a[ 105 ] , ans ;


int judge( int num )
{
    if( num >= 0  && num <= 10 )
    return 1;
    return 0;
}


void dfs( int cur , int s , int cnt )
{
    if( cur == N )
    {
        if( s == S )
        {
            if ( cnt > ans )
                ans = cnt;
        }
        return ;
    }
    if( s > S )
        return ;

    if( a[cur] + 3 >= 0 && ( a[cur] + 3 ) % 3 == 0 )
    {
        int b = ( a[cur] + 3 ) / 3;
        if( judge( b ) && judge( b-1 ) && judge( b-2 ) )
        {
            if( b >= p  )
            dfs( cur + 1 , s + 1 , cnt + 1 );
            else
            dfs( cur + 1 , s + 1 , cnt );
        }
    }
    if( a[cur] + 2 >= 0 && ( a[cur] + 2 ) % 3 == 0 )
    {
        int b = ( a[cur] + 2 ) / 3;
        if( judge( b ) && judge( b - 2 ) )
        {
            if( b >= p  )
            dfs( cur + 1 , s + 1 , cnt + 1 );
            else
            dfs( cur + 1 , s + 1 , cnt );
        }
    }
    if( a[cur] + 2 >= 0 && ( a[cur] + 2 ) % 3 == 0 )
    {
        int b = ( a[cur] + 2 ) / 3;
        if( judge( b ) && judge( b-1 ) )
        {
            if( b >= p  )
            dfs( cur + 1 , s  , cnt + 1 );
            else
            dfs( cur + 1 , s  , cnt );
        }
    }
    if( a[cur] + 1 >= 0 && ( a[cur] + 1 ) % 3 == 0 )
    {
        int b = ( a[cur] + 1 ) / 3;
        if( judge( b ) && judge( b - 1 ) )
        {
            if( b >= p  )
            dfs( cur + 1 , s  , cnt + 1 );
            else
            dfs( cur + 1 , s  , cnt );
        }
    }
    if( a[cur] >= 0 && ( a[cur] ) % 3 == 0 )
    {
        int b = ( a[cur] ) / 3;
        if( judge( b ) && judge( b - 1 ) && judge( b + 1 ) )
        {
            if( b + 1 >= p  )
            dfs( cur + 1 , s + 1 , cnt + 1 );
            else
            dfs( cur + 1 , s + 1 , cnt );
        }
    }
    if( a[cur] - 1  >= 0 && ( a[cur] - 1 ) % 3 == 0 )
    {
        int b = ( a[cur] - 1  ) / 3;
        if( judge( b ) && judge( b + 1 ) )
        {
            if( b + 1 >= p  )
            dfs( cur + 1 , s  , cnt + 1 );
            else
            dfs( cur + 1 , s  , cnt );
        }
    }
    if( a[cur] - 2 >= 0 && ( a[cur] - 2 ) % 3 == 0 )
    {
        int b = ( a[cur] - 2 ) / 3;
        if( judge( b ) && judge( b + 1 ) )
        {
            if( b + 1 >= p  )
            dfs( cur + 1 , s  , cnt + 1 );
            else
            dfs( cur + 1 , s , cnt );
        }
    }
    if( a[cur] - 2 >= 0 && ( a[cur] - 2 ) % 3 == 0 )
    {
        int b = ( a[cur] - 2 ) / 3;
        if( judge( b ) && judge( b + 2 ) )
        {
            if( b + 2 >= p  )
            dfs( cur + 1 , s + 1 , cnt + 1 );
            else
            dfs( cur + 1 , s + 1, cnt );
        }
    }
    if( a[cur] - 3 >= 0 && ( a[cur] - 3 ) % 3 == 0 )
    {
        int b = ( a[cur] - 3 ) / 3;
        if( judge( b ) && judge( b + 1 ) && judge( b + 2 ) )
        {
            if( b + 2 >= p  )
            dfs( cur + 1 , s + 1 , cnt + 1 );
            else
            dfs( cur + 1 , s + 1, cnt );
        }
    }
    if( a[cur]  >= 0 && ( a[cur] ) % 3 == 0 )
    {
        int b = ( a[cur] ) / 3;
        if( judge( b ) )
        {
            if( b >= p  )
            dfs( cur + 1 , s  , cnt + 1 );
            else
            dfs( cur + 1 , s , cnt );
        }
    }

}
int main()
{
    int cases;
    freopen("B-small-attempt0.in","r" ,stdin);
    freopen("B.txt","w" ,stdout);
    scanf("%d" , &cases );
    for( int t = 1 ;t <= cases ; t++ )
    {
        scanf("%d%d%d" , & N , &S , &p );
        for( int i = 0 ; i < N ; i++ )
            scanf( "%d" , &a[i] );
        printf("Case #%d: ", t );
        ans = 0;
        dfs( 0  , 0 , 0 );
        printf("%d\n" ,ans );
    }
    return 0;
}

