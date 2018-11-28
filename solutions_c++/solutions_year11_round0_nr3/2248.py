#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;
int main()
{
	int t;
	scanf("%d", &t);
	for (int ca=0; ca<t; ca++) {
		int n;
		scanf("%d", &n);
		
		static int a[10000000];
		for (int i=0; i<n; i++)
			scanf("%d", a+i);
		
		sort(a, a+n);
		long long sum = 0, xo = 0;
		for (int i=1; i<n; i++)
		{
			sum += a[i];
			xo ^= a[i];
		}
		printf("Case #%d: ", ca+1);
		if (a[0] == xo)
			printf("%d\n", sum);
		else
			printf("NO\n");
	}
	
}
