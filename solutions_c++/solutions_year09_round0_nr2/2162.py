#include <iostream>
#include <string>

using namespace std;

void go(int *amap, int *bmap, int run, char *runs, char &b, int h, int w, int x, int y);

void main()
{
	int t, h, w, x, y;
	int *amap = new int[10000], *bmap = new int[10000], run;
	char *runs = new char[10000], b;

	cin >> t;
	for (int a = 1; a <= t; a++)
	{
		cin >> h >> w;
		b = 'a';
		run = 0;
		memset(amap, 0, 10000 * sizeof(int));
		memset(bmap, 0, 10000 * sizeof(int));
		memset(runs, 0, 10000 * sizeof(char));
		for (y = 0; y < h; y++)
		{
			for (x = 0; x < w; x++)
			{
				cin >> amap[y * w + x];
			}
		}
		for (y = 0; y < h; y++)
		{
			for (x = 0; x < w; x++)
			{
				run++;
				go(amap, bmap, run, runs, b, h, w, x, y);
			}
		}
		cout << "Case #" << a << ":\n";
		for (y = 0; y < h; y++)
		{
			for (x = 0; x < w; x++)
			{
				cout << runs[bmap[y * w + x]] << " ";
			}
			cout << endl;
		}
	}
}

void go(int *amap, int *bmap, int run, char *runs, char &b, int h, int w, int x, int y)
{
	unsigned int c, min, nx, ny;

	while (bmap[y * w + x] == 0)
	{
		c = amap[y * w + x];
		bmap[y * w + x] = run;
		min = c;
		if (y > 0     && amap[y * w + x - w] < min)//n
		{
			min = amap[y * w + x - w];
			nx = x;
			ny = y - 1;
		}
		if (x > 0     && amap[y * w + x - 1] < min)//w
		{
			min = amap[y * w + x - 1];
			nx = x - 1;
			ny = y;
		}
		if (x < w - 1 && amap[y * w + x + 1] < min)//e
		{
			min = amap[y * w + x + 1];
			nx = x + 1;
			ny = y;
		}
		if (y < h - 1 && amap[y * w + x + w] < min)//s
		{
			min = amap[y * w + x + w];
			nx = x;
			ny = y + 1;
		}
		if (min == c)
		{
			runs[run] = b++;
			return;
		}
		x = nx;
		y = ny;
	}
	runs[run] = runs[bmap[y * w + x]];
}
