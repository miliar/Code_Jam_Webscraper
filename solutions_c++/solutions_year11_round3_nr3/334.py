#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

using namespace std;

const int MAX = 20000;
long long a[MAX];

int nodd(int a, int b)
{
	if(b == 0)
		return a;
	return nodd(b, a % b);
}

long long findans(long long nod, int l, int h, int n)
{
	int i, j;
	bool ok = true;
	for(i = l; i < h + 1; i++)
	{
		ok = true;
		for(j = 0; j < n; j++)
			if((i % a[j] != 0) && (a[j] % i != 0))
			{
				ok = false;
				break;
			}
		if(ok)
			return i;
	}
	return -1;
}

int main()
{
	int t, k, i, l, h, b, n;
	long long nod;
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	scanf("%d", &t);
	for(k = 0; k < t; k++)
	{
		printf("Case #%d: ", k + 1);
		scanf("%d %d %d", &n, &l, &h);
		for(i = 0; i < n; i++)
			scanf("%d", a + i);
		nod = a[1];
		for(i = 1; i < n; i++)
			if(nod > a[i])
				nod = nodd(a[i], nod % a[i]);
			else
				nod = nodd(nod, a[i]);
		if(findans(nod, l, h, n) < 0)
			printf("NO\n");
		else
			printf("%I64d\n", findans(nod, l, h, n));
	}
    return 0;
}
