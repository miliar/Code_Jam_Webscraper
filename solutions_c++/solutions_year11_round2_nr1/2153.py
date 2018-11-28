#include <cstdio>
const int LIM = 101;
char board[LIM][LIM];
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		double WP[LIM], OWP[LIM], OOWP[LIM], RPI[LIM];
		int n;
		scanf("%d", &n);
		for (int j = 0; j < n; j++)
		{
			scanf("%s", board[j]);
			int w = 0, l = 0;
			for (int k = 0; k < n; k++)
				if (board[j][k] == '1')
					w++;
				else if (board[j][k] == '0')
					l++;
			if (w + l)
				WP[j] = (double)w / (double)(w + l);
			else
				WP[j] = 0;
		}
		for (int j = 0; j < n; j++)
		{
			double accel = 0; // accelerator
			int opps = 0; // opponents' quantity
			for (int k = 0; k < n; k++)
			{
				double forthis = 0;
				if (board[j][k] != '.')
				{
					opps++;
					int win = 0, loose = 0;
					for (int l = 0; l < n; l++)
						if (l != j)
							if (board[k][l] == '1')
								win++;
							else if (board[k][l] == '0')
								loose++;
					if (win + loose)
						forthis = (double)win / (double)(win + loose);
				}
				accel += forthis;
			}
			if (opps)
				OWP[j] = accel / opps;
			else
				OWP[j] = 0;
		}
		for (int j = 0; j < n; j++)
		{
			double accel = 0;
			int opps = 0;
			for (int k = 0; k < n; k++)
				if (board[j][k] != '.')
				{
					opps++;
					accel += OWP[k];
				}
			if (opps)
				OOWP[j] = accel / (double)opps;
			else
				OOWP[j] = 0;
		}
		for (int j = 0; j < n; j++)
			RPI[j] = 0.25 * WP[j] + 0.5 * OWP[j] + 0.25 * OOWP[j];
		printf("Case #%d:\n", i + 1);
		for (int j = 0; j < n; j++)
			printf("%.7lf\n", RPI[j]);
	}
	return 0;
}