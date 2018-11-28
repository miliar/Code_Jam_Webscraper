#include <stdio.h>

int main()
{
	int cases, numcase = 1, bsize, K, i, j, ir, jr, cnt, it, jt;
	char board[50][51], rotated[50][51];
	bool red, blue;

	//freopen("A-small.in", "r", stdin);
	//freopen("A-small.out", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	for(scanf("%i", &cases); numcase <= cases; numcase++)
	{
		scanf("%i %i\n", &bsize, &K);
		for(i = 0; i < bsize; i++)
			scanf("%s", board[i]);

		// rotate
		for(i = bsize - 1; i >= 0; i--)
		{
			jr = bsize - 1 - i;
			for(j = 0; j < bsize; j++)
				rotated[j][jr] = board[i][j];
		}

		// gravity
		for(i = bsize - 2; i >= 0; i--)
		{
			for(j = 0; j < bsize; j++)
			{
				if(rotated[i][j] != '.')
				{
					ir = i + 1;
					while(ir < bsize && rotated[ir][j] == '.')
						ir++;
					
					ir--;

					if(ir != i)
					{
						rotated[ir][j] = rotated[i][j];
						rotated[i][j] = '.';
					}
				}
			}
		}

		red = false;
		blue = false;
		// check
		for(i = 0; i < bsize; i++)
		{
			for(j = 0; j < bsize; j++)
			{
				if(rotated[i][j] != '.')
				{
					// vertical
					cnt = 1;
					it = i - 1;
					jt = j;
					while(it >= 0 && rotated[it][jt] == rotated[i][j])
					{
						it--;
						cnt++;
					}
					it = i + 1;
					while(it < bsize && rotated[it][jt] == rotated[i][j])
					{
						it++;
						cnt++;
					}
					if(cnt >= K) { if(rotated[i][j] == 'B') blue = true; else red = true; }

					// horizontal
					cnt = 1;
					it = i;
					jt = j - 1;
					while(jt >= 0 && rotated[it][jt] == rotated[i][j])
					{
						jt--;
						cnt++;
					}
					jt = j + 1;
					while(jt < bsize && rotated[it][jt] == rotated[i][j])
					{
						jt++;
						cnt++;
					}
					if(cnt >= K) { if(rotated[i][j] == 'B') blue = true; else red = true; }

					// diagonal 1									
					cnt = 1;
					it = i - 1;
					jt = j - 1;
					while(it >= 0 && jt >= 0 && rotated[it][jt] == rotated[i][j])
					{
						it--;
						jt--;
						cnt++;
					}
					it = i + 1;
					jt = j + 1;
					while(it < bsize && jt < bsize && rotated[it][jt] == rotated[i][j])
					{
						it++;
						jt++;
						cnt++;
					}
					if(cnt >= K) { if(rotated[i][j] == 'B') blue = true; else red = true; }

					// diagonal 2
					cnt = 1;
					it = i - 1;
					jt = j + 1;
					while(it >= 0 && jt < bsize && rotated[it][jt] == rotated[i][j])
					{
						it--;
						jt++;
						cnt++;
					}
					it = i + 1;
					jt = j - 1;
					while(it < bsize && jt >= 0 && rotated[it][jt] == rotated[i][j])
					{
						it++;
						jt--;
						cnt++;
					}
					if(cnt >= K) { if(rotated[i][j] == 'B') blue = true; else red = true; }
				}
			}
		}

		if(red && blue) printf("Case #%i: Both\n", numcase);
		else if(red) printf("Case #%i: Red\n", numcase);
		else if(blue) printf("Case #%i: Blue\n", numcase);
		else printf("Case #%i: Neither\n", numcase);
	}

	return 0;
}