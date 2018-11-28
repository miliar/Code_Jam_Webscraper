#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

const	int	limitSize	= 40000;

int		n , m;
char		mat	[100][100];
int		idx	[100][100];

vector<int>	list	[limitSize];

void	init()
{
	scanf("%d%d" , &n , &m);
	for (int i = 0; i < n; i ++)
		scanf("%s" , mat[i]);
}

int		N;

void	add(int v , int x , int y)
{
	if (0 <= x && x < n && 0 <= y && y < m)
	{
		if (mat[x][y] == '.')
			list[v].push_back(idx[x][y]);
	}
}

bool		mark	[limitSize];
int		cy	[limitSize];

bool	extendPath(int u)
{
	int	i , v , size = list[u].size();
	for (i = 0; i < size; i ++)
	{
		v = list[u][i];
		if (! mark[v])
		{
			mark[v] = 1;
			if (cy[v] < 0 || extendPath(cy[v]))
				return	cy[v] = u , 1;
		}
	}
	return 0;
}



void	solve()
{
	int	i , j;
	int	ans = 0;

	for (i = 0; i < n; i ++)
		for (j = 0; j < m; j ++)
		{
			idx[i][j] = i * m + j;
			list[idx[i][j]].clear();

			if (mat[i][j] == '.') ans ++;
		}
	for (i = 0; i < n; i ++)
		for (j = 0; j < m; j ++)
			if (j % 2)
	{
		if (mat[i][j] == '.')
		{
			for (int x = i - 1; x <= i + 1; x ++)
			{
				add( idx[i][j] , x , j - 1 );
				add( idx[i][j] , x , j + 1 );
			}
		}
	}

	
	memset(cy , 0xff , sizeof(cy));
	for (i = 0; i < n * m; i ++)
	{
		memset(mark , 0 , sizeof(mark));
		if ( extendPath(i)) ans --;
	}

	printf("%d\n" , ans);
}

int	main()
{
	freopen("C-large.in" , "r" , stdin);
	freopen("Clarge.txt" , "w" , stdout);

	int		cntCase , t;
	scanf("%d" , &cntCase);
	for (t = 1; t <= cntCase; t ++)
	{
		init();
		printf("Case #%d: " , t);
		solve();
	}

	return 0;
}
