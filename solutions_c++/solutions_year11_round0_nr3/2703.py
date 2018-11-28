#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;

const int MX=10000000;
const int N=1010;
__int64 mn, sum, xor;
int a[N], n;

int main()
{
	//freopen("C-large.in", "r", stdin);
	//freopen("C-large.out", "w", stdout);
	int i, j, k, cas, cas1;
	scanf("%d", &cas);
	for(cas1=1; cas1<=cas; cas1++)
	{
		scanf("%d", &n);
		scanf("%d%d", &a[1], &a[2]);
		xor = a[1] ^ a[2];
		sum = a[1] + a[2];
		if(a[1]>a[2])
			mn = a[2];
		else
			mn = a[1];
		for(i=3; i<=n; i++)
		{
			scanf("%d", &a[i]);
			if(a[i]<mn)
				mn = a[i];
			xor = xor ^ a[i];
			sum += a[i];
		}
		printf("Case #%d: ", cas1);
		if(xor!=0)
		{
			printf("NO\n");
			continue;
		}
		printf("%I64d\n", sum - mn);
	}
	return 0;
}