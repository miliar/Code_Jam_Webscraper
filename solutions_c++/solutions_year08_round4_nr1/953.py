//#pragma comment(linker, "/STACK:10000000")
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <iostream>
#include <stack>
#include <queue>
#include <cmath>
using namespace std;
typedef long long lint;

int G[33];
int C[33];
int M;

int Calc(int p, int mask)
{
	if(p > M / 2)
		return G[p];
	int f = G[p];
	if(C[p] && (mask & (1 << p)))
		f = 1 - f;
	if(f)
		return Calc(2 * p, mask) & Calc(2 * p + 1, mask);
	return Calc(2 * p, mask) | Calc(2 * p + 1, mask);
}

int Bits(int x)
{
	int ret = 0;
	while(x)
	{
		if(x & 1)
			ret++;
		x >>= 1;
	}
	return ret;
}

bool Solve(int test)
{
	printf("Case #%d: ", test);
	int v;
	scanf("%d %d", &M, &v);
	for(int i = 1; i <= M / 2; ++i)
	{
		scanf("%d %d", G + i, C + i);
	}
	for(int i = M / 2 + 1; i <= M; ++i)
		scanf("%d", G + i);
	int t = M / 2;
	int ans = 100;
	for(int i = 0; i < 1 << t + 1; ++i)
	{
		if(Calc(1, i) == v)
			ans = min(ans, Bits(i));
	}
	if(ans == 100)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n", ans);
	return true;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("inputA.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t = 0;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i)
		Solve(i);
	//while(Solve(++t));
	return 0;
}