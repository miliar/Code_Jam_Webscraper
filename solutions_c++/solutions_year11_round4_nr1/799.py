#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <ctime>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <math.h>
#include <queue>
#include <memory.h>
#include <iostream>
#include <stack>
//#include <complex>
 
using namespace std;
 
void ASS(bool b)
{
    if (!b)
    {
        ++*(int*)0;
    }
}
 
#define FOR(i, x) for (int i = 0; i < (int)(x); i++)
#define CL(x) memset(x, 0, sizeof(x))
 
#pragma comment(linker, "/STACK:106777216")
 
typedef vector<int> vi;
typedef long long LL;

struct node
{
	int d, w;
};

bool operator < (node a, node b)
{
	return a.w < b.w;
}

void Solve()
{
	int X, S, R;
	cin >> X;
	cin >> S >> R;
	double t;
	cin >> t;
	int n;
	cin >> n;
	vector<node> a;
	FOR(i, n)
	{
		int b, e, w;
		cin >> b >> e >> w;
		node nd;
		nd.d = e - b;
		nd.w = w;
		a.push_back(nd);
		X -= nd.d;
	}
	{
		node nd;
		nd.d = X;
		nd.w = 0;
		a.push_back(nd);
	}
	sort(a.begin(), a.end());
	double Time = 0;
	FOR(i, a.size())
	{
		double t0 = a[i].d / (double)(R + a[i].w);
		if (t0 < t)
		{
			t -= t0;
			Time += t0;
		}
		else
		{
			Time += t;
			Time += (a[i].d - t * (R + a[i].w)) / (double)(S + a[i].w);
			t = 0;
		}
	}
	printf("%0.9lf\n", Time);
}

int main()
{
#ifndef _DEBUG_4444
	freopen("c:\\GCJ\\in.txt", "r", stdin);
	freopen("c:\\GCJ\\out.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	FOR(i, t)
	{
		printf("Case #%d: ", i + 1);
		Solve();
	}
	return 0;
}