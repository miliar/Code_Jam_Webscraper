//============================================================================
// Name        : watersheds.cpp
// Author      : Fify
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <memory.h>
using namespace std;

int mp1[105][105];
char mp2[105][105];
int h, w;
char ch;

int main()
{
	freopen("/home/fify/Desktop/data2.in", "r", stdin);
	freopen("/home/fify/Desktop/data2.out", "w", stdout);
	void solve();
	int t;
	cin>>t;
	for(int i = 0;i<t;i++)
	{
		solve();
	}
}

void solve()
{
	static int cas = 1;
	ch = 'a';

	int bfs1(int i, int j);
	int bfs2(int i, int j);

	cin >> h >> w;
	for(int i = 0;i<h;i++)
	{
		for(int j = 0;j<w;j++)
		{
			cin >> mp1[i][j];
		}
	}

	memset(mp2, 0, sizeof(mp2));

	for(int i = 0;i<h;i++)
	{
		for(int j = 0;j<w;j++)
		{
			int tmp ;
			if((tmp = bfs1(i, j)) >= 0)
			{
				ch ++;
			}
		}
	}

	printf("Case #%d:\n", cas++);
	for(int i = 0;i<h;i++)
	{
		for(int j = 0;j<w - 1;j++)
		{
			cout << mp2[i][j] << " ";
		}
		cout << mp2[i][w-1] << endl;

	}
}

int bfs1(int i, int j)
{
	int bfs2(int i, int j);
	int getFirst(int i, int j);

	if(mp2[i][j] != 0)
		return -1;

	mp2[i][j] = ch;
	bfs2(i, j);

	switch(getFirst(i, j))
	{
	case 0:
		bfs1(i - 1, j);
		break;
	case 1:
		bfs1(i, j -1);
		break;
	case 2:
		bfs1(i, j +1);
		break;
	case 3:
		bfs1(i + 1, j);
		break;
	default:
		break;
	}

	return 0;
}

int bfs2(int i, int j)
{
	if(mp2[i][j] == 0)
	{
		mp2[i][j] = ch;
	}
	else if(mp2[i][j] != ch)
	{
		return 0;
	}
	int getFirst(int i, int j);
	if(i - 1 >= 0 && getFirst(i - 1, j) == 3)
		bfs2(i - 1, j);
	if(j - 1 >= 0 && getFirst(i, j - 1) == 2)
		bfs2(i, j - 1);
	if(j + 1 < w && getFirst(i, j + 1) == 1)
		bfs2(i, j+1);
	if(i + 1 < h && getFirst(i + 1, j) == 0)
		bfs2(i + 1, j);

	return 0;
}

int getFirst(int i, int j)
{
	int res = -1;
	int tmp = mp1[i][j];

	if(i - 1 >= 0 && mp1[i-1][j] < tmp)
	{
		tmp = mp1[i-1][j];
		res = 0;
	}
	if(j - 1 >= 0 && mp1[i][j-1] < tmp)
	{
		tmp = mp1[i][j-1];
		res = 1;
	}
	if(j + 1 < w && mp1[i][j+1] < tmp)
	{
		tmp = mp1[i][j+1];
		res = 2;
	}
	if(i + 1 < h && mp1[i+1][j] < tmp)
	{
		tmp = mp1[i+1][j];
		res = 3;
	}

	return res;
}

