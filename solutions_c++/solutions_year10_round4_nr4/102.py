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

struct Circle
{
	double x, y, r;

	bool operator<(const Circle& c) const {
		return r < c.r;
	}
};

struct Point
{
	int x, y;

};

Point cow[5000];
Point backet[1000];
int cowCount, backetCount;

Circle v[5000];

double dist(double x1, double y1, double x2, double y2) 
{
	return sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2));
}

const double pi = acos(-1.0);
const double eps = 1e-8;
bool eq(double a, double b, double e = eps)
{
	return fabs(a - b) < e;
}

double sqr(double a)
{
	return a * a;
}
int getSing(double a)
{
	if (a > 0)
		return 1;
	return -1;
}
double solve(Point& backet)
{
	assert (cowCount == 2);
	
	for (int i = 0; i < cowCount; i++)
	{
		v[i].x = cow[i].x;
		v[i].y = cow[i].y;
		v[i].r = dist(cow[i].x, cow[i].y, backet.x, backet.y);
	}

	sort(v, v + cowCount);

	
	double pi = acos(-1.0);

	double d = dist(v[0].x, v[0].y, v[1].x, v[1].y);

	if (d - 1e-7 < v[1].r - v[0].r)
		return pi * v[0].r * v[0].r;

	if (fabs(d - (v[0].r+ v[1].r)) < 1e-8)
		return 0;


	int i = 1;
	int j = 0;

	double r0 = v[i].r;
	double r1 = v[j].r;

	double a = (sqr(r0) - sqr(r1) + sqr(d) ) / (2 * d);

	double h = sqrt(sqr(r0) - sqr(a));

	double x2 = v[i].x + a *  (v[j].x - v[i].x) / d;
	double y2 = v[i].y + a *  (v[j].y - v[i].y) / d;

	double x3 = x2 + h * (v[j].y - v[i].y) / d ;
	double y3 = y2 - h * (v[j].x - v[i].x) / d ;

	double x4 = x2 - h * (v[j].y - v[i].y) / d ;
	double y4 = y2 + h * (v[j].x - v[i].x) / d ;


	double l = dist(x3, y3, x4, y4);

	double area = 0;

	for (int i = 0; i < 2; i++)
	{
		double r = v[i].r;
		double a = acos((r * r + r * r - l * l) / (2 * r * r));

		double x = a * r * r / 2 - r * r * sin(a) / 2;

		int sign1 = getSing((v[i].x - x4) * (y3 - y4) - (v[i].y - y4) * (x3 - x4));
		int sign2 = getSing((v[i].x - x4) * (v[1 - i].y - y4) - (v[i].y - y4) * (v[1 - i].x - x4));

		if (sign1 != sign2)
			x = pi * r * r - x;

		

		area += x;

	}


	return area;
}

int main(int argc, char* argv[])
{
//#ifdef _DEBUG
	freopen("Test.in", "r", stdin);
//#endif

	int T;
	scanf("%d", &T);


	for (int nTest = 1; nTest <= T; nTest++)
	{		
		scanf("%d %d", &cowCount, &backetCount);

		for (int i = 0; i < cowCount; i++)
		{
			scanf("%d %d", &cow[i].x, &cow[i].y);
		}

		for (int i = 0; i < backetCount; i++)
		{
			scanf("%d %d", &backet[i].x, &backet[i].y);
		}

		printf("Case #%d:", nTest);


		for (int i = 0; i < backetCount; i++)
		{
			double res = solve(backet[i]);

			printf(" %.7lf", res);
		}

		printf("\n");
	}

	return 0;
}


