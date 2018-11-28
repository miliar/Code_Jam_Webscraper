#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <functional>
using namespace std;

#pragma comment(linker,"/STACK:100000000")

int gcd(int x, int y)
{
	return y==0 ? x : gcd(y, x%y);
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input2.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T, i;
	scanf("%d", &T);
	for (i=0; i<T; ++i)
	{
		long long n;
		int pd, pg;
		scanf("%I64d%d%d", &n, &pd, &pg);
		int g=gcd(pd, 100);
		int a=pd/g;
		int b=100/g;
		printf("Case #%d: ", i+1);
		if (b>n || (pg==100 && pd<100) || (pg==0 && pd>0))
			printf("Broken\n");
		else
			printf("Possible\n");
	}
	return 0;
}