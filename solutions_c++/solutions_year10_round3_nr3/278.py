#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <algorithm>
using namespace std;
int map[512][512];
char str[512][512];
int res[512];
int hash[512][512];
int tot = 0;
bool isboard(int n, int m, int s_x, int s_y, int length)
{
	int i , j;
	for(j = s_y + 1; j < s_y + length; j ++)
	{
		if(map[s_x][j] == map[s_x][j-1] || hash[s_x][j])
			return false;
	}
	for(i = s_x + 1  ; i < s_x + length; i ++)
	{
		for(j = s_y ; j < s_y + length; j ++)
		{
			if(map[i][j] == map[i-1][j] || hash[i][j])
				return false;
		}
	}
	for(i = s_x; i < s_x + length ; i ++)
	{
		for(j = s_y ; j < s_y + length; j ++)
			hash[i][j] = 1;
	}
	res[length] ++;
	tot -= length * length;
	return true;
}
int main()
{
	int i, j, k, t, n, m, temp, cas = 0, count, flag = 0;
	freopen("C-small.in", "r", stdin);
//	freopen("C-large.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	scanf("%d", &t);
	while(t--)
	{
		count = 0;
		scanf("%d %d", &n, &m);
		tot = n * m;
		for(i = 0; i < n; i ++)
		{
			scanf("%s", &str[i]);
			for(j = 0; j < m/4; j ++)
			{
				if(str[i][j] >= 'A')
					str[i][j] = str[i][j] - 'A' + 10;
				else str[i][j] = str[i][j] - '0';
				int cnt = 3;
				while(cnt >= 0)
				{
					map[i][j * 4 + cnt] = str[i][j] % 2;
					str[i][j]/=2;
					cnt --;
				}
			}
		}
		int r = (n < m)?n:m;
		memset(hash, 0, sizeof(hash));
		memset(res, 0, sizeof(res));
		int cc = 0;
		for(int l = r; l >= 2; l --)
		{
			flag = false;
			for(i = 0 ; i <= n - l ; i ++ )
			{
				for(j = 0; j <= m - l; j ++)
				{
					if(!hash[i][j])
					{
						if(isboard(n, m, i, j, l))
							flag = true;
					}
				}
			}
			if(flag)
				cc ++;
		}
		
		res[1] = tot;
		if(res[1] != 0)
			cc ++;
		printf("Case #%d: %d\n", ++cas, cc );
		for(i = r; i >= 1; i --)
		{
			if(res[i] != 0)
				printf("%d %d\n", i, res[i]);
		}
	}
}