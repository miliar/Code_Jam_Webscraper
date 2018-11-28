#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;

char in[1000];
int board[500][500];



int main()
{
	int t;
    freopen("B.out", "w", stdout);

    scanf("%d",&t);
    for ( int k = 1; k <= t; ++k )
	{
		int row, col, d;
        scanf("%d %d %d", &row, &col, &d);
        int R = row*2, C = col*2;

        for( int i = 0; i < row; ++i )
		{
            scanf("%s", in);
            for( int j = 0; j < col; ++j )
                board[ i ][ j ] = d + ( in[ j ] - '0' );
        }

		int i, j, l, m, n, tempx, tempy;
        
        for( i=(row>col)?(col):(row); i>2; --i ){

            for( j=i; (j+i)<=R; j+=2 ){
                for( l=i; (l+i)<=C; l+=2 ){

                    long long int x = 0, y = 0;
                    for( m=j-i+1,tempx=j+i-1; m<=tempx; m+=2 ){
                        for( n=l-i+1,tempy=l+i-1; n<=tempy; n+=2 ){
                            x += ((m-j)*board[m/2][n/2]);
                            y += ((n-l)*board[m/2][n/2]);
                        }
                    }
                    x -= ((1-i)*board[(j-i+1)/2][(l-i+1)/2]);
                    x -= ((i-1)*board[(j+i-1)/2][(l-i+1)/2]);
                    x -= ((1-i)*board[(j-i+1)/2][(l+i-1)/2]);
                    x -= ((i-1)*board[(j+i-1)/2][(l+i-1)/2]);
                    y -= ((1-i)*board[(j-i+1)/2][(l-i+1)/2]);
                    y -= ((i-1)*board[(j-i+1)/2][(l+i-1)/2]);
                    y -= ((1-i)*board[(j+i-1)/2][(l-i+1)/2]);
                    y -= ((i-1)*board[(j+i-1)/2][(l+i-1)/2]);

                    if( x==0 && y==0 )  break;

                }
                if( (l+i)<=C )  break;
            }
            if( (j+i)<=R )  break;

        }

        if( i < 3 )   
			printf("Case #%d: IMPOSSIBLE\n", k);
        else        
			printf("Case #%d: %d\n", k, i);
    }

    return 0;
}


