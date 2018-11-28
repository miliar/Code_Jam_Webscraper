#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;

int n;
int s[2000];

int solve()
{
	int xorr = 0, minn = 2000000000, w, sum = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &w);
		minn = min(minn, w);
		xorr ^= w;
		sum += w;
	}
	if (xorr)puts("NO");
	else printf("%d\n", sum - minn);
}

int main()
{
	int tc;
	scanf("%d", &tc);
	for (int i = 1; i <= tc; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}

