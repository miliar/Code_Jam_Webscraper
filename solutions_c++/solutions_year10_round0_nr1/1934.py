#include <cstdio>
#include <iostream>
using namespace std;

int i, j, k, n, m;
bool ok;

int main()
{
	freopen("a.in", "r", stdin);
   	freopen("a.out", "w", stdout);
   	scanf("%d", &m);
   	for (i = 1; i <= m; i++)
   	{
   		scanf("%d%d", &n, &k);
   		ok = 1;
   		for (j = 0; j < n; j++)
   			ok &= ((k & (1 << j)) > 0);
   		if (ok)
	   		printf("Case #%d: ON\n", i);
	   	else
			printf("Case #%d: OFF\n", i);
   	}
}
