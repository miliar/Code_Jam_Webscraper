#include <iostream>
#include <fstream>
using namespace std;

int t, h, w, tt, c;
int map[120][120];
int res[120][120];
ifstream ifs;
ofstream ofs;

void readdata()
{
	int i, j;
	
	ifs >> h >> w;
	for (i = 0; i < h; ++i)
		for (j = 0; j < w; ++j )
			ifs >> map[i][j];
		
}

void find(int x, int y)
{
	int qx[12000];
	int qy[12000];
	int i, j, tc, bx, by;
	
	i = 0;
	tc = 0;
	qx[i] = x;
	qy[i] = y;
	while (true)
	{
		bx = qx[i];
		by = qy[i];
		
		if ((qx[i] - 1 >= 0) && (map[qx[i] - 1][qy[i]] < map[bx][by]))
		{
			bx = qx[i] - 1;
			by = qy[i];
		}
		
		if ((qy[i] - 1 >= 0) && (map[qx[i]][qy[i] - 1] < map[bx][by]))
		{
			bx = qx[i];
			by = qy[i] - 1;
		}
		
		if ((qy[i] + 1 < w) && (map[qx[i]][qy[i] + 1] < map[bx][by]))
		{
			bx = qx[i];
			by = qy[i] + 1;
		}
		
		if ((qx[i] + 1 < h) && (map[qx[i] + 1][qy[i]] < map[bx][by]))
		{
			bx = qx[i] + 1;
			by = qy[i];
		}
		
		if ((bx == qx[i]) && (by == qy[i]))
			break;
		
		++i;
		qx[i] = bx;
		qy[i] = by;
		
		tc = res[bx][by];
		if (tc != 0) 
			break;
	}
	
	if (tc == 0)
		tc = ++c;
	
	for (j = 0; j <= i; ++j)
		res[qx[j]][qy[j]] = tc;
}

void work()
{
	int i, j;
	
	for (i = 0; i < h; ++i)
		for (j = 0; j < w; ++j)
			res[i][j] = 0;
	c = 0;
	for (i = 0; i < h; ++i)
		for (j = 0; j < w; ++j)
			if (res[i][j] == 0)
				find(i, j);
			
}

void print()
{
	int i, j;
	ofs << "Case #" << (tt + 1) << ":" << endl;
	for (i = 0; i < h; ++i)
	{
		for (j = 0; j < w; ++j)
		{
			ofs << (char)('a' + res[i][j] - 1);
			if (j != w - 1) ofs << " ";
		}
		ofs << endl;
	}
}

int main()
{
	ifs.open("qr2.in");
	ofs.open("qr2.out");
	
	ifs >> t;
	
	for (tt = 0; tt < t; ++tt)
	{
		readdata();
		work();
		print();
	}
	
	ifs.close();
	ofs.close();
}
