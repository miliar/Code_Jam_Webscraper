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

bool empty[110];
int l[110];
int ln;

int getAns(int p, int q)
{
	if (p == q)
		return 0;
	else
	{
		int i = 0;
		int count = -1;
		int res = 10000000;
		for (i = 0; i < ln; i++)
		{
			if (l[i] >= p && l[i] <= q)
			{
				count = q - p + getAns(p, l[i] - 1) + getAns(l[i] + 1, q);
				res = count > res ? res : count;
			}
		}
		if (count == -1)
			return 0;
		else return res;
	}
}

int main()
{
	freopen("3.in", "r", stdin);
	freopen("3.out", "w", stdout);

	int t, T, i, j, k;
	int P, Q;

	scanf ("%d", &T);
	for (t = 1; t <= T; t++)
	{
		scanf ("%d%d", &P, &Q);
		//memset(empty, 0, sizeof(empty));
		//empty[0] = empty[P + 1] = true;
		for (i = 0; i < Q; i++)
			scanf ("%d", &l[i]);
		ln = Q;
		int res = getAns(1, P);
		printf ("Case #%d: %d\n", t, res);
	}

	return 0;
}