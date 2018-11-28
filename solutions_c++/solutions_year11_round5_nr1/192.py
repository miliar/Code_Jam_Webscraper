#include <assert.h> 
#include <ctype.h> 
#include <float.h> 
#include <math.h> 
#include <stdio.h> 
#include <string> 
#include <stdlib.h> 
#include <time.h> 
#include <algorithm> 
#include <numeric> 
#include <functional> 
#include <utility> 
#include <vector> 
#include <list> 
#include <set> 
#include <map> 
#include <queue> 
#include <stack> 
#include <sstream> 
#include <iostream> 
#include <memory.h>

using namespace std; 

#define rep(i,n) for(int i=0;i<(n);++i)
#define clr(a,b) memset(a,b,sizeof(a)); 
#define all(c) (c).begin(), (c).end() 
#define inf 1000000000 

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<string> vs;
typedef vector<int> vi;

struct Point
{
	int x, y;
};


void build(vector<Point>& l, vector<double>& ax, vector<double> &y)
{
	int cur = 0;
	for (int i = 0; i < ax.size(); i++)
	{
		if (cur + 1 < l.size() && ax[i] == l[cur + 1].x)
			cur++;

		if (ax[i] == l[cur].x)
		{
			y[i] = l[cur].y;
			continue;;
		}

		y[i] = l[cur].y + (l[cur + 1].y -l[cur].y) * (double(ax[i] - l[cur].x)) / (l[cur + 1].x - l[cur].x);
	}

	assert (cur == l.size() - 1);
}

void solveTest()
{
	printf("\n");

	int W, L, U, G;
	cin >> W >> L >> U >> G;

	vector<Point> l(L);
	for (int i = 0; i < L; i++)
		cin >> l[i].x >> l[i].y;

	vector<Point> u(U);
	for (int i = 0; i < U; i++)
		cin >> u[i].x >> u[i].y;

	double totalArea = 0;

	for (int i = 1; i < U; i++)
	{
		assert (u[i].x > u[i - 1].x);
		totalArea += 0.5 * (u[i].x - u[i - 1].x) * (u[i - 1].y + u[i].y);
	}
	for (int i = 1; i < L; i++)
	{
		assert (l[i].x > l[i - 1].x);

		totalArea -= 0.5 * (l[i].x - l[i - 1].x) * (l[i - 1].y + l[i].y);
	}
	
	vector<double> ax;
	rep(i, U) ax.push_back(u[i].x);
	rep(i, L) ax.push_back(l[i].x);

	sort(ax.begin(), ax.end());
	ax.resize(unique(all(ax)) - ax.begin());

	vector<double> yl(ax.size());
	vector<double> yu(ax.size());

	build(l, ax, yl);
	build(u, ax, yu);

	double pieceArea = totalArea / G;

	int px = 0;

	for (int cut = 0; cut < G ; cut++)
	{
		double curArea = 0;
		while (px + 1 < ax.size())
		{
			double part = 0.5 * (ax[px + 1] - ax[px]) * (yu[px + 1] + yu[px]);
			part -= 0.5 * (ax[px + 1] - ax[px]) * (yl[px + 1] + yl[px]);
			
			if (part + curArea <= pieceArea)
			{
				curArea += part;
				px++;
			}
			else
				break;
		}

		if (pieceArea > curArea + 1e-6)
		{
			double lx = ax[px];
			double rx = ax[px + 1];

			while (rx - lx > 1e-10)
			{
				double mx = (rx + lx) / 2;

				double ymu = yu[px] + (yu[px + 1] - yu[px]) * (double(mx - ax[px])) / (ax[px + 1] - ax[px]);
				double yml = yl[px] + (yl[px + 1] - yl[px]) * (double(mx - ax[px])) / (ax[px + 1] - ax[px]);

				double part = 0.5 * (mx - ax[px]) * (ymu + yu[px]);
				part -= 0.5 * (mx - ax[px]) * (yml + yl[px]);

				if (curArea + part > pieceArea)
				{
					rx = mx;
				}
				else
				{
					lx = mx;
				}
			}

			double mx = (rx + lx) / 2;

			double ymu = yu[px] + (yu[px + 1] - yu[px]) * (double(mx - ax[px])) / (ax[px + 1] - ax[px]);
			double yml = yl[px] + (yl[px + 1] - yl[px]) * (double(mx - ax[px])) / (ax[px + 1] - ax[px]);

			curArea += 0.5 * (mx - ax[px]) * (ymu + yu[px]);
			curArea -= 0.5 * (mx - ax[px]) * (yml + yl[px]);

			ax[px] = mx;

			yu[px] = ymu;
			yl[px] = yml;
		}

		assert (fabs(pieceArea - curArea) < 1e-6);
		
		if (cut != G - 1)
		printf("%.8lf\n", ax[px]);

	}

	assert (fabs(ax[px] - W) < 1e-7);

}


int main(int argc, char* argv[])
{
	freopen("test.in", "r", stdin);

	int T;
	scanf("%d", &T);

	for (int nTest = 1; nTest <= T; nTest++)
	{		
		printf("Case #%d:", nTest);

		solveTest();

		fflush(stdout);
	} 

	return 0;
}


