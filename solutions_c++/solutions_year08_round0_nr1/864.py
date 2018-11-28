#include<cstdio>
#include<vector>

#define MAXCOUNT 10000;
using namespace std;

int dp[1100][1100];

vector<string> v;
int engineCount;
int queries;
void input()
{
	scanf("%d\n", &engineCount);
	char tmp[110];
	for (int i = 0; i < engineCount; i++) 
	{
		gets(tmp);
		v.push_back(tmp);
	}
}

int solve()
{
	char tmp[110];

	scanf("%d\n", &queries);

	if(queries == 0)
		return 0;
	gets(tmp);
	for(int i = 0; i < engineCount; i++)
	{
		if(strcmp(v[i].c_str(), tmp))
		{
			dp[0][i] = 0;
		}
		else
		{
			dp[0][i] = MAXCOUNT;
		}
	}

	for(int i = 1; i < queries; i++)
	{
		gets(tmp);
		string s(tmp);
		for(int j = 0; j < engineCount; j++)
		{
			if(!strcmp(v[j].c_str(), tmp))
			{
				dp[i][j] = MAXCOUNT;
			}
			else
			{
				for(int k = 0; k < engineCount; k++)
				{
					if(k != j)
					{
						dp[i][j] = min(dp[i][j], dp[i-1][k] + 1);
					}
					else
					{
						dp[i][j] = min(dp[i][j], dp[i-1][k]);
					}
				}
			}
		}
	}

	int ans = MAXCOUNT;
	for(int i = 0; i < engineCount; i++)
		ans = min(ans, dp[queries - 1][i]);

	return ans;
}
int main()
{
	int tests;

	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);

	scanf("%d",&tests);

	for(int test = 0; test < tests; test++)
	{
		v.clear();
		for(int i = 0; i < 1100; i++)
			for(int j = 0; j < 1100; j++)
				dp[i][j] = MAXCOUNT;
		input();
		printf("Case #%d: %d\n", test + 1, solve());
	}

	return 0;
}