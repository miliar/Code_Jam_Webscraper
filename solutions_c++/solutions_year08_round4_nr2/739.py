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

bool Solve(int test)
{
	printf("Case #%d: ", test);
	int N, M, A;
	scanf("%d %d %d", &N, &M, &A);
	for(int a = 1; a <= N; ++a)
		for(int d = 1; d <= M; ++d)
		{
			if(a * d < A)
				continue;
			int q = a * d - A;
			if(!q)
			{
				printf("0 0 %d %d %d %d\n", a, 0, 0, d);
				return true;
			}
			for(int c = 1; c <= min(q, N); ++c)
			{
				if(q % c)
					continue;
				int b = q / c;
				if(b > M)
					continue;
				printf("0 0 %d %d %d %d\n", a, b, c, d);
				return true;
			}
		}
	printf("IMPOSSIBLE\n");
	return true;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("inputB.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t = 0;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i)
		Solve(i);
	//while(Solve(++t));
	return 0;
}