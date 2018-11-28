#include <stdio.h>

int matrix[2][100][100];

void resetmatrix(int i)
{
	for (int k = 0; k < 100; k++)
	{
		for (int j = 0; j < 100; j++)
		{
			matrix[i][k][j] = -1;
		}
	}
}

int main()
{
	int T;
	int N;
	bool B[100];
	int but[100];

	scanf("%d", &T);
	

	for (int j = 0; j < T; j++)
	{
		resetmatrix(1);
		matrix[1][0][0] = 0;

		char tlf[3];
		scanf("%d", &N);

		for (int k = 0; k < N; k++)
		{
			scanf("%s %d", tlf, &but[k]);
			but[k]--;
			B[k] = (tlf[0] == 'O');
		}

		bool foundit = false;
		int time = 0;
		while (!foundit)
		{
			int now = time % 2;
			time++;
			//fprintf(stderr, "Testing %d\n", time);					
			resetmatrix(now);


			for (int i = 0; i < 100; i++)
			{
				for (int j = 0; j < 100; j++)
				{
					if (matrix[!now][i][j] < 0) continue;

					for (int step = 0; step < 9; step++)
					{						
						int dx[2] = {step % 3, step / 3};
						for (int k = 0; k < 2; k++)
						{
							dx[k]--;
						}

						int x[2] = {i, j};
						int newx[2] = {i + dx[0], j + dx[1]};

						bool ok = true;
						for (int r = 0; r < 2; r++)
						{
							if (newx[r] < 0 || newx[r] > 99) ok = false;
						}
						if (!ok) continue;

						int index = matrix[!now][i][j];

						for (int k = 0; k < 2; k++)
						{
							if (!dx[k] && B[index] == k && but[index] == newx[k])
							{
								index++;
								break;
							}
						}

						if (index > matrix[now][newx[0]][newx[1]])
						{
							matrix[now][newx[0]][newx[1]] = index;
						}

						if (index == N)
						{
							foundit = true;
							goto end;
						}
					}
				}
			}
end:;
		}
		printf("Case #%d: %d\n", j + 1, time);
	}
}