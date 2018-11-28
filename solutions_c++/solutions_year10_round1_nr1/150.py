#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

#define MAX 50

int matr[MAX][MAX];

int main()
{
	freopen("A.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		int N, K;
		scanf("%d%d", &N, &K);
		for (int i = 0; i < N; i++)
		{
			char s[100];
			scanf("%s", s);
			for (int j = 0; j < N; j++)
			{
				if (s[j] == 'R')
					matr[i][j] = 1;
				else if (s[j] == 'B')
					matr[i][j] = 2;
				else
					matr[i][j] = 0;
			}
		}

		for (int i = 0; i < N; i++)
			for (int j = N - 2; j >= 0; j--)
				if (matr[i][j] != 0)
				{
					for (int k = j; (k + 1) < N && matr[i][k + 1] == 0; k++)
						swap(matr[i][k], matr[i][k+1]);
				}
		bool has[3] = {false, false, false};
		int dirs[4][2] = {{1, 0}, {0, 1}, {1, 1}, {1, -1}};
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				if (matr[i][j] != 0)
				{
					int c = matr[i][j];
					for (int d = 0; d < 4; d++)
					{
						int cnt = 0;
						for (int k = 0; k < K; k++)
						{
							int xx = i + dirs[d][0] * k;
							int yy = j + dirs[d][1] * k;
							if (xx >= 0 && xx < N && yy >= 0 && yy < N && matr[xx][yy] == c)
								cnt++;
						}
						if (cnt == K)
							has[c] = true;
					}
				}
		string res;
		if (has[1] && has[2])
		{
			res = "Both";
		}
		else if(has[1])
		{
			res = "Red";
		}
		else if(has[2])
		{
			res = "Blue";
		}
		else
			res = "Neither";

		printf("Case #%d: %s\n", t+1, res.c_str());

	}
	fclose(stdout);
	return 0;
}