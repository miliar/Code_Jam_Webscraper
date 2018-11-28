#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	const int tx[4] = {-1,0,0,1};
	const int ty[4] = {0,-1,1,0};
	const int maxw = 120;
	int a[maxw][maxw];
	int map[maxw][maxw];
	int d[maxw][maxw];
	int qx[maxw * maxw];
	int qy[maxw * maxw];
	char c[27];
	int t, tc;
	int h, w;
	int i, j, k;
	int x, y;
	int xx, yy;
	int p, q;
	int mark;
	int head, tail;
	fstream inf("b.in");
	ofstream ouf("b.out");
	inf>>t;
	for (tc = 1; tc <= t; tc++) {
		inf>>h>>w;
		for (i = 0; i < h; i++)
			for (j = 0; j < w; j++)
				inf>>a[i][j];
		for (i = 0; i < h; i++)
			for (j = 0; j < w; j++)
			{
				p = 0;
				for (k = 0; k < 4; k++)
				{
					x = i + tx[k]; y = j + ty[k];
					if (x < 0 || x >= h || y < 0 || y >= w ) continue;
					if (a[x][y] < a[i][j])
						if (p == 0 || a[x][y] < q) {p = k + 1; q = a[x][y];}
				}
				d[i][j] = p;
			}
		mark = 0;
		for (i = 0; i < h; i++)
			for (j = 0; j < w; j++)
				if (d[i][j] == 0) {
					mark ++;
					qx[0] = i; qy[0] = j;
					head = 0; tail = 0;
					map[i][j] = mark;
					while (head <= tail)
					{
						for (k = 0; k < 4; k++)
						{
							x = qx[head] + tx[k]; y = qy[head] + ty[k];
							if (x < 0 || x >= h || y < 0 || y >= w ) continue;
							if (d[x][y] != 0) {
								xx = x + tx[d[x][y] - 1];
								yy = y + ty[d[x][y] - 1];
								if (xx == qx[head] && yy == qy[head])
								{
									tail ++;
									qx[tail] = x; qy[tail] = y;
									map[x][y] = mark;
								}
							}
						}
						head ++;
					}
				}
		mark = 0;
		for (i = 0; i < 27; i++) c[i] = 1;
		for (i = 0; i < h; i++)
			for (j = 0; j < w; j++)
				if (c[map[i][j]] == 1)
				{
					mark ++;
					c[map[i][j]] = 96 + mark;
				}
		ouf<<"Case #"<<tc<<":"<<endl;
		for (i = 0; i < h; i++)
		{
			for (j = 0; j < w - 1; j++)
				ouf<<c[map[i][j]]<<' ';
			ouf<<c[map[i][w - 1]]<<endl;
		}
	}
	inf.close();
	ouf.close();
}