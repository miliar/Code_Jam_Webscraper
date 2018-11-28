#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <string>
using namespace std;

typedef long long int64;
const int N = 100;
const int LEN = 300;

char word[N][LEN];
int len[N], cnt[LEN];
char s[LEN];
int L, maxdep, ret, n;
const int MOD = 10009;

int calc()
{
	int p = 1, ret = 0;
	for (int i = 0; i < L; ++i)
	{
		if (s[i] == '+')
		{
			ret = (ret + p) % MOD;
			p = 1;
		}
		else
		{
			p = p * cnt[s[i]] % MOD;
		}
	}
	return ret;
}

void DFS(int dep)
{
	if (dep == maxdep)
	{
		ret = (ret + calc()) % MOD;
		return;
	}
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < len[i]; ++j)
			cnt[word[i][j]]++;
		DFS(dep + 1);
		for (int j = 0; j < len[i]; ++j)
			cnt[word[i][j]]--;
	}
}

int main()
{
	freopen("B-small-attempt0.in", "r", stdin); freopen("B.out", "w", stdout);
	int cas, num = 0;
	scanf("%d", &cas);
	while (cas--)
	{
		int k;
		scanf("%s %d", s, &k);
        L = strlen(s);
        s[L++] = '+';
		s[L] = 0;
        scanf("%d", &n);
		for (int i = 0; i < n; ++i)
		{
			scanf("%s", word[i]);
			len[i] = strlen(word[i]);
		}
        printf("Case #%d:", ++num);
		for (maxdep = 1; maxdep <= k; ++maxdep)
		{
			memset(cnt, 0, sizeof(cnt));
			ret = 0;
			DFS(0);
			printf(" %d", ret);
		}
        puts("");
	}
    return 0;
}