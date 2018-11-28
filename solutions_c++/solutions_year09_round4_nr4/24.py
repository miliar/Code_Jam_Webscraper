#include <iostream>
#include <cmath>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cstring>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

struct Circle
{
	double x, y, r;
};

int n;
Circle c[100];

double dist(int a, int b)
{
	return sqrt((c[a].x-c[b].x)*(c[a].x-c[b].x)+(c[a].y-c[b].y)*(c[a].y-c[b].y));
}

bool inside(int x, int y)
{
	if (c[x].r+1e-8>=c[y].r)
		if (c[x].r-c[y].r+1e-8>dist(x,y))
			return true;
	return false;
}

double max(double a, double b)
{
	if (a<b)
		return b;
	return a;
}

double min(double a, double b)
{
	if (a<b)
		return a;
	return b;
}

double work()
{
	if (n==2)
	{
		if (inside(0,1))
			n=1;
		else if (inside(1,0))
		{
			n=1;
			Circle t = c[0];
			c[0]=c[1];
			c[1]=t;
		}
	}
	else if (n==3)
	{
		int p[3];
		for (int i=0; i<3; i++)
			p[i]=0;
		for (int i=0; i<3; i++)
			for (int j=0; j<3; j++)
				if (i!=j)
					if (p[i]==0&&p[j]==0&&inside(i,j))
						p[j]=1;
		if (p[0]==1)
		{
			c[0]=c[1];
			c[1]=c[2];
			n--;
		}
		if (p[0]==1)
		{
			c[0]=c[1];
			c[1]=c[2];
			n--;
		}
		if (n>1&&p[1]==1)
		{
			c[1]=c[2];
			n--;
		}
	}

	double ans = 0;
	if (n==1)
		return c[0].r;
	else if (n==2)
	{
		if (c[0].r>c[1].r)
			return c[0].r;
		else
			return c[1].r;
	}
	else if (n==3)
	{
		ans = max(c[0].r + c[0].r, c[1].r+c[2].r+dist(1,2));
		ans = min(ans, max(c[1].r + c[1].r, c[0].r+c[2].r+dist(0,2)));
		ans = min(ans, max(c[2].r + c[2].r, c[0].r+c[1].r+dist(0,1)));
		ans/=2;
	}
	return ans;
}

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);

	int T;
	cin >> T;
	for (int i=1; i<=T; i++)
	{
		cin >> n;
		for (int j=0; j<n; j++)
			cin >> c[j].x >> c[j].y >> c[j].r;
		printf("Case #%d: %0.8lf\n", i, work());
	}

	return 0;
}