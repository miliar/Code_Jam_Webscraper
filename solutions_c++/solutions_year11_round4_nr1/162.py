#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

struct sWalkWay
{
	int b, e, w;
};

sWalkWay ww[1024];

bool cmp1(const sWalkWay &a, const sWalkWay &b)
{
	return a.b < b.b;
}

bool cmp2(const sWalkWay &a, const sWalkWay &b)
{
	return a.w < b.w;
}

double work()
{
	double X, S, R, T;
	int N;
	cin >> X >> S >> R >> T >> N;
	double t = T;
	for (int i = 0; i < N; i ++)
		cin >> ww[i].b >> ww[i].e >> ww[i].w;
	sort(ww, ww + N, cmp1);
	int walk = ww[0].b;
	for (int i = 1; i < N; i ++)
		walk += ww[i].b - ww[i-1].e;
	walk += X - ww[N-1].e;

	double ans = 0.0;
	sort(ww, ww + N, cmp2);
	
	
	double vl = t * R;
	if (vl >= walk)
	{
		double vvt = double(walk) / R;
		ans += vvt;   t -= vvt;
	} else {
		double vvt = (double(walk) - vl) / S;
		ans += t + vvt;   t = 0.0;
	}


	for (int i = 0; i < N; i ++)
	{
		double vl = t * (R + ww[i].w);
		if (vl >= ww[i].e - ww[i].b)
		{
			double vvt = double(ww[i].e - ww[i].b) / (R + ww[i].w);
			t -= vvt;   ans += vvt;
		} else {
			double vvt = double(ww[i].e - ww[i].b - vl) / (S + ww[i].w);
			ans += t + vvt;   t = 0.0;   
		}
	}
	
	return ans;
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int k = 1; k <= T; k ++)
		printf("Case #%d: %.7f\n", k, work());
	return 0;
}