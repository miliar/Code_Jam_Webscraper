#include <stdio.h>
#include <stdlib.h>
#include <iostream>

char data[4][5];

int main()
{
	int case_total, case_current;
	int total_dots;
	int i, j;
	int streak_horz, streak_vert[4], streak_diag[2];
	int status;
	char streak_horz_c, streak_vert_c[4], streak_diag_c[2];

	scanf("%d", &case_total);

	for (case_current = 1; case_current <= case_total; case_current++)
	{
		total_dots = 0;
		streak_vert[0] = 0;
		streak_vert[1] = 0;
		streak_vert[2] = 0;
		streak_vert[3] = 0;
		streak_diag[0] = 0;
		streak_diag[1] = 0;
		streak_vert_c[0] = 0;
		streak_vert_c[1] = 0;
		streak_vert_c[2] = 0;
		streak_vert_c[3] = 0;
		streak_diag_c[0] = 0;
		streak_diag_c[1] = 0;

		status = 0;

		for (i = 0; i < 4; i++)
		{
			scanf("%s", data[i]);
			streak_horz = 0;
			streak_horz_c = 0;
			for (j = 0; j < 4 && !status; j++)
			{
				if (data[i][j] == '.')
				{
					total_dots++;

					streak_horz = 0;
					streak_horz_c = 0;
					streak_vert[j] = 0;
					streak_vert_c[j] = 0;
					if (i == j)
					{
						streak_diag[0] = 0;
						streak_diag_c[0] = 0;
					}
					if (i == 3 - j)
					{
						streak_diag[1] = 0;
						streak_diag_c[1] = 0;
					}
					continue;
				}

				if (streak_horz_c == 0)
				{
					streak_horz++;
					streak_horz_c = data[i][j];
				}
				else if (data[i][j] == streak_horz_c || data[i][j] == 'T')
				{
					streak_horz++;
				}
				else
				{
					streak_horz = 1;
					streak_horz_c = data[i][j];
				}

				if (streak_horz >= 4)
				{
					status = (streak_horz_c == 'X') ? 1 : 2;
					break;
				}

				if (streak_vert_c[j] == 0)
				{
					streak_vert[j]++;
					streak_vert_c[j] = data[i][j];
				}
				else if (data[i][j] == streak_vert_c[j] || data[i][j] == 'T')
				{
					streak_vert[j]++;
				}
				else
				{
					streak_vert[j] = 1;
					streak_vert_c[j] = data[i][j];
				}

				if (streak_vert[j] >= 4)
				{
					status = (streak_vert_c[j] == 'X') ? 1 : 2;
					break;
				}

				if (i == j)
				{
					if (streak_diag_c[0] == 0)
					{
						streak_diag[0]++;
						streak_diag_c[0] = data[i][j];
					}
					else if (data[i][j] == streak_diag_c[0] || data[i][j] == 'T')
					{
						streak_diag[0]++;
					}
					else
					{
						streak_diag[0] = 1;
						streak_diag_c[0] = data[i][j];
					}

					if (streak_diag[0] >= 4)
					{
						status = (streak_diag_c[0] == 'X') ? 1 : 2;
						break;
					}
				}

				if (i == 3 - j)
				{
					if (streak_diag_c[1] == 0)
					{
						streak_diag[1]++;
						streak_diag_c[1] = data[i][j];
					}
					else if (data[i][j] == streak_diag_c[1] || data[i][j] == 'T')
					{
						streak_diag[1]++;
					}
					else
					{
						streak_diag[1] = 1;
						streak_diag_c[1] = data[i][j];
					}

					if (streak_diag[1] >= 4)
					{
						status = (streak_diag_c[1] == 'X') ? 1 : 2;
						break;
					}
				}
			}
		}

		printf("Case #%d: ", case_current);
		if (!status)
		{
			printf("%s", (total_dots) ? "Game has not completed" : "Draw");
		}
		else
		{
			printf("%c won", (status - 1) ? 'O' : 'X');
		}
		printf("\n");
	}

	return 0;
}
