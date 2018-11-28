#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <list>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <valarray>
#include <ctime>
#include <set>
#include <sstream>

using namespace std;

typedef pair<int,int> PII;
int mp[100][100];
char res[100][100];
int h,w;

char DFS(int i, int j, char c)
{
	int m = mp[i][j];
	PII d;
	if (i > 0 && mp[i - 1][j] < m)
	{
		m = mp[i - 1][j];
		d = PII(-1,0);
	}
	if (j > 0 && mp[i][j - 1] < m)
	{
		m = mp[i][j - 1];
		d = PII(0,-1);
	}
	if (j < w - 1 && mp[i][j + 1] < m)
	{
		m = mp[i][j + 1];
		d = PII(0,1);
	}
	if (i < h - 1 && mp[i + 1][j] < m)
	{
		m = mp[i + 1][j];
		d = PII(1,0);
	}
	if (!d.first && !d.second)
	{
		if (!res[i][j])
			res[i][j] = c;
		else
			res[i][j] = min(c,res[i][j]);	
		return res[i][j];
	}
	char t = DFS(i + d.first,j + d.second,c);
	res[i][j] = min(c,t);
	return res[i][j];
}


int main()
{
	freopen("in.in", "rt", stdin);
	freopen("out.out", "wt", stdout);
	int t;
	scanf("%d",&t);
	for (int tt = 0; tt < t; tt++)
	{
		scanf("%d%d",&h,&w);
		for (int i = 0; i < h; i++)
			for (int j = 0; j < w; j++)
				mp[i][j] = res[i][j] = 0;
		for (int i = 0; i < h;i++)
			for(int j = 0; j < w;j++)
				scanf("%d",&mp[i][j]);
		int chr = 'a' - 1;
		
		for (int i = 0; i < h;i++)
			for(int j = 0; j < w; j++)
			{
				char k = DFS(i,j,chr + 1);
				if (chr < k)
					chr = k;
			}


		printf("Case #%d:\n",tt + 1);
		for (int i = 0; i < h; i++)
			for (int j = 0; j < w; j++)
			{
				putchar(res[i][j]);
				if (j != w - 1)
					putchar(' ');
				else
					putchar('\n');
			}		
	}
	
	return 0;
}