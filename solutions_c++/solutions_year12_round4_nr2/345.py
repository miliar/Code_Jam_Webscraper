#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <cmath>
#include <map>
#include <list>
#include <algorithm>
#include <assert.h>
using namespace std;

ifstream fin("input.in");
ofstream fout("output.out");

struct Pos
{
	double x,y;
};

struct Person
{
	double r;
	int i;
};

bool operator<(const Person& p1, const Person& p2)
{
	return p1.r > p2.r;
}

int n;
Person a[1010];
Pos ans[1010];
double W, L;

bool inter(int j, int i, double x2, double y2)
{
	double x1 = ans[a[j].i].x;
	double y1 = ans[a[j].i].y;
	double dx = fabs(x1 - x2);
	double dy = fabs(y1 - y2);
	double L = sqrt(dx*dx + dy*dy);
	return a[i].r + a[j].r > L;
}

bool tryInsert(int i, double x, double y)
{
	int j;
	if(x < 0 || x > W || y < 0 || y > L)
		return 0;

	for(j=0; j<i; ++j)
		if(inter(j, i, x,y))
			break;
	if(j<i)
		return 0;

	ans[a[i].i].x = x;
	ans[a[i].i].y = y;
	return 1;
}

bool tryUp(int j, int i)
{
	double x = ans[a[j].i].x;
	double y = ans[a[j].i].y;
	y += a[i].r + a[j].r;
	return tryInsert(i, x, y);
}

bool tryDown(int j, int i)
{
	double x = ans[a[j].i].x;
	double y = ans[a[j].i].y;
	y -= a[i].r + a[j].r;
	return tryInsert(i, x, y);
}
bool tryLeft(int j, int i)
{
	double x = ans[a[j].i].x;
	double y = ans[a[j].i].y;
	x -= a[i].r + a[j].r;
	return tryInsert(i, x, y);
}
bool tryRight(int j, int i)
{
	double x = ans[a[j].i].x;
	double y = ans[a[j].i].y;
	x += a[i].r + a[j].r;
	return tryInsert(i, x, y);
}

bool tryUpLeft(int j, int i)
{
	double x = ans[a[j].i].x;
	double y = ans[a[j].i].y;
	y += a[i].r + a[j].r;
	x -= a[i].r + a[j].r;
	return tryInsert(i, x, y);
}

bool tryUpRight(int j, int i)
{
	double x = ans[a[j].i].x;
	double y = ans[a[j].i].y;
	y += a[i].r + a[j].r;
	x += a[i].r + a[j].r;
	return tryInsert(i, x, y);
}


bool tryDownLeft(int j, int i)
{
	double x = ans[a[j].i].x;
	double y = ans[a[j].i].y;
	y -= a[i].r + a[j].r;
	x -= a[i].r + a[j].r;
	return tryInsert(i, x, y);
}


bool tryDownRight(int j, int i)
{
	double x = ans[a[j].i].x;
	double y = ans[a[j].i].y;
	y -= a[i].r + a[j].r;
	x += a[i].r + a[j].r;
	return tryInsert(i, x, y);
}


int main()
{
	int t,tt,i,j;
	fin>>tt;
	for(t=1; t<=tt; ++t)
	{
		fin>>n>>W>>L;
		for(i=0; i<n; ++i)
		{
			fin>>a[i].r;
			a[i].i = i;
		}
		sort(a, a+n);
		for(i=0; i<n; ++i)
		{
			if(tryInsert(i,0,0))
				continue;
			if(tryInsert(i,W,0))
				continue;
			if(tryInsert(i,0,L))
				continue;
			if(tryInsert(i,W,L))
				continue;

			for(j=i-1; j>=0; --j)
			{
				if(tryUp(j,i))
					break;
				if(tryDown(j,i))
					break;
				if(tryLeft(j,i))
					break;
				if(tryRight(j,i))
					break;
				if(tryUpLeft(j,i))
					break;
				if(tryUpRight(j,i))
					break;
				if(tryDownLeft(j,i))
					break;
				if(tryDownRight(j,i))
					break;
			}
			assert(j != i);
		}
		fout<<"Case #"<<t<<":";
		for(i=0; i<n; ++i)
			fout<<fixed<<' '<<ans[i].x<<' '<<ans[i].y;
		fout<<endl;
	}
	return 0;
}