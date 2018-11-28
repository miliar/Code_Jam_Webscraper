#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>
#include<numeric>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include<list>
#include<iterator>
using namespace std;

#define INF (1<<30)
#define EPS (1e-7)


char res[102][102];
int visit[102][102],g[102][102],n,m,alpha;

int dir[4][2] = { { -1,0 }, {0,-1}, {0,1}, {1,0}};

bool check( int i, int j )
{
	if ( i >= 0 && i < n && j >= 0 && j < m )
		return true;
	return false;
}

void dfs_visit( int i, int j)
{
	if ( res[i][j] != 0)
		return;

	int ii,jj,si,sj,min,k;
	visit[i][j] = 1;
	min = 1 << 20;
	for ( k = 0; k < 4; k ++)
	{
		ii = i + dir[k][0];
		jj = j + dir[k][1];
		if ( check(ii,jj) )
		{
			if ( g[ii][jj] < min )
			{
				min = g[ii][jj];
				si = ii;
				sj = jj;
			}
		}
	}
	if ( min >= g[i][j] ) // sink 
	{
		res[i][j] = alpha + 'a';
		alpha++;
		return;
	}
	else 
	{
		dfs_visit(si,sj);
		res[i][j] = res[si][sj];
	}
}


void dfs()
{
	int i,j;
	memset(visit, 0, sizeof( visit) );
	memset(res,0,sizeof(res));
	alpha = 0;
	//res[0][0] = 'a';
	for( i = 0; i < n; i ++)
	{
		for(j = 0; j < m; j ++)
		{
			if ( visit[i][j] == 0 )
			{
				dfs_visit(i,j);
			}
		}
	}
}
	
int main() 
{
	freopen("B-large.in", "r", stdin);
	freopen("b.txt", "w", stdout);

	int nCase,test,i,j;
	scanf("%d",&nCase);
	for ( test = 1; test <= nCase; test++)
	{
		scanf("%d %d",&n,&m);
		for( i = 0; i < n; i ++)
			for ( j = 0; j < m; j ++)
			{
				scanf("%d",&g[i][j]);
			}
		dfs();
		printf("Case #%d:\n",test);
		for ( i = 0; i < n; i ++)
		{
			printf("%c",res[i][0]);
			for ( j = 1; j < m; j ++)
				printf(" %c",res[i][j]);
			printf("\n");
		}
	}

	return 0;
}
