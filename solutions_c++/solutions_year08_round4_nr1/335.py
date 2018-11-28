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

struct cell_s
{
	int type; // 0 - or, 1 - and
	int changable;
} cell[10001];

int N;
int target;
int ans;

int mem[10001][2];

int go(int pl, int target)
{
	int lch = pl * 2 + 1;
	int rch = pl * 2 + 2;
	if (lch >= N)
		return (target == cell[pl].type) ? 0 : 0x3F3F3F3F;

	if (mem[pl][target] != 0x3F3F3F3F)
		return mem[pl][target];

	int &res = mem[pl][target];
	int p, q;
	int k, r;
	for (k = 0;k < 2;k++)
	{
		if (!cell[pl].changable && k != cell[pl].type)
			continue;
		for (p = 0;p < 2;p++)
		{
			for (q = 0;q < 2;q++)
			{
				if (!k)
					r = p || q;
				else
					r = p && q;
				if (r != target)
					continue;
				int ap = go(lch, p);
				int aq = go(rch, q);
				if (res > ap + aq + (cell[pl].type != k))
					res = ap + aq + (cell[pl].type != k);
			}
		}
	}
	return res;
}

int main()
{
	int ti, t;
	scanf("%d", &t);
	for (ti = 1;ti <= t;ti++)
	{
		memset(mem, 0x3F, sizeof(mem));
		scanf("%d", &N);
		scanf("%d", &target);
		
		int i;
		for (i = 0;i < N / 2;i++)
			scanf("%d %d", &cell[i].type, &cell[i].changable);
		for (;i < N;i++)
		{
			scanf("%d", &cell[i].type);
			cell[i].changable = 0;
		}

		ans = go(0, target);
		printf("Case #%d: ", ti);
		if (ans == 0x3F3F3F3F)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", ans);
	}
	return 0;
}