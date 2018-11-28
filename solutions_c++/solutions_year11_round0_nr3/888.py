#include <iostream>
#include <string>
#include <string.h>
#include <cstring>
#include <algorithm>
#include <queue>
#pragma comment (linker, "/STACK:256000000")

using namespace std;

int n;
int c[1100];

void solve(int test)
{
	scanf("%d", &n);
	for (int i = 1; i <= n; i ++)
		scanf("%d", &c[i]);
	int res = 0;
	for (int i = 1; i <= n; i ++)
		res ^= c[i];
	if (res != 0)
	{
		printf("Case #%d: NO\n", test);
		return ;
	}

	int s = 0;
	sort(c + 1, c + n + 1);
	for (int i = 2; i <= n; i ++)
		s += c[i];
	printf("Case #%d: %d\n", test, s);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i ++)
		solve(i);
	return 0;
}