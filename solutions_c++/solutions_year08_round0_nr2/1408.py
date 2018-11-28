#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

#include <iostream>
#include <fstream>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <list>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;

const int MAXN = 100+1;
int cx[MAXN],cy[MAXN];
int nx,ny;
bool bmap[MAXN][MAXN];
bool bmark[MAXN];
struct TRIP 
{
	int start;
	int end;
}a2b[MAXN],b2a[MAXN];
int findpath(int u)
{
	int i,j;
	for (i = 0 ; i < ny ; i++)
	{
		if(bmap[u][i] && !bmark[i])
		{
			bmark[i] = 1;
			if ( cy[i] == -1 || findpath(cy[i]) )
			{
				cy[i] = u;
				cx[u] = i;
				return 1;
			}
		}
	}
	return 0;
}
int MaxMatch()
{
	int i,j;
	int res = 0;
	memset(cx, 0xffffffff, sizeof(cx));
	memset(cy, 0xffffffff, sizeof(cy));
	for (i = 0 ; i < nx ; i++)
	{
		if (cx[i] == -1)
		{
			memset(bmark, 0, sizeof(bmark));
			res += findpath(i);
		}
	}
	return res;
}
int main()
{
	int ncase;
	scanf("%d" , &ncase);
	int i,j;
	int m = 0;
	ofstream cout("1.out");
	while (ncase--)
	{
		m++;
		int NA,NB,turntime;
		scanf("%d",&turntime);
		scanf("%d%d" ,&NA,&NB );

		memset(bmap,0,sizeof(bmap));
		int itmp1,itmp2,itmp3,itmp4;
		for (i = 0 ; i < NA ; i++)
		{
			scanf("%d:%d %d:%d",&itmp1,&itmp2,&itmp3,&itmp4);
			a2b[i].start = itmp1*60 + itmp2;
			a2b[i].end = itmp3*60 + itmp4;
		}
		for (i = 0 ; i < NB ; i++)
		{
			scanf("%d:%d %d:%d",&itmp1,&itmp2,&itmp3,&itmp4);
			b2a[i].start = itmp1*60 + itmp2;
			b2a[i].end = itmp3*60 + itmp4;
		}
		nx = NB;
		ny = NA;
		for (i = 0 ; i < NB ; i++)
		{
			for (j = 0 ; j < NA ; j++)
			{
				if (b2a[i].end + turntime <= a2b[j].start)
					bmap[i][j] = 1;
			}
		}
		int res = MaxMatch();
		cout << "Case #"<< m<<":";
		cout <<" "<< NA - res;
		nx = NA;
		ny = NB;
		memset(bmap,0,sizeof(bmap));
		for (i = 0 ; i < NA ; i++)
		{
			for (j = 0 ; j < NB ; j++)
			{
				if (a2b[i].end + turntime <= b2a[j].start)
					bmap[i][j] = 1;
			}
		}
		res = MaxMatch();
		cout <<" "<< NB - res << endl;
	}
	return 0;
}
