#include <iostream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
#include <string>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <complex>
using namespace std;

typedef long long int64;

int bit_cnt(int n)
{
	int result = 0;
	for (;n; n&= n-1, ++result);
	return result;
}


char dest[256];
int mp[128][128];
int use[128];
int evalue(string s)
{
	int ans = 0, t = 1;
	for (int i = 0; i < s.length(); ++i)
	{
		if (s[i] == '+')
		{
			ans = ans + t;
			ans %= 10009;
			t = 1;
		}
		else
		{
			t = t * use[s[i]];
			t %= 10009;
		}
	}
	return (ans + t) % 10009;
}

int tot_k;
int ans[20];
void solve(int n, int k)
{

	int x = tot_k - k;
	ans[x] = (ans[x] + evalue(dest)) % 10009;
	if (k == 0) return;
	{
		
		for (int i = 0; i < n; ++i)
		{
			for (int j = 'a' ; j <= 'z'; ++j)
			{
				use[j] += mp[i][j];
			}
			solve(n, k - 1);
			for (int j = 'a' ; j <= 'z'; ++j)
			{
				use[j] -= mp[i][j];
			}
		}
	}
}
char buff[1024];
int main()
{
freopen("r3\\B-small-attempt4.in", "r", stdin);
freopen("r3\\B-small-attempt4.out", "w", stdout);
	int cas;scanf("%d", &cas);
	int id = 1;
	while (cas--)
	{
		int k;
		scanf("%s%d", dest, &k);
		tot_k = k;
		int n;
		scanf("%d", &n);
		memset(mp, 0, sizeof mp);
		for (int i = 0; i < n; ++i)
		{
			
			scanf("%s", buff);
			for (int j = 0; buff[j]; ++j) ++mp[i][buff[j]];
		}
		
		printf("Case #%d:", id++);
		memset(ans, 0, sizeof ans);
		memset(use, 0, sizeof use);
		solve(n, k);
		for (int i = 1; i <= tot_k; ++i)
		printf(" %d", ans[i]);

		puts("");
		cerr << id - 1 << endl;
	}
	return 0;
}
