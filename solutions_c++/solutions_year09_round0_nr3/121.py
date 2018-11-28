#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;

#define FOR( i , a , b ) for( int (i)=(a);(i)<=(b);i++)
int N , M = 19;
const int MD = 10000;
char A[505];
const char B[25] = " welcome to code jam";
int F[505][25];

void Init()
{
    char c;
    N = 0;
    while( scanf("%c" , &c) == 1 )
    {
	 	   if( c == '\n' ) break;
	 	   A[++N] = c;
    }   
}

void Work()
{
     memset(F , 0 , sizeof(F));
     FOR( i , 0 , N ) F[i][0] = 1;
     FOR( j , 1 , M ) F[0][j] = 0;
     
     FOR( j , 1 , M )
     FOR( i , 1 , N )
     	  F[i][j] = (F[i-1][j] + F[i-1][j-1]*(A[i]==B[j]))% MD;
     	  
     printf("%0.4d\n" , F[N][M]);
}
     

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C.out","w",stdout);
    int Test;
    scanf("%d\n" , &Test);
    FOR(t , 1 , Test)
    {
          Init();
          printf("Case #%d: " , t);
          Work();
    }         
    return 0;
}
