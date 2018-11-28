#include <iostream>
#include <utility>
#include <vector>

using namespace std;


char board[40][40];
bool use[40][40];
int dp[40][40];
char s[1000];
vector<pair<int, int> > res;


int getNum(char c)
{
	if(c >= 'A' && c <= 'Z')
	{
		return c - 'A' + 10;
	}
	return c - '0';
}


void del(int I, int J, int L)
{
	for(int i = 0; i < L; i++)
	{
		for(int j = 0; j < L; j++)
		{
			use[I + i][J - j] = true;
		}
	}

}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int _i = 0; _i < t; _i++)
	{
		int n, m, len;
		res.clear();
		scanf("%d%d", &n, &m);
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < m; j++)
			{
				use[i][j] = false;
				dp[i][j] = 0;
				board[i][j] = '0';
			}
		}
		len = m / 4;
		for(int j = 0; j < n; j++)
		{
			scanf("%s", s);
			for(int k = 0; k < len; k++)
			{
				int p = getNum(s[k]);
				for(int _ = 1; _ <= 4; _++)
				{
					board[j][k * 4 + 4 - _] = '0' + (p & 1);
					p /= 2;
				}
			}
		}
		printf("Case #%d: ", _i + 1); 
		while(true)
		{
			for(int i = 0; i < n; i++)
			{
				if(use[i][0])
				{
					dp[i][0] = 0;
				}
				else
				{
					dp[i][0] = 1;
				}
				for(int j = 1; j < m; j++)
				{
					if(use[i][j])
					{
						dp[i][j] = 0;
						continue;
					}
					dp[i][j] = 1;
					if(board[i][j] != board[i][j - 1])
					{
						dp[i][j] = dp[i][j - 1] + 1;
					}
				}
			}
			int bestI = -1;
			int bestJ = -1;
			int bestLen = -1;
			for(int i = 0; i < n; i++)
			{
				for(int j = 0; j < m; j++)
				{
					int mi = 1000;
					for(int k = 0; k + i < n; k++)
					{
						mi = min(mi, dp[i + k][j]);
						if(k > 0 && board[i + k][j] == board[i + k - 1][j])
						{
							break;
						}
						if(mi >= k + 1)
						{
							if(bestLen < k + 1)
							{
								bestLen = k + 1;
								bestI = i;
								bestJ = j;
							}
						}
					}
				}
			}
			if(bestLen == -1)
			{
				break;
			}
			del(bestI, bestJ, bestLen);
			if( res.size() == 0 || res.back().first != bestLen)
			{
				res.push_back( make_pair(bestLen, 1));
			}
			else
			{
				res.back().second++;
			}
		}
		printf("%d\n", res.size());
		for(int _ = 0; _ < res.size(); _++)
		{
			printf("%d %d\n", res[_].first, res[_].second);
		}
	}
	return 0;
}