#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <cstring>
#include <map>
#include <algorithm>
#include <memory.h>

using namespace std;
#define MAXN 1010
typedef long long int Lint;

int cas, c=0, i, j, k, m, n, row, col, d, R, C, tmpx, tmpy;
char in[MAXN];
int board[MAXN][MAXN];
long long int x, y;

int main()
{
	int cases;
	int casenum = 1;
	freopen("test", "r", stdin);
	//freopen("output", "w", stdout);
	scanf("%d", &cases);
	while(cases--)
	{
        scanf("%d %d %d", &row, &col, &d);
        R = row*2;
        C = col*2;

        for( i=0; i<row; ++i ){
            scanf("%s", in);
            for( j=0; j<col; ++j )
                board[i][j] = d+(in[j]-'0');
        }
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

                    if( x==0 && y==0 )  break;
                }
                if( (k+i)<=C )  break;
            }
            if( (j+i)<=R )  break;

        }

        if( i<3 )
        	printf("Case #%d: IMPOSSIBLE\n", casenum++);
        else
        	printf("Case #%d: %d\n", casenum++, i);
    }
	return 0;
}

