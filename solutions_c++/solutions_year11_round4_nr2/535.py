#include<iostream>
#include<cstdio>
#define Max 1005

using namespace std;

char str[Max];

int arr[Max][Max];
long long int M[Max][Max];
long long int PX[Max][Max];
long long int PY[Max][Max];


long long ct(int ax, int ay, int bx, int by, long long R[][Max])
{
	ax--;
	ay--;

	return R[bx][by] + R[ax][ay] - R[bx][ay] - R[ax][by];
}

void ct2(int x, int y, int cx, int cy, long long &px, long long &py, bool ty=0)
{
	if(ty)
	{
		px -= 1LL * (x+x - cx-cx-1) * arr[x][y];
		py -= 1LL * (y+y - cy-cy-1) * arr[x][y];
	}
	else
	{
		px -= 1LL * (x - cx) * arr[x][y];
		py -= 1LL * (y - cy) * arr[x][y];
	}
}

int main()
{
	int z, zi;

	scanf("%d", &z);

	for(zi=1;zi<=z;zi++)
	{
		int n, m, d, i, j, k, ans, t;

		scanf("%d %d %d", &n, &m, &d);

		for(i=1;i<=n;i++)
		{
			scanf(" %s", str);

			for(j=1;j<=m;j++)
				arr[i][j] = str[j-1] - '0' + d;
		}

		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
				M[i][j] = arr[i][j] - M[i-1][j-1] + M[i][j-1] + M[i-1][j];

		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
				PX[i][j] = i*arr[i][j] - PX[i-1][j-1] + 
				PX[i][j-1] + PX[i-1][j];

		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
				PY[i][j] = j*arr[i][j] - PY[i-1][j-1] + 
				PY[i][j-1] + PY[i-1][j];

		ans = -1;
		for(k=min(n, m);k>=3;k--)
		{
			if(k % 2 == 1)
			{
				t = k/2;
				for(i=1;i<=n;i++)
					for(j=1;j<=m;j++)
					{
						if(i+t > n || i-t-1 < 0 || j+t > m || j-t-1 < 0)
							continue;

						long long px, py, cx, cy, tm;

						px = ct(i-t, j-t, i+t, j+t, PX);
						py = ct(i-t, j-t, i+t, j+t, PY);
						tm = ct(i-t, j-t, i+t, j+t, M);

						cx = i*tm;
						cy = j*tm;

						px -= cx;
						py -= cy;

						ct2(i-t, j-t, i, j, px, py);
						ct2(i+t, j-t, i, j, px, py);
						ct2(i+t, j+t, i, j, px, py);
						ct2(i-t, j+t, i, j, px, py);

						if(px == 0 && py == 0)
						{
							ans = k;
						}
					}
			}
			else
			{
				t = k/2;
				for(i=1;i<=n;i++)
					for(j=1;j<=m;j++)
					{

						if(i+t > n || i-t < 0 || j+t > m || j-t < 0)
							continue;
						long long px, py, cx, cy, tm;

						px = ct(i-t+1, j-t+1, i+t, j+t, PX);
						py = ct(i-t+1, j-t+1, i+t, j+t, PY);
						tm = ct(i-t+1, j-t+1, i+t, j+t, M);

						px *= 2;
						py *= 2;
						cx = (i+i+1)*tm;
						cy = (j+j+1)*tm;

						px -= cx;
						py -= cy;

						ct2(i-t+1, j-t+1, i, j, px, py, 1);
						ct2(i+t, j-t+1, i, j, px, py, 1);
						ct2(i+t, j+t, i, j, px, py, 1);
						ct2(i-t+1, j+t, i, j, px, py, 1);

						if(px == 0 && py == 0)
						{
							ans = k;
						}
					}
			}

			if(ans != -1)
				break;
		}
		printf("Case #%d: ", zi);
		if(ans == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", ans);
	}
}
