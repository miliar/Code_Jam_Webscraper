#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int graf[100][100];
char dp[100][100];
char start;
int H,W;

char dfs(int i, int j)
{
	if(dp[i][j] != 'Z') return dp[i][j];
	char ret;
	int curr = graf[i][j];
	int nexti = i,nextj = j;
	if(i > 0 && curr > graf[i-1][j])
	{
		nextj = j;
		nexti = i-1;
		curr = graf[i-1][j];
	}
	if(j > 0 && curr > graf[i][j-1])
	{
		nexti = i;
		nextj = j-1;
		curr = graf[i][j-1];
	}
	if(j < W-1 && curr > graf[i][j+1])
	{
		nexti = i;
		nextj = j+1;
		curr = graf[i][j+1];
	}
	if(i < H-1 && curr > graf[i+1][j])
	{
		nextj = j;
		nexti = i+1;
		curr = graf[i+1][j];
	}
	if(nexti != i || nextj != j)
	{
		dp[i][j] = dfs(nexti,nextj);
	}
	else dp[i][j] = start++;

	return dp[i][j];
}

int main()
{
	int tcase;
	cin >> tcase;
	for(int t = 1; t <= tcase; t++)
	{
		cout << "Case #" << t << ":" << endl;
		cin >> H >> W;
		memset(graf,0,sizeof(graf));
		fill((char*)dp,(char*)dp+100*100,'Z');
		start = 'a';
		for(int i = 0;i < H; i++)
		{
			for(int j = 0; j < W; j++)
			{
				cin >> graf[i][j];
			}
		}
		for(int i = 0;i < H; i++)
		{
			for(int j = 0; j < W; j++)
			{
				if(dp[i][j] == 'Z')
				{
					dfs(i,j);
				}
				cout << dp[i][j];
				if(j != W-1) cout << " ";
			}
			cout << endl;
		}
	}
	return 0;
}
