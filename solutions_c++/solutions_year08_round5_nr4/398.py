#include <iostream>

using namespace std;

int main()
{
	int N;
	scanf("%d", &N);
	for (int ca=1; ca<=N; ca++)
	{


		int H, W, R;
		scanf("%d%d%d", &H, &W, &R);
		int a[100][100];
		bool b[100][100];
		int fx[2][2] = {{1,2},{2,1}};

		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		for (int i=0; i<R; i++)
		{
			int x, y;
			scanf("%d%d", &x, &y);
			b[x-1][y-1] = 1;
			//printf("%d %d\n", x, y);
		}

		a[0][0] = 1;
		for (int i=0; i<H; i++)
			for (int j=0; j<W; j++)
				if (b[i][j])
					a[i][j] = 0;
				else
				for (int k=0; k<2; k++)
				{
					int x = i-fx[k][0];
					int y = j-fx[k][1];
					if (x >= 0 && y >=0)
					{
						a[i][j] += a[x][y];
						a[i][j] %= 10007;
					}
				}
				/*
		for (int i=0; i<H; i++)
		{
			for (int j=0; j<H; j++)
				printf("%d ", a[i][j]);
			putchar(10);
		}
		*/
		printf("Case #%d: %d\n", ca, a[H-1][W-1]);
	}
}
