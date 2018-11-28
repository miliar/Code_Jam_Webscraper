#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

double L[1024], W[1024];

int N, idx[1024];

bool cmp0(int a, int b)
{
	return W[a] < W[b];
}

bool cmp1(int a, int b)
{
	return W[a] > W[b];
}

double solve(double walk, double run, double t)
{
	double ret = 0;

	for (int i = 0; i < N; i++)
	{
		double len = L[idx[i]];
		if (t > 0)
		{
			if (t > len / (run + W[idx[i]]))
			{
				ret += len / (run + W[idx[i]]);
				t -= len / (run + W[idx[i]]);
			}
			else
			{
				ret += t; 
				ret += (len - t * (run + W[idx[i]])) / (walk + W[idx[i]]);
				t = 0;
			}
		}
		else
		{
			ret += len / (walk + W[idx[i]]);
		}
	}

	return ret;
}

int main()
{
	freopen("f:\\A-small-attempt0.in", "r", stdin);
	freopen("f:\\A-small-attempt0.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t_case = 1; t_case <= T; t_case++)
	{
		double X, S, R, t;
		scanf("%lf %lf %lf %lf %d", &X, &S, &R, &t, &N);
		for (int i = 0; i < N; i++)
		{
			int x, y;
			scanf("%d %d %lf", &x, &y, &W[i]);
			L[i] = y - x;
			X -= L[i];
		}
		L[N] = X; W[N] = 0; N++;

		for (int i = 0; i < N; i++) idx[i] = i;
		sort(idx, idx + N, cmp0);
		double res = solve(S, R, t);
		sort(idx, idx + N, cmp1);
		res = min(res, solve(S, R, t));

		printf("Case #%d: %.10f\n", t_case, res);
	}
	return 0;
}
