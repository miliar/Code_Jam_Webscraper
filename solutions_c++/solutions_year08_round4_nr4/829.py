#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
#include <set>
#include <stack>
#include <string>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

#define FOR(i, k, n) for(int i = (k); i < (n); i++)
#define FORZ(i, n) FOR(i, 0, n)
#define pb push_back
#define sz(x) x.size()
#define all(x) x.begin(), x.end()
#define cl(x) memset(x, 0, sizeof(x))

int perm[5];
int ans, len;
char str[1009];
char word[1009];

void Check()
{
	int d = 1;
	char c = str[0];
	FORZ(i, len)
		if(str[i] != c)
		{
			d++;
			c = str[i];
		}
	if(d < ans || ans == -1)
		ans = d;
}

void Make(int a, int k)
{
	if(a == k)
	{
		FORZ(i, len)
		{
			int cnt = i / k;
			str[i] = word[perm[i % k] - 1 + cnt * k];
		}
		Check();
		return;
	}
	FORZ(j, k)
	{
		bool flag = false;
		FORZ(x, a)
			if(perm[x] == j + 1)
			{
				flag = true;
				break;
			}
		if(flag)
			continue;
		perm[a] = j + 1;
		Make(a + 1, k);
	}
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int N, k, n;
	scanf("%d", &N);
	FORZ(i, N)
	{
		ans = -1;
		scanf("%d\n", &k);
		gets(word);
		len = strlen(word);
		strcpy(str, word);
		Check();
		cl(perm);
		Make(0, k);
		printf("Case #%d: %d\n", i + 1, ans);
	}
	return 0;
}