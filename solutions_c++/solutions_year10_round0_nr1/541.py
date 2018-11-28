// GCJ 2010 Qual 
// 1. Snapper Chain

// May 8, 2010
// wookayin

#include <stdio.h>
#include <string>
#include <algorithm>

using namespace std;

int n, k;

bool go(int n, int k)
{
	return (((1 << n) - 1) & k) == ((1<<n) - 1);
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T, tt;
	scanf("%d", &T);
	for(tt=1; tt<=T; ++tt)
	{
		scanf("%d %d", &n, &k);
		printf("Case #%d: %s\n", tt, go(n, k) ? "ON" : "OFF");
	}
	return 0;
}