#pragma comment (linker, "/STACK:64000000")
#include <cstdio>
#include <cstring>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
#include <cctype>
#include <bitset>
#include <sstream>
#include <set>
#include <map>

using namespace std;
template <class T> T sqr(T a) { return a * a; }

int dp[10010];
int d[10010];
int l[10010];
int n, len;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	for (int testCount = 0; testCount < testNum; testCount++)
	{
		cin >> n;
		for (int i = 0; i < n; i++)
			cin >> d[i] >> l[i];
		cin >> len;
		memset(dp, -1, sizeof(dp));
		int ok = 0;
		dp[0] = d[0];
		for (int i = 0; i < n; i++)
			if (dp[i] != -1)
			{
				for (int j = i + 1; j < n; j++)
					if (d[j] - d[i] <= dp[i])
					{
						int nv = min(l[j], d[j] - d[i]);
						dp[j] = max(dp[j], nv);
					}
				if (len - d[i] <= dp[i])
					ok = 1;
			}
		if (ok)
			printf("Case #%d: YES\n", testCount + 1);
		else
			printf("Case #%d: NO\n", testCount + 1);
	}
	return 0;
}