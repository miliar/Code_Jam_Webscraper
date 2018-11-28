#include<cstring>
#include<algorithm>
#include<iostream> 
#include<cstdio>
#include<queue>
#include<fstream>
using namespace std;

int main()
{
    freopen("B-small.in", "r", stdin);
    freopen("b.out", "w", stdout);

    int t, c = 0, i, j, k, m, n, row, col, d, R, C, tmpx, tmpy;
    char in[1000];
    int board[500][500];
    long long int x, y;

    scanf("%d",&t);
    while( t-- )
	{
        scanf("%d %d %d", &row, &col, &d);
        R = row*2;
        C = col*2;

        for( i=0; i<row; ++i ){
            scanf("%s", in);
            for( j=0; j<col; ++j )
                board[i][j] = d+(in[j]-'0');
        }

        /*for( i=0; i<row; ++i ){
            for( j=0; j<col; ++j ){
                printf("%d", board[i][j]);
            }
            putchar('\n');
        }*/

        for( i=(row>col)?(col):(row); i>2; --i ){

            for( j=i; (j+i)<=R; j+=2 ){
                for( k=i; (k+i)<=C; k+=2 ){

                    x = 0;
                    y = 0;
                    for( m=j-i+1,tmpx=j+i-1; m<=tmpx; m+=2 ){
                        for( n=k-i+1,tmpy=k+i-1; n<=tmpy; n+=2 ){
                            x += ((m-j)*board[m/2][n/2]);
                            y += ((n-k)*board[m/2][n/2]);
                        }
                    }
                    x -= ((1-i)*board[(j-i+1)/2][(k-i+1)/2]);
                    x -= ((i-1)*board[(j+i-1)/2][(k-i+1)/2]);
                    x -= ((1-i)*board[(j-i+1)/2][(k+i-1)/2]);
                    x -= ((i-1)*board[(j+i-1)/2][(k+i-1)/2]);
                    y -= ((1-i)*board[(j-i+1)/2][(k-i+1)/2]);
                    y -= ((i-1)*board[(j-i+1)/2][(k+i-1)/2]);
                    y -= ((1-i)*board[(j+i-1)/2][(k-i+1)/2]);
                    y -= ((i-1)*board[(j+i-1)/2][(k+i-1)/2]);

                    if( x==0 && y==0 )
						break;

                }
                if( (k+i)<=C )
					break;
            }
            if( (j+i)<=R )
				break;

        }

        if( i < 3 )
			printf("Case #%d: IMPOSSIBLE\n", ++c);
        else
			printf("Case #%d: %d\n", ++c, i);
    }

    return 0;
}

