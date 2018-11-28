#include <cstdio>

using namespace std;

char board[4][5];

void solve(int t)
{
	printf("Case #%d: ", t);
	int all = 0;
	for(int i = 0; i < 4; ++i)
		for(int j = 0; j < 4; ++j)
			all += board[i][j] == '.';
	for(int i = 0; i < 4; ++i)
	{
		int cnt[300] = {};
		for(int j = 0; j < 4; ++j)
			cnt[board[i][j]]++;
		if(cnt['O'] == 4 || cnt['O'] == 3 && cnt['T'] == 1)
		{
			printf("O won\n");
			return;
		}
		if(cnt['X'] == 4 || cnt['X'] == 3 && cnt['T'] == 1)
		{
			printf("X won\n");
			return;
		}
	}
	for(int i = 0; i < 4; ++i)
	{
		int cnt[300] = {};
		for(int j = 0; j < 4; ++j)
			cnt[board[j][i]]++;
		if(cnt['O'] == 4 || cnt['O'] == 3 && cnt['T'] == 1)
		{
			printf("O won\n");
			return;
		}
		if(cnt['X'] == 4 || cnt['X'] == 3 && cnt['T'] == 1)
		{
			printf("X won\n");
			return;
		}
	}
	for(int i = 0; i < 2; ++i)
	{
		int cnt[300] = {};
		if(i == 0)
			for(int j = 0; j < 4; ++j)
				cnt[board[j][j]]++;
		else
			for(int j = 0; j < 4; ++j)
				cnt[board[j][3-j]]++;
		if(cnt['O'] == 4 || cnt['O'] == 3 && cnt['T'] == 1)
		{
			printf("O won\n");
			return;
		}
		if(cnt['X'] == 4 || cnt['X'] == 3 && cnt['T'] == 1)
		{
			printf("X won\n");
			return;
		}
	}
	if(all == 0)
		printf("Draw\n");
	else
		printf("Game has not completed\n");
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int k = 1; k <= t; ++k)
	{
		for(int i = 0; i < 4; ++i)
			scanf("%s", board[i]);
		solve(k);
	}
	return 0;
}