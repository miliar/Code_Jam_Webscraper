#include <vector>
#include <cstring>
#include <map>
#include <string>
#include <iostream>
#include <functional>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int cases;
	scanf("%d", &cases);
	for (int t = 1; t <= cases; t++)
	{
		int N, K;
		scanf("%d%d", &N, &K);
		long long n, k;
		n = N; k = K;
		n = ((long long)(1 << n)) -1;
		if ((k & n) == n)
		{
			printf("Case #%d: ON\n", t);
		}
		else
		{
			printf("Case #%d: OFF\n", t);
		}
	}
	return 0;
}