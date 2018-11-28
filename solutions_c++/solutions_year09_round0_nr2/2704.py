#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

int alti[10003][10003];
int flow[10003][10003];
char alpha[10003][10003];
int sink[10003];
int sinkix = 0;
char ch = 'a';


map<char,char> solve(int h,int w)
{
	memset(flow,0,sizeof(flow));
	memset(alpha,0,sizeof(alpha));
	memset(sink,0,sizeof(sink));
	sinkix = 0;
	ch = 'a';

	for (int i = 0;i <= h+1;i++)
	{
		alti[i][0] = 100000;
		alti[i][w+1] = 100000;
	}
	for (int j = 0;j <= w+1;j++)
	{
		alti[0][j] = 100000;
		alti[h+1][j] = 100000;
	}

	for (int i = 1;i <= h;i++)
	{
		for (int j = 1;j <= w;j++)
		{
			int level[4] = {alti[i-1][j]-alti[i][j],alti[i][j-1]-alti[i][j],alti[i][j+1]-alti[i][j],alti[i+1][j]-alti[i][j]};
			int minval = 0,minix = 0;
			for (int k = 0;k < 4;k++)
			{
				if (level[k] < minval)
				{
					minval = level[k];
					minix = k;
				}
			}
			if (minval < 0)
			{
				if (minix == 0)
				{
					flow[i-1][j] |= 1;
				}
				else if (minix == 1)
				{
					flow[i][j-1] |= 2;
				}
				else if (minix == 2)
				{
					flow[i][j+1] |= 4;
				}
				else
				{
					flow[i+1][j] |= 8;
				}
			}
			else
			{
				sink[sinkix++] = (i-1)*w+(j-1);
			}
		}
	}

	/*
	cout << "flow jk" << endl;
	for (int j = 1;j <= h;j++)
	{
		for (int k = 1;k <= w;k++)
		{
			cout << flow[j][k] << " ";
		}
		cout << endl;
	}
	*/

	for (int ix = 0;ix < sinkix;ix++,ch++)
	{
		queue<int> coord;
		coord.push(sink[ix]);
		while (!coord.empty())
		{
			int curr = coord.front();
			coord.pop();
			int i = curr/w+1,j = curr%w+1;
			alpha[i][j] = ch;
			if ((flow[i][j] & 1) == 1)
			{
				coord.push((i+1-1)*w+(j-1));
			}
			if ((flow[i][j] & 2) == 2)
			{
				coord.push((i-1)*w+j+1-1);
			}
			if ((flow[i][j] & 4) == 4)
			{
				coord.push((i-1)*w+j-1-1);
			}
			if ((flow[i][j] & 8) == 8)
			{
				coord.push((i-1-1)*w+j-1);
			}
		}
	}

	map<char,char> charmap;
	char chix = 'a',lastchar = '\0';
	for (int i = 1;i <= h;i++)
	{
		for (int j = 1;j <= w;j++)
		{
			if (alpha[i][j] != lastchar)
			{
				charmap.insert(make_pair(alpha[i][j],chix++));
				lastchar = alpha[i][j];
			}
		}
	}
	return charmap;
}

int main()
{
	ofstream fout("bout.txt");
	FILE *fp=fopen("B-small-attempt0.in","r");

	int t;
	fscanf(fp,"%d\n",&t);
	for (int i = 0;i < t;i++)
	{
		int h,w;
		fscanf(fp,"%d %d\n",&h,&w);
		for (int j = 1;j <= h;j++)
		{
			for (int k = 1;k <= w;k++)
			{
				fscanf(fp,"%d\n",&alti[j][k]);
			}
		}

		map<char,char> charm = solve(h,w);

		fout << "Case #" << i+1 << ":" << endl;
		for (int j = 1;j <= h;j++)
		{
			for (int k = 1;k <= w;k++)
			{
				fout << charm[alpha[j][k]] << " ";
			}
			fout << endl;
		}
	}	
	return 0;
}