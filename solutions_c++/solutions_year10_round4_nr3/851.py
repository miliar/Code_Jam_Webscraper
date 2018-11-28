#include <stdio.h>
int main()
{
    int C,R,X1[100],Y1[100],X2[100],Y2[100];
    int map[2][100][100];
    scanf("%d",&C);
    for( int i = 0 ; i < C ; i++ )
    {
        for( int j = 0 ; j < 100 ; j++ )
            for( int k = 0 ; k < 100 ; k++ )
                    map[0][j][k] = 0;
        scanf("%d",&R);
        for( int j = 0 ; j < R ; j++ )
        {
            scanf("%d %d %d %d",&X1[j],&Y1[j],&X2[j],&Y2[j]);
            for( int k = X1[j]-1 ; k < X2[j] ; k++ )
                for( int l = Y1[j]-1 ; l < Y2[j] ; l++ )
                    map[0][k][l] = 1;
        }
        int T = 0;
        bool whileNext = true;
        while(whileNext)
        {
            T++;
            whileNext = false;
            for( int j = 0 ; j < 100 ; j++ )
                map[T%2][0][j] = 0;
            for( int j = 0 ; j < 100 ; j++ )
                map[T%2][j][0] = 0;
            for( int j = 1 ; j < 100 ; j++ )
                for( int k = 1 ; k < 100 ; k++ )
                {
                    if( map[(T+1)%2][j-1][k] == 0 && map[(T+1)%2][j][k-1] == 0 )
                        map[T%2][j][k] = 0;
                    else if( map[(T+1)%2][j-1][k] == 1 && map[(T+1)%2][j][k-1] == 1 )
                        map[T%2][j][k] = 1;
                    else
                        map[T%2][j][k] = map[(T+1)%2][j][k];
                }
            for( int j = 0 ; j < 100 ; j++ )
                for( int k = 0 ; k < 100 ; k++ )
                    if( map[T%2][j][k] == 1 )
                    {
                        whileNext = true;
                        j = k = 100; // break;
                    }
        }
        printf("Case #%d: %d\n",i+1,T);
    }
    return 0;
}
