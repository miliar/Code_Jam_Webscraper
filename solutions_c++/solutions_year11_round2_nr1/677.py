#include <iostream>

using namespace std;


char board[110][110];
double rpi[110];
int N[110];
double wp[110];
double owp[110];
double oowp[110];


int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testCount;
	scanf("%d", &testCount);
	for(int testNumber = 1; testNumber <= testCount; testNumber++)
	{
		printf("Case #%d:\n", testNumber);
		memset(board, 0, sizeof board);
		memset(rpi, 0, sizeof rpi);
		memset(wp, 0, sizeof wp);
		memset(owp, 0, sizeof owp);
		memset(oowp, 0, sizeof oowp);
		memset(N, 0, sizeof N);
		int n;
		scanf("%d", &n);
		for(int i = 0; i < n; i++)
		{
			scanf("%s", board[i]);
		}
		for(int i = 0; i < n; i++)
		{
			int win = 0;
			int all = 0;
			for(int j = 0; j < n; j++)
			{
				if(board[i][j] == '1')
				{
					win++;
					all++;
					N[i]++;
				}
				else if(board[i][j] == '0')
				{
					all++;
					N[i]++;
				}
			}
			wp[i] = (win + 0.) / (all + 0.);
		}
		for(int i = 0; i < n; i++)
		{
			double x = 0;
			int all = 0;
			for(int j = 0; j < n; j++)
			{
				if(board[i][j] != '.')
				{
					x += (wp[j] * N[j] - (board[j][i] - '0')) / (N[j] - 1);
					all++;
				}
			}
			owp[i] = x / all;
		}
		for(int i = 0; i < n; i++)
		{
			double x = 0;
			int all = 0;
			for(int j = 0; j < n; j++)
			{
				if(board[i][j] != '.')
				{
					x += owp[j];
					all++;
				}
			}
			oowp[i] = x / all;
		}
		for(int i = 0; i < n; i++)
		{
			rpi[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
			printf("%.10lf\n", rpi[i]);
		}
	}
	return 0;
}