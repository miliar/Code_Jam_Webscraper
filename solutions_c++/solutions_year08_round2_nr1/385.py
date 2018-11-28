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

lint X[101], Y[101];

bool Solve(int test)
{
	int n, A, B, C, D, x0, y0, M;
	scanf("%d %d %d %d %d %d %d %d", &n, &A, &B, &C, &D, &x0, &y0, &M);
	X[0] = x0;
	Y[0] = y0;
	for(int i = 1; i < n; ++i)
	{
		X[i] = (X[i - 1] * A + B) % M;
		Y[i] = (Y[i - 1] * C + D) % M;
	}
	int ans = 0;
	for(int i = 0; i < n; ++i)
		for(int j = i + 1; j < n; ++j)
			for(int k = j + 1; k < n; ++k)
			{
				if(((X[i] + X[j] + X[k]) % 3 == 0) && ((Y[i] + Y[j] + Y[k]) % 3 == 0))
					ans++;
			}
	printf("Case #%d: %d\n", test, ans);
	return true;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t = 0;
	scanf("%d", &t);
	for(int i = 0; i < t; ++i)
		Solve(i + 1);
	//while(Solve(++t));
	return 0;
}