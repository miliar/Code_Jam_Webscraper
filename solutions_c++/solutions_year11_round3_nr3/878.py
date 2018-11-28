#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

int n, l, h;
int a[100 + 5];
int ans;

void init()
{
	scanf("%d%d%d", &n, &l, &h);
	for (int i = 0; i < n; i++)
		scanf("%d", &a[i]);
}

void process()
{
	bool flag;
	ans = -1;
	for (int i = l; i <= h; i++)
	{
		flag = true;
		for (int j = 0; j < n; j++)
			if (!(i % a[j] == 0 || a[j] % i == 0))
			{
				flag = false;
				break;
			}
		if (flag)
		{
			ans = i;
			break;
		}
	}
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		init();
		process();
		printf("Case #%d: ", t);
		if (ans == -1)
			printf("NO\n");
		else
			printf("%d\n", ans);
	}
	return 0;
}