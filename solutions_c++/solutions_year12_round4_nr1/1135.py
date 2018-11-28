//============================================================================
// Name        : A.cpp
// Author      : kangaroo
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

const int maxn = 20000;

int d[maxn], l[maxn], best[maxn];

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int casenum=1; casenum <= T; ++casenum)
	{
		printf("Case #%d: ", casenum);
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d %d", &d[i], &l[i]);
		memset(best, 0, sizeof(best));
		best[0] = d[0];
		for (int i = 0; i < n; ++i)
			if (best[i])
			{
				for (int j = i + 1; j < n; ++j)
				{
					if (best[i] + d[i] < d[j]) break;
					best[j] = max(best[j], min(l[j], d[j] - d[i]));
				}
			}
		int k;
		scanf("%d", &k);
		bool ok = false;
		for (int i = 0; i < n; ++i)
			if (best[i] && d[i] + best[i] >= k){
			printf("YES\n");
			ok = true; break;
			}
		if (!ok) printf("NO\n");
	}
	return 0;
}
