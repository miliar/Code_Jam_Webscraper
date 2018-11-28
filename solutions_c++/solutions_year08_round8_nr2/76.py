#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <set>
#include <algorithm>
#pragma warning (disable: 4996)

using namespace std;

vector<string> cold;
struct of { int col; int a; int b; };

int check(int x, of * o, int N)
{
	int d[10000] = { 0 };
	set<int> cols;
	int c = 0;
	for (int i = 0; i < N; i++)
	{
		if (x & (1 << i))
		{
			cols.insert(o[i].col);
			c++;
		}
	}
	if (cols.size() > 3)
		return 9999;
	for (int i = 0; i < N; i++)
	{
		if (x & (1 << i))
			fill<int*, int>(d + o[i].a, d + o[i].b + 1, 1);
	}
	return find<int*, int>(d, d + 10000, 0) == d + 10000 ? c : 9999;
}

int main()
{
	int ncase;
	scanf("%d", & ncase);
	for (int cas = 1; cas <= ncase; cas++)
	{
		int N;
		scanf("%d", & N);
		of o[400];
		cold.clear();
		for (int i = 0; i < N; i++)
		{
			char buf[256];
			scanf("%s %d %d", buf, & o[i].a, & o[i].b);
			for (unsigned j = 0; j < cold.size(); j++)
			{
				if (buf == cold[j])
				{o[i].col = j; goto found;
				}
			}
			o[i].col = cold.size();
			cold.push_back(string(buf));
found:
			o[i].a--;
			o[i].b--;
		}

		int b = 9999;
		for (unsigned m = 0; m < (1u << N); ++m)
			b = min(b, check(m, o, N));

		if (b < 9999)
			printf("Case #%d: %d\n", cas, b);
		else
			printf("Case #%d: IMPOSSIBLE\n", cas);
	}

	return 0;
}
