#include <iostream>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>

#define MAX 204800
#define EPS 0.0001
#define NUM_RECT 64
#define PI (long double)3.1415926535897932384626433832795

using namespace std;
FILE *in; FILE *out;

double MIN_SIDE;
double totalArea, area;
double radius, thickness;
double line, gap, fly;
double realRadius, realArea, rectSide;


inline int isInside(double x, double y)
{
	return sqrt(x * x + y * y) <= realRadius;
}


double recArea(double x, double y, double side)
{
	if (!isInside(x, y)) return 0.0;
	if (isInside(x + side, y + side)) return side * side;
	if (side < MIN_SIDE) return 0.0;
	
	double ans = 0, half = side / 2.0;

	ans += recArea(x, y, half);
	ans += recArea(x, y + half, half);
	ans += recArea(x + half, y, half);
	ans += recArea(x + half, y + half, half);
	
	return ans;
}


double findArea(double cx, double cy)
{
	int i;
	int cnt = 0;
	double dx, dy;
		
	if (isInside(cx + gap, cy + gap)) return realArea;
	
	for (i=0; i<MAX; i++)
	{
		dx = cx + gap * ((double)rand() / (double)32768);
		if (dx < cx + fly || dx > cx + gap - fly) continue;

		dy = cy + gap * ((double)rand() / (double)32768);
		if (dy < cy + fly || dy > cy + gap - fly) continue;

		cnt += isInside(dx, dy);
	}

	return ((double)cnt / (double)MAX) * gap * gap;
}



void doWork(void)
{
	int i, c;
	double cx, cy, ans;
	
	area = 0;
	fscanf(in, "%lf", &fly);
	fscanf(in, "%lf %lf", &radius, &thickness);
	fscanf(in, "%lf %lf", &line, &gap);
	
	realRadius = radius - thickness - fly;
	rectSide = max((gap - fly * 2.0), 0.0);
	realArea = rectSide * rectSide;

	totalArea = (PI * radius * radius) / 4.00;
	MIN_SIDE = sqrt(PI * realRadius * realRadius) * (long double)0.0000002;
	area = totalArea;
	
	cout << "Real Radius: " << realRadius << endl;
	cout << "MIN_SIDE: " << MIN_SIDE << endl;
//	system("pause");
	
	double inc = gap + line * 2.0;
	for (cx = line; cx < realRadius; cx += inc)
	{
		int best = NUM_RECT;
		int left = 0, right = NUM_RECT, mid;
		
		while (left <= right)
		{
			mid = (left + right) / 2;
			
			cy = line + mid * inc;
			if (isInside(cx + gap, cy + gap)) left = mid + 1;
			else
			{
				best = min(best, mid);
				right = mid - 1;
			}
		}
		area -= realArea * best;
		for (cy = line + best * inc; cy < realRadius; cy += inc) //area -= findArea(cx, cy);
			area -= recArea(cx + fly, cy + fly, rectSide);
	}
//	system("pause");
	
	ans = area / totalArea;
	ans = max(ans, 0.0);

	char tmp[20];
	sprintf(tmp, "%.7lf", ans);
	for (i=0; i<(int)strlen(tmp)-1; i++) fprintf(out, "%c", tmp[i]);
	fprintf(out, "\n");
	cout << "Test ready..." << endl;
	return;
}


int main(void)
{
	int tests, i;
	
	in = fopen("FlySwatter.in", "rt");
	out = fopen("FlySwatter.out", "wt");
	
	fscanf(in, "%d", &tests);
	for (i=0; i<tests; i++)
	{
		fprintf(out, "Case #%d: ", i+1);
		doWork();
	}
	
	return 0;
}
