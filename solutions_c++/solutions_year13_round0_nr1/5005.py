#include <cstdio>
#include <algorithm>

using namespace std;

char board[4][5];

int conv(int n)
{
	int y = n/4;
	int x = n%4;
	char c = board[y][x];
	if (c=='O')
		return 0;
	else if (c=='X')
		return 1;
	else if (c=='T')
		return 2;
	else
		return 3;
}

// 0: O, 1: X, 2: none
int getres(int arr[])
{
	int cnt[4] = { 0 };
	for (int i=0; i<4; ++i)
		++cnt[conv(arr[i])];

	for (int i=0; i<2; ++i)
	{
		if (cnt[i] == 4 || (cnt[i]==3 && cnt[2]==1))
			return i;
	}

	return 2;
}

int cnt[10][4];

int main()
{
	for (int i=0; i<4; ++i)
	{
		for (int j=0; j<4; ++j)
		{
			cnt[i*2][j] = i*4 + j;
			cnt[i*2+1][j] = i + j*4;
		}

		cnt[8][i] = i*5;
		cnt[9][i] = i*3 + 3;
	}
	
	int t;
	scanf("%d", &t);
	for (int c=1; c<=t; ++c)
	{
		for (int i=0; i<4; ++i)
			scanf("%s", board[i]);

		printf("Case #%d: ", c);

		int ans = 2;
		for (int i=0; i<10; ++i)
		{
			ans = getres(cnt[i]);
			if (ans != 2)
				break;
		}

		if (ans == 0)
			printf("O won");
		else if (ans == 1)
			printf("X won");
		else
		{
			int i;
			for (i=0; i<16; ++i)
				if (conv(i) == 3)
					break;

			if (i==16)
				printf("Draw");
			else
				printf("Game has not completed");
		}

		printf("\n");
	}
	
	return 0;
}