#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <fstream>
using namespace std;

#define all(o) (o).begin(), (o).end()
#define allr(o) (o).rbegin(), (o).rend()
#define INF 2147483647
typedef long long ll;
typedef pair<int, int> ii;
template <class T> int size(T x) { return x.size(); }

int n;
ii* ropes;
int D;

map<ii, bool> mem;

bool canreach(int r, int l)
{
	if (ropes[r].first + l >= D) return true;

	ii cur(r, l);
	if (mem.find(cur) != mem.end())
		return mem[cur];

	for (int i = r + 1; i < n; i++)
	{
		if (ropes[i].first > ropes[r].first + l) break;
		if (canreach(i, min(ropes[i].second, ropes[i].first - ropes[r].first)))
			return mem[cur] = true;
	}

	return mem[cur] = false;
}

int main()
{
	int ts;
	scanf("%d\n", &ts);

	for (int t = 0; t < ts; t++)
	{
		mem.clear();
		scanf("%d\n", &n);

		ropes = new ii[n];
		for (int i = 0; i < n; i++)
		{
			scanf("%d %d\n", &(ropes[i].first), &(ropes[i].second));
		}

		scanf("%d\n", &D);

		if (canreach(0, ropes[0].first))
		{
			printf("Case #%d: YES\n", t + 1);
		}
		else
		{
			printf("Case #%d: NO\n", t + 1);
		}

		delete[] ropes;
	}

	return 0;
}