//============================================================================
// Name        : B.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

const int maxn = 200;
int t[maxn];

int main() {
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int casenum=1; casenum <= T; ++casenum)
	{
		printf("Case #%d: ", casenum);
		int n, s, p;
		scanf("%d %d %d", &n, &s, &p);
		for (int i = 0; i < n; ++i)
			scanf("%d", &t[i]);
		sort(t, t + n);
		int ans = 0;
		for (int i = n-1; i >= 0; --i)
		{
			if (max(p, 3 * p - 2) <= t[i])
				ans++;
			else if (s != 0 && max(p, 3 * p - 4) <= t[i])
			{
				s--;
				ans++;
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}
