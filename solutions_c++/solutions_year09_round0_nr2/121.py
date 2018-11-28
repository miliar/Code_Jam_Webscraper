#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;

#define FOR( i , a , b ) for( int (i)=(a);(i)<=(b);i++)
int N , M , Fa[10005] , Mark[10005];
int A[105][105];

void Init()
{
     scanf("%d%d" , &N , &M);
     FOR( i , 0 , N+1 )
     FOR( j , 0 , M+1 ) A[i][j] = 100000;
     FOR( i , 1 , N )
     FOR( j , 1 , M ) scanf("%d" , &A[i][j]);
}

const int Dx[4] = { -1 , 0 , 0 , 1 };
const int Dy[4] = { 0 , -1 , 1 , 0 };

int Find( int x , int y )
{
    int Mi=100000 , p = -1;
    FOR( i , 0 , 3 )
    if( A[x+Dx[i]][y+Dy[i]] < A[x][y] )
    if( A[x+Dx[i]][y+Dy[i]] < Mi )
    {
        Mi = A[x+Dx[i]][y+Dy[i]];
        p = i;
    }
    
    if( p != -1 ) 
	return (x+Dx[p]-1)*M + (y+Dy[p]);
    else return 0;
}       

int Fpath( int x )
{
    int y = x , tmp;
    while( Fa[y] != 0 ) y = Fa[y];
    while( Fa[x] != 0 )
    {
	 	   tmp = Fa[x];
	 	   Fa[x] = y;
	 	   x = tmp;
    }
    return y;
}
           
    

void Work()
{
     memset( Fa , 0 , sizeof(Fa));
     FOR( x , 1 , N )
     FOR( y , 1 , M )
     {
          int Id1 = (x-1)*M + y;
          int Id2 = Find( x , y );
          if( Id2 != 0 )
          if( Fpath(Id1) != Fpath(Id2) ) Fa[Fpath(Id1)] = Fpath(Id2);
     }
     
     memset(Mark , 0 , sizeof(Mark));
     int Res = 0;
     
     FOR( x , 1 , N )
     {
          FOR( y , 1 , M )
          {
               if( y > 1 ) printf(" ");
               if( Mark[Fpath((x-1)*M+y)] == 0 )
               {
			   	   Res++;
			   	   Mark[Fpath((x-1)*M+y)] = Res;
		       }
		       printf("%c" , Mark[Fpath((x-1)*M+y)]+'a'-1 );
          }
          printf("\n");
     }
}
     

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B.out","w",stdout);
    int Test;
    scanf("%d" , &Test);
    FOR(t , 1 , Test)
    {
          Init();
          printf("Case #%d:\n" , t);
          Work();
    }         
    return 0;
}
