#include <iostream>
#include <algorithm>
#include <map>
using namespace std ; 
#define MAXN 105
int dir[4][2] = { {-1,0} ,{0,-1} ,{0,1} , {1,0} } ;
int mat[MAXN][MAXN] ;
int val[MAXN][MAXN] ;
bool used[MAXN][MAXN] ;
int n , m ; 

struct Point
{
	int x , y ; 
	int v ;
	Point(){}
	Point(int x , int y , int v):x(x),y(y),v(v){}
} list[MAXN*MAXN] , next ;
bool cmp(Point a, Point b)
{
	return a.v > b.v ; 
}

map<int , int> Map ;

int DFS( Point now )
{
	if( used[now.x][now.y] ) return val[now.x][now.y] ;
	used[now.x][now.y] = true ;
	int i ;
	int u = -1 , v = -1;
	int Max = mat[now.x][now.y] ;
	for(i = 0 ;i < 4 ; i++)
	{
		next.x = now.x + dir[i][0] ;
		next.y = now.y + dir[i][1] ;
		if( next.x >= 0 && next.x < n && next.y >= 0 && next.y < m )
		{
			if( Max > mat[next.x][next.y])
			{
				Max = mat[next.x][next.y] ;
				u = next.x ; 
				v = next.y ;
			}
		}
	}
	if( u == -1 && v == -1 ) return val[now.x][now.y] ;
	else return val[u][v] = DFS( Point(u , v , 0) ) ;
}

int main()
{
	freopen("B-large.in" ,"r" ,stdin ) ;
	freopen("B-large.out" , "w" ,stdout) ;
	int T , Case = 0 ; 
	int i , j , t ;
	scanf("%d" , &T) ;
	while(T--)
	{
		Case++ ;
		scanf("%d %d" ,&n ,&m) ;
		for(i = 0 ; i < n ; i++)
		{
			for(j = 0 ; j < m ; j++)
			{
				scanf("%d" , &mat[i][j]) ;
				val[i][j] = i*m+j ;
				used[i][j] = false ;
				list[val[i][j]].x = i ; 
				list[val[i][j]].y = j ;
				list[val[i][j]].v = mat[i][j] ;
			}
		}
		sort(list , list+n*m , cmp) ;
		for(i = 0 ; i < n*m ; i++)
			val[list[i].x][list[i].y] = DFS( list[i] ) ;

		Map.clear() ;
		int t = 0 ;
		for(i = 0 ; i < n ; i++)
		{
			for(j = 0 ; j < m ; j++)
			{
				if( Map.find( val[i][j] ) == Map.end() )
				{
					mat[i][j] = t ;
					Map[val[i][j]] = t ;
					t++ ;
				}
				else mat[i][j] = Map[ val[i][j] ];
			}
		}
		printf("Case #%d:\n" , Case) ;
		for(i = 0 ; i < n ; i++)
		{
			for(j = 0 ; j < m-1 ; j++)
				printf("%c " ,mat[i][j] + 'a' ) ;
			printf("%c\n" , mat[i][j] + 'a') ;
		}
		
	}
	return 0 ;
}

/*
100
2 3
7 6 7
7 6 7

*/