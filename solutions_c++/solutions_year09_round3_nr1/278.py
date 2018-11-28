#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <ctime>
#include <iostream>

 
using namespace std;

__int64 getAns(int val[], int n)
{
	int max = -1;
	int i;
	for (i = 0; i < n; i++)
	{
		max = max > val[i] ? max : val[i];
	}
	__int64 res = 0;
	max++;
	for (i = 0; i < n; i++)
	{
		res = res * max + val[i];
	}
	return res;
}

int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);

	int T, t, i, j, n, res;
	char num[100];
	int ch[256];
	int val[100];

	scanf ("%d", &T);
	for (t = 1; t <= T; t++)
	{
		for (i = 0; i < 256; i++)
			ch[i] = -1;
		scanf ("%s", num);
		bool isCh = true;
		if (num[0] >= '0' && num[0] <= '9')
			isCh = false;
		int count = 0;
		val[0] = 1;
		ch[num[0]] = 1;
		for (i = 0; num[i] != 0; i++)
		{
			if (ch[num[i]] == -1)
			{
				val[i] = count;
				ch[num[i]] = count;
				count++;
				if (count == 1)
					count++;
			}
			else
				val[i] = ch[num[i]];
		}

		printf ("Case #%d: %I64d\n", t, getAns(val, strlen(num)));
	}

	return 0;
}