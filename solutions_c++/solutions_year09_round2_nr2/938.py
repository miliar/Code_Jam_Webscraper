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

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t, T, n, i, k;
	scanf ("%d", &T);
	char str[50];
	int a[50];
	int init[50];
	for (t = 1; t <= T; t++)
	{
		scanf ("%s", str);
		k = 0;
		for (i = 0; str[i] != 0; i++)
		{
			a[i] = str[i] - '0';
			if (a[i])
				init[k++] = a[i];
		}
		sort(init, init + k);
		n = i;
		if (next_permutation (a, a + n))
		{
			for (i = 0; i < n; i++)
			{
				str[i] = a[i] + '0';
			}
		}
		else
		{
			if (a[0] == 0)
			{
				for (i = 1; i < n; i++)
				{
					if (a[i])
						break;
				}
				swap(a[0], a[i]);
			}
			
			for (i = n - 1; i > 0; i--)
				str[i + 1] = a[i] + '0';
			str[0] = a[0] + '0';
			str[1] = '0';
			str[n + 1] = 0;
		}
		printf ("Case #%d: %s\n", t, str);
	}
	return 0;
}