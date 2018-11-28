//============================================================================
// Name        : A.cpp
// Author      : xbit
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <vector>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>

using namespace std;

#define SZ(a) ((int)(a).size())
#define pii pair<int,int>
#define mp make_pair
template<class A, class B> A convert(B x) {stringstream s; s << x; A r; s >> r; return r;}

int g[10002], c[10002], l[10002];
int mem[10002][2];
int M, V;

int mmin(int a, int b, int c)
{
if (a != -1 && (b == -1 || a+c  < b))
	return a+c;
else
	return b;
}

int calc(int node, int num)
{
	if (mem[node][num] != -2)
		return mem[node][num];

	if (node > (M-1)/2)
	{
		if (l[node] == num)
			return 0;
		else
			return -1;
	}

		int res = -1;

		if ((g[node] == 1 || c[node] == 1)&& num == 1)
		{
			int t;
			int t1 = calc(node*2, 1);
			int t2 = calc(node*2+1, 1);
			if (t1 == -1 || t2 == -1) t = -1; else t = t1+t2;
			res = mmin(t, res, ( (c[node] == 1 && g[node] != 1) ? 1 : 0));
		} else
			if ((g[node] == 1 || c[node] == 1)&& num == 0)
			{
				int t;
				int t1 = calc(node*2, 0); int t2 = calc(node*2+1, 1);
				if (t1 == -1 ) t = -1; else t = t1;
				res = mmin(t, res, ( (c[node] == 1 && g[node] != 1) ? 1 : 0));

				t1 = calc(node*2, 1); t2 = calc(node*2+1, 0);
				if (t2 == -1) t = -1; else t = t2;
				res = mmin(t, res, ( (c[node] == 1 && g[node] != 1) ? 1 : 0));
			}

		if ((g[node] == 0 || c[node] == 1)&& num == 0)
		{
			int t;
			int t1 = calc(node*2, 0);
			int t2 = calc(node*2+1, 0);
			if (t1 == -1 || t2 == -1) t = -1; else t = t1+t2;
			res = mmin(t, res, ( (c[node] == 1 && g[node] != 0) ? 1 : 0));

		} else
			if ((g[node] == 0 || c[node] == 1) && num == 1)
			{
				int t;
				int t1 = calc(node*2, 0);
				int t2 = calc(node*2+1, 1);
				if (t2 == -1) t = -1; else t = t2;
				res = mmin(t, res, ( (c[node] == 1 && g[node] != 0) ? 1 : 0));

				t1 = calc(node*2, 1); t2 = calc(node*2+1, 0);
				if (t1 == -1) t = -1; else t = t1;
				res = mmin(t, res, ( (c[node] == 1 && g[node] != 0) ? 1 : 0));
			}
	//cout << "D: "<< node << " " << num << ": " << res << endl;
	mem[node][num] = res;
	return res;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testCnt;
	cin >> testCnt;
	for (int testNum = 0; testNum < testCnt; ++testNum)
	{

		cin >> M >> V;
		memset(g, 0, sizeof g);
		memset(c, 0, sizeof c);
		memset(l, 0, sizeof l);
		for (int i = 0; i <=M; ++i)
			for (int j = 0; j <= 1; ++j)
			{
				mem[i][j] = -2;
			}
		for (int i = 1; i <= (M-1)/2; ++i)
		{
			cin >> g[i] >> c[i];
		}
		for (int i = 1; i <= (M+1)/2; ++i)
		{
			cin >> l[i+(M-1)/2];
		}

		int res = calc(1, V);

		cout << "Case #" << testNum+1 << ": ";
		if (res == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << res << endl;
	}
	return 0;
}
