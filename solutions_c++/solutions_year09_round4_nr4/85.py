#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<numeric>
#include<math.h>
#include<set>
#include<map>
#include<fstream>
#define epsilon 0.000000001
#define cosinusa(a, b, c) ((a * a + b * b - c * c) / (2.0 * a * b));
#define infi 1000000000
using namespace std;

struct circle
{
	double cx, cy, r;
};
double dist(double x1, double y1, double x2, double y2)
{
	return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
}
int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d: ", testCounter + 1);
		int n;
		cin >> n;
		if(n > 3)
		{
			printf("0.000\n");
			continue;
		}
		double maxm = 0.0;
		vector<circle> v(n);
		for(int i = 0; i < n; i++)
		{
			cin >> v[i].cx >> v[i].cy >> v[i].r;
			maxm = max(maxm, v[i].r);
		}
		if(n == 3)
		{
			double minm = 1e9;
			for(int i = 0; i < 3; i++)
				for(int j = i + 1; j < 3; j++)
					minm = min(minm, v[i].r + v[j].r + dist(v[i].cx, v[i].cy, v[j].cx, v[j].cy));
			maxm = max(maxm, 0.5 * minm);
			printf("%.9lf\n", maxm); 
		}
		else
			printf("%.9lf\n", maxm); 
	}
	return 0;
}
