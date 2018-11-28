#include <cstdio>
#include <cctype>
#include <map>
#include <string>
using namespace std;

int tests, n, q, SUMA;
int dx[8] = {-1, -1, 1, 1, 2, 0, -2, 0};
int dy[8] = {-1, 1, -1, 1, 0, -2, 0, 2};
int dx2[4] = {-1, 0, 1, 0};
int dy2[4] = {0, -1, 0, 1};

char t[30][30];
map<int, string> vis[50][20][20];

string sprawdz(int dl, int suma, int x, int y)
{
	if (dl == 0)
	{
		if (suma == 0)
			return string("x");
		return string("");
	}
	
	if (vis[dl][x][y].count(suma))
		return vis[dl][x][y][suma];
	
	string ans;
	
	for (int k = 0; k < 4; k++)
		if (x + dx[k] >= 0 && x + dx[k] < n && y + dy[k] >= 0 && y + dy[k] < n)
		{
			string s1 = sprawdz(dl - 1, suma + (t[x][y + dy[k]] == '+' ? -1 : 1) * (t[x + dx[k]][y + dy[k]] - '0'), x + dx[k], y + dy[k]);
			string s2 = sprawdz(dl - 1, suma + (t[x + dx[k]][y] == '+' ? -1 : 1) * (t[x + dx[k]][y + dy[k]] - '0'), x + dx[k], y + dy[k]);

			if (!s1.empty())
			{
				s1 = t[x + dx[k]][y + dy[k]] + s1;
				if (t[x][y + dy[k]] == '+') s1 = '+' + s1; else s1 = '-' + s1;

				if (ans.empty() || s1 < ans)
					ans = s1;
			}
			
			if (!s2.empty())
			{
				s2 = t[x + dx[k]][y + dy[k]] + s2;
				if (t[x + dx[k]][y] == '+') s2 = '+' + s2; else s2 = '-' + s2;
				
				if (ans.empty() || s2 < ans)
					ans = s2;
			}
		}
	
	for (int k = 4; k < 8; k++)
		if (x + dx[k] >= 0 && x + dx[k] < n && y + dy[k] >= 0 && y + dy[k] < n)
		{
			string s1 = sprawdz(dl - 1, suma + (t[x + dx[k] / 2][y + dy[k] / 2] == '+' ? -1 : 1) * (t[x + dx[k]][y + dy[k]] - '0'), x + dx[k], y + dy[k]);
			string s2 = sprawdz(dl - 1, suma + (t[x + dx[k] / 2][y + dy[k] / 2] == '+' ? -1 : 1) * (t[x + dx[k]][y + dy[k]] - '0'), x + dx[k], y + dy[k]);
			
			if (!s1.empty())
			{
				s1 = t[x + dx[k]][y + dy[k]] + s1;
				if (t[x + dx[k] / 2][y + dy[k] / 2] == '+') s1 = '+' + s1; else s1 = '-' + s1;
				
				if (ans.empty() || s1 < ans)
					ans = s1;
			}
			
			if (!s2.empty())
			{
				s2 = t[x + dx[k]][y + dy[k]] + s2;
				if (t[x + dx[k] / 2][y + dy[k] / 2] == '+') s2 = '+' + s2; else s2 = '-' + s2;
				
				if (ans.empty() || s2 < ans)
					ans = s2;
			}
		}
	
	for (int k = 0; k < 4; k++)
		if (x + dx2[k] >= 0 && x + dx2[k] < n && y + dy2[k] >= 0 && y + dy2[k] < n)
		{
			string s = sprawdz(dl - 1, suma + (t[x + dx2[k]][y + dy2[k]] == '+' ? -1 : 1) * (t[x][y] - '0'), x, y);
			
			if (!s.empty())
			{
				s = t[x][y] + s;
				if (t[x + dx2[k]][y + dy2[k]] == '+') s = '+' + s; else s = '-' + s;
				
				if (ans.empty() || s < ans)
					ans = s;
			}
		}
	
	vis[dl][x][y][suma] = ans;
	
	return ans;
}

int main()
{
	scanf("%d", &tests);
	for (int tc = 0; tc < tests; tc++)
	{
		scanf("%d %d", &n, &q);
		for (int i = 0; i < n; i++)
			scanf("%s", &t[i]);
		
		for (int i = 0; i < 50; i++)
			for (int j = 0; j < 20; j++)
				for (int k = 0; k < 20; k++)
					vis[i][j][k].clear();
		
		printf("Case #%d:\n", tc + 1);
		
		for (int qu = 0; qu < q; qu++)
		{
			string ans;
			scanf("%d", &SUMA);
			
			for (int d = 1; ; d++)
			{
				for (int i = 0; i < n; i++)
				{
					for (int j = 0; j < n; j++)
						if (isdigit(t[i][j]))
						{
							string s = sprawdz(d - 1, SUMA - (t[i][j] - '0'), i, j);
							
							if (!s.empty())
							{
								s = t[i][j] + s;
								
								if (ans.empty() || s < ans)
									ans = s;
							}
						}
				}
				if (!ans.empty())
					break;
			}
			
			for (int i = 0; i < (int)ans.size() - 1; i++)
				printf("%c", ans[i]);
			printf("\n");
		}
	}
	return 0;
}