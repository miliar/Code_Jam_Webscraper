#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t, n, k;
	scanf("%d", &t);
	int i;
	for(i=1; i<=t; ++i)
	{
		scanf("%d %d", &n, &k);
		int tmp = (1<<n) - 1;
		k &= tmp;
		printf("Case #%d: %s\n", i, (k==tmp) ? "ON" : "OFF");
	}
	return 0;
}

