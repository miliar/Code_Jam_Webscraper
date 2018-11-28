#include <cstdio>

const int dx[] = {1, 0, 1, 1};
const int dy[] = {0, 1, 1, -1};

int T;
int main()
{
	scanf("%d", &T);
	for(int t = 0; t < T; t ++)
	{
		int N, K;
		scanf("%d %d\n", &N, &K);
		char c[N][N];
		for(int i = 0; i < N; i ++)
		{
			for(int j = 0; j < N; j ++)
				c[i][j] = getc(stdin);
			getc(stdin);
		}
		char newC[N][N];
		for(int i = 0; i < N; i ++)
		{
			for(int j = 0; j < N; j ++)
			{
				newC[i][j] = c[N - 1 - j][i];
//				fprintf(stderr, "%c", newC[i][j]);
			}
//			fprintf(stderr, "\n");
		}
		for(int row = N - 1; row > 0; row --)
			for(int col = 0; col < N; col ++)
				if( newC[row][col] == '.' )
				{
					int r = row - 1;
					while(r > 0 && newC[r][col] == '.')		r --;
					newC[row][col] = newC[r][col];
					newC[r][col] = '.';
				}
		int count[256];
		count['R'] = count['B'] = 0;
		for(int i = 0; i < N; i ++)
			for(int j = 0; j < N; j ++)	if( newC[i][j] != '.' )
				for(int d = 0; d < 4; d ++)
				{
					bool fl = 1;
					int x = i, y = j;
					for(int k = 1; k < K; k ++)
						if( x + dx[d] < 0 || x + dx[d] >= N || y + dy[d] < 0 || y + dy[d] >= N || newC[i][j] != newC[x + dx[d]][y + dy[d]] )
						{
							fl = 0;
							break;
						}
						else
							x += dx[d], y += dy[d];
					if( fl )	
						count[ newC[i][j] ] ++;
				}
		printf("Case #%d: %s\n", t + 1, (count['R'] && count['B']) ? "Both" : (count['R'] ? "Red" : count['B'] ? "Blue" : "Neither"));
	}
}
