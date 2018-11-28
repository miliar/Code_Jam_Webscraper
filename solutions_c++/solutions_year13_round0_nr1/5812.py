#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;
#define MAXN 100 + 5
#define MAXV 10000 + 5
#define INF 1e9
#define eps 1e-9
int n;
char G[6][6];
int cnt[2];
int isEqual(char a, char b)
{
	if(a == b || a == 'T' || b == 'T')
		return 1;
	return 0;
}
int isRowEqual(int row)
{
	if(isEqual(G[row][1], G[row][2]) && isEqual(G[row][2], G[row][3]) 
		&& isEqual(G[row][3], G[row][4]) && isEqual(G[row][1], G[row][4]))
		return 1;
	return 0;
}
int isColEqual(int col)
{
	if(isEqual(G[1][col], G[2][col]) && isEqual(G[2][col], G[3][col]) 
		&& isEqual(G[3][col], G[4][col]) && isEqual(G[1][col], G[4][col]))
		return 1;
	return 0;
}
int isDiaEqual(int flag)
{
	if(flag == 1)
	{
		if(G[1][1] == '.')
			return 0;
		if(isEqual(G[1][1], G[2][2]) && isEqual(G[2][2], G[3][3]) 
			&& isEqual(G[3][3], G[4][4]) && isEqual(G[1][1], G[4][4]))
			return 1;
	}
	if(flag == 4)
	{
		if(G[4][1] == '.')
			return 0;
		if(isEqual(G[4][1], G[3][2]) && isEqual(G[3][2], G[2][3]) 
			&& isEqual(G[2][3], G[1][4]) && isEqual(G[4][1], G[1][4]))
			return 1;
	}
	return 0;
}
int solve()
{
	for(int i = 1; i <= 4; i++)
	{
		if(G[i][1] == 'X' || (G[i][1] == 'T' && G[i][2] == 'X'))
		{
			if(isRowEqual(i))
			{
				cnt[0] = 4;
				break;
			}
		}
		else if(G[i][1] == 'O' || (G[i][1] == 'T' && G[i][2] == 'O'))
		{
			if(isRowEqual(i))
			{
				cnt[1] = 4;
				break;
			}
		}
	}
	for(int i = 1; i <= 4; i++)
	{
		if(G[1][i] == 'X' || (G[1][i] == 'T' && G[2][i] == 'X'))
		{
			if(isColEqual(i))
			{
				cnt[0] = 4;
				break;
			}
		}
		else if(G[1][i] == 'O' || (G[1][i] == 'T' && G[2][i] == 'O'))
		{
			if(isColEqual(i))
			{
				cnt[1] = 4;
				break;
			}
		}
	}
	if(G[1][1] == 'X' || (G[1][1] == 'T' && G[2][2] == 'X'))
	{
		if(isDiaEqual(1))
		{
			cnt[0] = 4;
		}
	}
	if(G[4][1] == 'X' || (G[4][1] == 'T' && G[3][2] == 'X'))
	{
		if(isDiaEqual(4))
		{
			cnt[0] = 4;
		}
	}
	if(G[1][1] == 'O' || (G[1][1] == 'T' && G[2][2] == 'O'))
	{
		if(isDiaEqual(1))
		{
			cnt[1] = 4;
		}
	}
	if(G[4][1] == 'O' || (G[4][1] == 'T' && G[3][2] == 'O'))
	{
		if(isDiaEqual(4))
		{
			cnt[1] = 4;
		}
	}
	if(cnt[0] == 4)
		return 1;
	if(cnt[1] == 4)
		return 2;
	int isFinish = 1;
	for(int i = 1; i <= 4; i++)
	{
		for(int j = 1; j <= 4; j++)
		{
			if(G[i][j] == '.')
			{
				isFinish = 0;
				break;
			}
		}
		if(!isFinish)
			break;
	}
	if(!isFinish) return -1;
	else return 0;
}
int main()
{
#ifdef LOCAL
	freopen("data.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	getchar();
	for(int ncas = 1; ncas <= T; ncas++)
	{
		cnt[0] = 0, cnt[1] = 0;
		printf("Case #%d: ", ncas);
		for(int i = 1; i <= 4; i++)
		{
			for(int j = 1; j <= 4; j++)
			{
				scanf("%c", &G[i][j]);
			}
			getchar();
		}
		getchar();
		int ans = solve();
		if(ans == 0)
		{
			printf("Draw\n");
		}
		else if(ans == -1)
		{
			printf("Game has not completed\n");
		}
		else if(ans == 1)
		{
			printf("X won\n");
		}
		else if(ans == 2)
		{
			printf("O won\n");
		}
	}
	return 0;
}