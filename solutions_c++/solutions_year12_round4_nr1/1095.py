#pragma comment(linker, "/STACK:100000000")
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;

#define eps 1e-8

int T, D, N, a[10005], i, j, k, t, L[10005], b[10005];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%d", &T);
	for(t = 1; t <= T; t++)
	{
		scanf("%d", &N);
		for(i = 1; i <= N; i++)
			scanf("%d %d", &a[i], &L[i]);
		scanf("%d", &D);
		printf("Case #%d: ", t);

//		if(L[1] < a[1])
//		{
//			puts("NO");
//			continue;
//		}

		memset(b, 0, sizeof(b));
		b[1] = a[1];
		for(i = 1; i <= N; i++)
			for(j = i + 1; j <= N && a[i] + b[i] >= a[j]; j++)
			{
				b[j] = max(b[j], min(L[j], a[j] - a[i]));
			}

		for(i = 1; i <= N; i++)
			if(b[i] + a[i] >= D)
			{
				puts("YES");
				break;
			}
		if(i > N)
			puts("NO");
	}
	return 0;
}