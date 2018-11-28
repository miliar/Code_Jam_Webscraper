#if 1
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <stack>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <functional>
#include <algorithm>
#include <cmath>
#include <bitset>
#include <cstdio>
using namespace std;

typedef long long LL;
typedef long double LD;
const LD eps = 1e-9;

typedef pair<int, int> pii;
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) cerr << #x << " = " << x << endl;

const int maxn = 2 * (1 << 11);
LL tree[maxn][64];
int cost[maxn];
int miss[maxn];
const LL inf = 2024 * 100000;

int N;
LL go(int root, int alreadyMiss, int l = 0, int r = N - 1)
{
	if(l == r)
	{
		if(alreadyMiss <= miss[l])
			return 0;
		else
			return inf;
	}
	LL &res = tree[root][alreadyMiss];
	if(res != -1)
		return res;
	
	int m = (l + r) / 2;
	// miss it:
	LL p1 = go(2 * root + 1, alreadyMiss + 1, l, m) + go(2 * root + 2, alreadyMiss + 1, m + 1, r);
	// not miss
	LL p2 = go(2 * root + 1, alreadyMiss, l, m) + go(2 * root + 2, alreadyMiss, m + 1, r) + cost[root];
	p1 = min(p1, inf);
	p2 = min(p2, inf);
	res = min(p1, p2);
	return res;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t; scanf("%d", &t);
	for(int z = 0; z < t; ++z)
	{
		int n; scanf("%d", &n);
		vector<int> m(1<<n);
		for(int i = 0; i < m.size(); ++i)
			scanf("%d", &miss[i]);
		N = 1 << n;
		vector< int > a;
		for(int i = n - 1; i >= 0; --i)
		{
			vector<int> e;
			for(int j = 0; j < (1 << i); ++j)
			{
				int w; scanf("%d", &w);
				e.pb(w);
			}
			reverse(e.begin(), e.end());
			for(int j = 0; j < e.size(); ++j)
				a.pb(e[j]);
		}
		reverse(a.begin(), a.end());
		for(int i = 0; i < a.size(); ++i)
			cost[i] = a[i];
		memset(tree, -1, sizeof tree);
		printf("Case #%d: %d\n",  z + 1, (int)go(0, 0));


	}
	
	return 0;
}
#endif