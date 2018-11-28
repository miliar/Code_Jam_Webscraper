#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cstdio>
#include <climits>
#include <queue>
using namespace std;

char str[503];
bool st[503];
char goo[] = "welcome to code jam";
const int len = 19;
int n, sum;

void dfs(int k, int in)
{
	if (in == 19)
	{
		sum++;
		if (sum > 9999)
			sum %= 10000;
		return;
	}
	for (int i=k; str[i] != 0; i++)
	{
		if (!st[i] && str[i] == goo[in])
		{
			st[i] = true;
			dfs(i+1, in+1);
			st[i] = false;
		}
	}

}
int main()
{
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	scanf("%d", &n);
	getchar();
	
	for (int t=1; t <=n; t++)
	{
		gets(str);
		memset(st, 0, sizeof(st));
		sum = 0;
		dfs(0, 0);
		printf("Case #%d: %04d\n", t, sum);

	}




	return 0;
}
