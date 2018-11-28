#include <iostream>
#include <deque>
using namespace std ;

const int maxn = 105 ;
int a[maxn][maxn] ;
char b[maxn][maxn] ;
bool visit[maxn*maxn] ;
int belong[maxn*maxn] ;
int n , m ;
int flag[4][2] = { -1 , 0 , 0 , -1 , 0 ,1 , 1 , 0} ;

int find_set( int x )
{
	if( x == belong[x] )
		return x ;
	else
		return belong[x] = find_set( belong[x] ) ;
}
void solve()
{
     int i , j , x , y , k , p , v ;
     char now = 'a' ;
	 for( i = 0 ; i < n*m ; i ++ )
		 belong[i] = i ;
	 memset( visit , 0 , sizeof(visit) ) ;
     for( i = 0 ; i < n ; i ++ )
          for( j = 0 ; j < m ; j ++ )
          {
			   v = a[i][j] ;
               for( k = 0 ; k < 4 ; k ++ )
			   {
				   x = i + flag[k][0] ;
				   y = j + flag[k][1] ;
				   if( x >= 0 && x < n && y >= 0 && y < m && v > a[x][y] )
				   {
					   v = a[x][y] ;
					   p = k ;
				   }
			   }
			   if( v != a[i][j] )
			   {
				    x = i + flag[p][0] ;
					y = j + flag[p][1] ;
					x = find_set( x*m + y ) ;
					y = find_set( i*m + j ) ;
					belong[x] = y ;
			   }
          }
	for( i = 0 ; i < n ; i ++ )
	{
		for( j = 0 ; j < m ; j ++ )
		{
			x = find_set( i*m + j ) ;
			if( !visit[x] )
			{
				b[x/m][x%m] = now ;
				now ++ ;
				visit[x] = true ;
			}
			b[i][j] = b[x/m][x%m] ;
		}
	}
}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int test , t = 1 ;
    scanf("%d" , &test ) ;
    while( test -- )
    {
           scanf("%d%d" , &n , &m )  ;
           int i , j ;
           for( i = 0 ; i < n ; i ++ )
                for( j = 0 ; j < m ; j ++ )
                     scanf("%d", &a[i][j] ) ;
           solve();
           printf("Case #%d:\n" , t ++ ) ;
           for( i = 0 ;i < n ; i++ )
           {
                for( j = 0 ;j < m ;j++ )
                {
                     if( j ) printf(" ") ;
                     printf("%c" , b[i][j] ) ;
                }
                printf("\n") ;
           }
    }
    return 0 ;
}
