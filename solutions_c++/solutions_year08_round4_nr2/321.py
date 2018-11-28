#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <cctype>
using namespace std;

int x, y, a;
int p, q, r, s;

int solve()
{
	for (p = 0;p <= x;p++)
	{
		for (q = 0;q <= y;q++)
		{
			for (r = 0;r <= x;r++)
			{
				for (s = 0;s <= y;s++)
				{
					if (p * s - q * r == a)
					{
						printf("%d %d %d %d %d %d\n", 0, 0, p, q, r, s);
						return true;
					}
				}
			}
		}
	}
	return false;
}

int main()
{
	int ti, t;
	scanf("%d", &t);
	for (ti = 1;ti <= t;ti++)
	{
		scanf("%d %d %d", &x, &y, &a);
		printf("Case #%d: ", ti);
		if (!solve())
			printf("IMPOSSIBLE\n");
	}
	return 0;
}