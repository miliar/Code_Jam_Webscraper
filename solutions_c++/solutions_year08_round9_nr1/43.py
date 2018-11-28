#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <ctime>
using namespace std;

#define for_each(it, v) for (typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)

const int MAX_N = 5000;
const int RANGE = 10000;

int n;
int a[MAX_N];
int b[MAX_N];
int c[MAX_N];

int tree[(RANGE + 1) * 2]; //[l, r]  [0, n - 1]

int getIndex(int l, int r)
{
	return (l + r) | (l != r);
}
void unmarkTree(int l, int r)
{
	if (l == r)
		return;
	int m = (l + r) / 2;
	tree[getIndex(l, m)] += tree[getIndex(l, r)];
	tree[getIndex(m + 1, r)] += tree[getIndex(l, r)];
	tree[getIndex(l, r)] = 0;
}
void modifyTree(int l, int r, int from, int to, int delta)
{
	if (from <= l && r <= to)
	{
		tree[getIndex(l, r)] += delta;
		return;
	}
	unmarkTree(l, r);
	int m = (l + r) / 2;
	if (from <= m)
		modifyTree(l, m, from, to, delta);
	if (m + 1 <= to)
		modifyTree(m + 1, r, from, to, delta);
}
int queryTree(int l, int r, int i)
{
	if (l == r)
		return tree[getIndex(l, r)];
	unmarkTree(l, r);
	int m = (l + r) / 2;
	if (i <= m)
		return queryTree(l, m, i);
	else
		return queryTree(m + 1, r, i);
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	//freopen("A.in", "r", stdin);
	int testNum;
	scanf("%d", &testNum);
	for (int testInd = 0; testInd < testNum; testInd++)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%d%d%d", &a[i], &b[i], &c[i]);
		int ans = 0;
		for (int z = 0; z <= RANGE; z++)
		{
			memset(tree, 0, sizeof(tree));
			for (int i = 0; i < n; i++)
				if (z >= c[i] && a[i] + b[i] <= RANGE - z)
					modifyTree(0, RANGE, a[i], RANGE - z - b[i], 1);
			for (int x = 0; x <= RANGE - z; x++)
				ans = max(ans, queryTree(0, RANGE, x));
		}
		printf("Case #%d: %d\n", testInd + 1, ans);
	}
	return 0;
}	
