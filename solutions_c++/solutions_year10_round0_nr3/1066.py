#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <fstream>
#include <algorithm>
#include <functional>
#include <queue>
#include <map>
#include <climits>
#include <cstring>
#include <list>
#include <ctime>
#include <sstream>
#include <set>

using namespace std;

typedef unsigned long long LL;
typedef pair<int, int> PII;
typedef pair<int, LL> PIL;

#define lowbit(a) ((a) & (-a))
#define two(a) (1 << (a))
#define left(a) (((a) <<1) + 1)
#define right(a) (left(a) + 1)

const int MAX = 1 << 11;
LL  r, k, n;
LL g[MAX], s[MAX];
LL cnt[MAX];

LL solve()
{
	cin >> r >> k >> n;

	LL d = 0;
	for(int i = 0; i < n; i++)
	{
		cin >> g[i];
		d += g[i];
	}
	copy(g, g + n, g + n);
	copy(g, g + n * 2, s);
	for(int i = 1; i <= (n << 1); i++) s[i] += s[i - 1];
	if(d <= k) return r * d;

	memset(cnt, 0, sizeof(cnt));
	map<int, int> vised;
	LL rt = 0;
	int p = 0;

	for(int i = 0; i < r ; i++)
	{
		if(vised.find(p) == vised.end())
		{
			vised[p] = i;
			LL tmp = k + 1;
			if(p) tmp += s[p - 1];
			tmp = lower_bound(s, s + n * 2, tmp) - s;
			
			if(tmp == 0) break;
			if(p) rt += s[tmp - 1] - s[p - 1];
			else rt += s[tmp - 1];

			cnt[i] = rt;
			p = tmp % n;
		}
		else
		{
			int u = vised[p], v = vised[p];

			LL d = 0;
			if(v) d = cnt[v - 1];

			u = i - u;
			rt += (r - i) / u * (rt - d);
			r = vised[p] + ((r - i) % u);
			if(r) rt += cnt[r - 1] - d;
			break;
		}
	}
	return rt;
}

int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": ";
		cout << solve() << endl;
	}
	return 0;
}

/*
1
100 2 2
1 2
*/