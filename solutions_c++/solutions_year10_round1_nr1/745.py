#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

char board[51][51];

bool win(int ci, int cj, int K, char p, int N)
{
	int c=1;
	int down=ci+1;
	while(c<K && down<N && board[down][cj]==p)
		c++, down++;
	if(c==K)
		return true;

	c=1;
	int right=cj+1;
	while(c<K && right<N && board[ci][right]==p)
		c++, right++;
	if(c==K)
		return true;

	c=1;
	down=ci+1, right=cj+1;
	while(c<K && down<N && right<N && board[down][right]==p)
	{
		c++;
		right++;
		down++;
	}
	if(c==K)
		return true;

	c=1;
	down=ci+1;
	int left=cj-1;
	while(c<K && down<N && left>=0 && board[down][left]==p)
	{
		c++;
		left--;
		down++;
	}
	if(c==K)
		return true;

	return false;
}

int main()
{
	freopen("data.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++)
	{
		memset(board, '.', sizeof(board));
		int N, K;
		scanf("%d%d", &N, &K);
		for(int i=0; i<N; i++)
			scanf("%s", board[i]);
		for(int i=0; i<N; i++)
			for(int j=N-1; j>=0; j--)
				if(board[i][j]=='R' || board[i][j]=='B')
				{
					int c=j, k=j+1;
					while(k<N && board[i][k]=='.')
					{
						swap(board[i][c], board[i][k]);
						k++;
						c++;
					}
				}
		bool red=false, blue=false;
		for(int i=0; i<N; i++)
			for(int j=0; j<N; j++)
			{
				if(board[i][j]=='R' && win(i, j, K, 'R', N))
					red=true;
				else if(board[i][j]=='B' && win(i, j, K, 'B', N))
					blue=true;
			}

		printf("Case #%d: ", t);
		if(red && !blue)
			printf("Red\n");
		else if(!red && blue)
			printf("Blue\n");
		else if(red && blue)
			printf("Both\n");
		else
			printf("Neither\n");
	}
	return 0;
}