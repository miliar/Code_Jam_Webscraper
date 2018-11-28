#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <deque>
using namespace std ;
struct Point
{
	int x , y , value ; 
};
Point point[100000] ; 
int mat[103][103] ;
vector<int>pre[103][103] , nex[103][103] ; 
bool use[103][103] ; 
char ans[103][103] ; 
deque<Point>deq ; 
int dir[4][2] = {-1,0,0,-1,0,1,1,0} ; 
bool cmp(Point a , Point b)
{
	if( a.value != b.value ) return a.value > b.value ; 
	if( a.x != b.x ) return a.x < b.x ; 
	return a.y < b.y ;
}
void BFS(int x , int y , char sign )
{
	deq.clear() ; 
	Point st , ne ; 
	int i , j , k ;
	st.x = x ; st.y = y ;
	use[st.x][st.y] = true ;
	ans[st.x][st.y] = sign ; 
	deq.push_back(st) ; 
	while( !deq.empty() )
	{
		st = deq.front() ; 
		deq.pop_front() ;
		for ( i = 0 ; i < pre[st.x][st.y].size() ; i ++ )
		{
			j = pre[st.x][st.y][i] ; 
			ne.x = st.x + dir[j][0] ;
			ne.y = st.y + dir[j][1] ;
			if( !use[ne.x][ne.y] )
			{
				use[ne.x][ne.y] = true ;
				ans[ne.x][ne.y] = sign ; 
				deq.push_back(ne) ; 
			}
 		}
		for( i = 0 ; i < nex[st.x][st.y].size() ; i ++ )
		{
			j = nex[st.x][st.y][i] ; 
			ne.x = st.x + dir[j][0] ;
			ne.y = st.y + dir[j][1] ;
			if( !use[ne.x][ne.y] )
			{
				use[ne.x][ne.y] = true ;
				ans[ne.x][ne.y] = sign ; 
				deq.push_back(ne) ; 
			}
 		}
	}
	return ;
}
int main()
{
	freopen("B-large.in","r",stdin) ;
	freopen("B-large.out","w",stdout) ; 
	int T , Case = 1 ;
	while ( 1 == scanf("%d",&T))
	{
		while ( T -- )
		{
			int i , j , R , C , x , y , res , sign , X , Y , cnt ;
			scanf("%d%d",&R,&C) ;
			cnt = 0 ; 
			for ( i = 0 ; i < R ; i ++)
				for ( j = 0 ; j < C ; j ++)
				{
					scanf("%d",&point[cnt].value) ; 
					mat[i][j] = point[cnt].value ; 
					point[cnt].x = i ; point[cnt].y = j ; 
					cnt ++ ; 
				}
			sort(point , point+cnt , cmp) ;
			for ( i = 0 ; i < R ; i ++)
				for ( j = 0 ; j < C ; j ++)
				{
					pre[i][j].clear() ;
					nex[i][j].clear() ;
				}
			memset(use , false , sizeof(use)) ; 
			for ( i = 0 ; i < cnt ; i ++)
			{
				res = -1 ; sign = -1 ; 
				for ( j = 0 ; j < 4 ; j ++)
				{
					x = point[i].x + dir[j][0] ; 
					y = point[i].y + dir[j][1] ;
					if( x < 0 || y < 0 || x >= R || y >= C ) continue ;
					if( mat[x][y] >= mat[point[i].x][point[i].y]) continue ;
					if( res == -1 || res > mat[x][y])
					{
						sign = j ; 
						res = mat[x][y] ; 
						X = x ; 
						Y = y ; 
					}
				}
				if( sign == -1 ) continue ;
				pre[X][Y].push_back(3-sign) ;
				nex[point[i].x][point[i].y].push_back(sign) ; 
			}
			char st = 'a' ; 
			for ( i = 0 ; i < R; i ++)
				for ( j = 0 ; j < C ; j ++)
				{
					if( use[i][j]) continue ;
					BFS( i , j , st) ; 
					st ++ ; 
				}
			printf("Case #%d:\n",Case++) ; 
			for ( i = 0 ; i < R ; i ++)
			{
				for ( j = 0 ; j < C ; j ++)
				{
					if( j ) printf(" ") ;
					printf("%c",ans[i][j]) ; 
				}
				printf("\n") ; 
			}
		}
	}
	return 0 ;
}