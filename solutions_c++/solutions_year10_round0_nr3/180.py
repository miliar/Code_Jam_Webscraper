#include <iostream>
#include <fstream>
#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>

using namespace std;

int n, k, r;
int g[1100];

void Load()
{
	scanf("%d%d%d", &r, &k, &n);
	int i;
	for (i = 0; i < n; i++)
	{
		scanf("%d", &g[i]);
	}
}

int go[1100];
int cnt[1100];
int was[1100];
long long wsum[1100];

void Solve()
{
	int i;
	for (i = 0; i < n; i++)
	{
		int j = i;
		int sum = 0;
		while (sum + g[j] <= k)
		{
			sum += g[j];
			j = (j + 1) % n;
			if (j == i) break;
		}
		go[i] = j;
		cnt[i] = sum;
	}
	/*cerr << "Goes counted:\n";
	for (i = 0; i < n; i++) cerr << "(" << go[i] << "," << cnt[i] << ") ";
	cerr << "\n";*/
	int lft = r;
	int cur = 0;
	long long ans = 0;
	memset(was, 0xFF, sizeof(was));
	i = 0;
	was[0] = 0;
	wsum[0] = 0;
	int f = 0;
	while (lft > 0)
	{
		ans += cnt[cur];
		cur = go[cur];
		//cerr << "Jumped to " << cur << " new ans = " << ans << " lft = " << lft << "\n";
		i++;
		lft--;
		if (was[cur] != -1 && f == 0)
		{
			int num = lft / (i - was[cur]);
			ans += (ans - wsum[cur]) * num;
			lft -= num * (i -was[cur]);
			f = 1;
		}
		was[cur] = i;
		wsum[cur] = ans;
	}
	cout << ans;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int nt, it;
	scanf("%d", &nt);
	for (it = 0; it < nt; it++)
	{
		printf("Case #%d: ", it + 1);
		Load();
		Solve();
		printf("\n");
	}
	return 0;
}