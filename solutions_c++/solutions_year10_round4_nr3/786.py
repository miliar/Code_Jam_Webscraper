#include <iostream>
#include <cstring>
#include <vector>
#include <cstdio>
#include <memory>
#include <string>
using namespace std;
#define N 110

int map[N][N];

int check(int *a,int n)
{
	int i=0,j=n-1;
	while(i!=j)
	{
		if ( a[i]!=a[j] )
			return 0;
		i++,j--;
	}
	return 1;
}

int check(int x,int y)
{
	if ( x>=0 && x< N && y>=0 && y<N )
		return 1;
	return 0;
}

int a=0;
void solve( int x,int y )
{
	printf("%d\n",a++);
	if ( x==0 || y==0 )
		return;
	if ( map[x-1][y]==1 && map[x][y-1]==1 )
		map[x][y] = 1;
	else
		if ( map[x-1][y]==0 && map[x][y-1]==0 )
			map[x][y] = 0;
	solve(x-1,y);
	solve(x,y-1);
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("C-small.out","w",stdout);
	int t;
	scanf("%d",&t);
	for ( int c = 1 ; c <= t; c++ )
	{
		memset(map,0,sizeof(map));
		int r;
		scanf("%d",&r);
		int x1,x2,y1,y2;
		while(r--)
		{
			scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
			for ( int x = x1 ; x <= x2 ; x++ )
				for ( int y = y1 ; y <= y2 ; y++ )
				{
					map[x][y] = 1;
				}
		}
		int cnt = 0;
		while(1)
		{
			
			for ( int x = N-1 ; x > 0 ; x-- )
			{
				for ( int y = N-1 ; y > 0 ; y-- )
				{
					if ( map[x-1][y]==1 && map[x][y-1]==1 )
						map[x][y] = 1;
					else
						if ( map[x-1][y]==0 && map[x][y-1]==0 )
							map[x][y] = 0;
				}
			}
			
			cnt++;
			int flag = 1;
			for ( int i = 1 ; i < N ; i++ )
			{
				for ( int j = 1 ; j < N ; j++ )
					if ( map[i][j]==1 )
						flag = 0;
			}
			if ( flag )
				break;
		}
		printf("Case #%d: %d\n",c,cnt);
	}

}