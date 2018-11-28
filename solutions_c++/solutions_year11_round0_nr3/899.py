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

int a[1500];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input2.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t, tt;
	scanf("%d", &t);
	for (tt=0; tt<t; ++tt)
	{
		int n, i;
		scanf("%d", &n);
		int s=0, x=0;
		for (i=0; i<n; ++i)
		{
			scanf("%d", &a[i]);
			x^=a[i];
			s+=a[i];
		}
		sort(a, a+n);
		printf("Case #%d: ", tt+1);
		if (x!=0)
		{
			printf("NO\n");
		}
		else
		{
			printf("%d\n", s-a[0]);
		}
	}
	return 0;
}