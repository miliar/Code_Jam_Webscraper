#include <iostream>
#include <cstdio>

#include <cstring>
#include <string>

#include <vector>
#include <map>
#include <set>

#include <algorithm>
#include <cmath>

using namespace std;


int a[100500];


int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testCount;
	scanf("%d", &testCount);
	for(int testNumber = 1; testNumber <= testCount; testNumber++)
	{
		printf("Case #%d: ", testNumber);
		int n;
		scanf("%d", &n);
		int m = 1500500;
		int s = 0;
		int xor = 0;
		for(int i = 0; i < n; i++)
		{
			scanf("%d", &a[i]);
			xor ^= a[i];
			s += a[i];
			m = min(m, a[i]);
		}
		if(xor != 0)
		{
			printf("NO\n");
			continue;
		}
		int res = s - m;
		printf("%d\n", res);
	}
	return 0;
}