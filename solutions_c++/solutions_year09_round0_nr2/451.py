#include<stdio.h>
#include <deque>
#include <algorithm>
using namespace std;
struct Node
{
	int x,y ;
};
bool path[200][200] ;
int Map[200][200] ;
int F[200][200] ;
int FF[40000] ;
char Ans[200][200] ;
int P[50000] ;
char s ;
int n,m ;
int dir[][2] = {{-1,0},{0,-1},{0,1},{1,0}} ;
int Find(int x)
{
	if(FF[x] == x) return x ;
	return (FF[x]=Find(FF[x])) ;
}
void dfs(int x,int y)
{
	int i , Min ;
	int xx,yy ;
	Min = 200000 ;
	int id ;
	for(i = 0 ; i < 4 ; i ++)
	{
		xx = x + dir[i][0] ;
		yy = y + dir[i][1] ;
		if(xx < 0 || xx >= n || yy < 0 || yy >= m) continue ;
		if(Min > Map[xx][yy])
		{
			Min = Map[xx][yy] ;
			id = i ;
		}
	}
	if(Map[x][y] <= Min) return ;
	int X = Find(F[x][y]) ;
	int Y = Find(F[x+dir[id][0]][y+dir[id][1]]) ;
	if(X == Y) return ;
	F[x][y] = F[x+dir[id][0]][y+dir[id][1]] ;

}
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("cc.out","w",stdout) ;
	int T ;
	while(1 == scanf("%d",&T))
	{
		int Case = 1 ;
		int i,j ;
		while(T --)
		{
			scanf("%d %d",&n,&m);
			int f = 0 ;
			for(i = 0 ; i < n*m ; i ++)
				FF[i] = i ;
			for(i = 0 ; i < n ; i ++)
			{
				for(j = 0 ; j < m ; j ++)
				{
					scanf("%d",&Map[i][j]) ;
					F[i][j] = f ++ ;
				}
			}
			for(int k = 0 ; k < 300 ; k ++)
			{
				for(i = 0 ; i < n ; i ++)
				{
					for(j = 0 ; j < m ; j ++)
					{
						dfs(i,j) ;
					}
				}
			}
			
			printf("Case #%d:\n",Case++) ;
			memset(P,-1,sizeof(P)) ;
			int id = 0;
			for(i = 0 ; i < n ; i ++)
			{
				for(j = 0 ; j < m ; j ++)
				{
					if(j != 0) printf(" ") ;
					if(P[F[i][j]] == -1)
					{
						P[F[i][j]] = id ++ ;
					}
					printf("%c",P[F[i][j]]+'a') ;
				}
				printf("\n") ;
			}
		}
	}
	return 0 ;
}