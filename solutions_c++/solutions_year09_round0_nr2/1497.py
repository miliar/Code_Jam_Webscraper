#include <cstdio>
#include <memory>

int H,W;
int map[110][110];
int temp[110][110];
char res[110][110];

int DX[] = {-1,0,0,1};
int DY[] = {0,-1,1,0};


bool deep(int x, int y)
{
	for (int i=0; i<4; i++)
	{
		int nx = x+DX[i];
		int ny = y+DY[i];
		if (nx < 0 || nx >= H
			|| ny < 0 || ny >= W)
			continue;
		if (map[x][y] > map[nx][ny])
			return false;
	}
	return true;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t=0; t<T; t++)
	{
		scanf("%d%d", &H, &W);
		for (int i=0; i<H; i++)
		{
			for (int j=0; j<W; j++)
			{
				scanf("%d", &map[i][j]);
			}
		}
		int val = 1;

		memset(temp,-1,sizeof(temp));
		for (int i=0; i<H; i++)
		{
			for (int j=0; j<W; j++)
			{
				if (deep(i,j))
				{
					temp[i][j] = val;
					val++;
				}
			}
		}

		bool b = true;
		while (b)
		{
			b = false;
			for (int i=0; i<H; i++)
			{
				for (int j=0; j<W; j++)
				{
					if (temp[i][j] != -1)
						continue;
					b = true;
					int x = map[i][j];
					int dir = -1;
					for (int k=0; k<4; k++)
					{
						int nx = i+DX[k];
						int ny = j+DY[k];
						if (nx < 0 || nx >= H
							|| ny < 0 || ny >= W)
							continue;
						if (map[nx][ny] < x)
						{
							x = map[nx][ny];
							dir = k;
						}
					}
					if (dir != -1)
					{
						int nx = i+DX[dir];
						int ny = j+DY[dir];
						temp[i][j] = temp[nx][ny];
					}
				}
			}
		}

		char valc = 'a';
		for (int i=0; i<H; i++)
		{
			for (int j=0; j<W; j++)
			{
				if (temp[i][j] != -1)
				{
					int tt = temp[i][j];
					for (int ii=0; ii<H; ii++)
					{
						for (int jj=0; jj<W; jj++)
						{
							if (tt == temp[ii][jj])
							{
								res[ii][jj] = valc;
								temp[ii][jj] = -1;
							}
						}
					}
					valc++;
				}
			}
		}

		printf("Case #%d:\n", t+1);
		for (int i=0; i<H; i++)
		{
			for (int j=0; j<W; j++)
			{
				if (j != 0)
					printf(" ");
				printf("%c", res[i][j]);
			}
			printf("\n");
		}

	}
	return 0;
}