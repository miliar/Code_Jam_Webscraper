#include <stdio.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <memory.h>
#include <algorithm>
#include <cassert>
#include <math.h>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a, b) memset(a, b, sizeof(a))

typedef long long lint;
typedef unsigned long long ull;

const double eps = 1e-9;
const int INF = 1000000000;
const lint LINF = 4000000000000000000ll;

void prepare()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
#else
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}

char s[205] = "a zoo ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv\0";
char d[205] = "y qee our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up\0";

char mapping[200];
bool used[30];

char tmp[105];

bool solve()
{
	int l = strlen(s);
	_(mapping, ' ');
	for (int i = 0; i < l; i++)
		mapping[s[i]] = d[i];

	_(used, 0);
	for (int i = 'a'; i <= 'z'; i++)
		used[mapping[i] - 'a'] = true;
	char x = ' ';
	for (int i = 0; i < 26; i++)
		if (!used[i])
		{
			x = i + 'a';
			break;
		}

	for (int i = 'a'; i <= 'z'; i++)
		if (mapping[i] == ' ')
			mapping[i] = x;

	int n;
	scanf("%d\n", &n);
	for (int i = 0; i < n; i++)
	{
		gets(tmp);
		l = strlen(tmp);
		for (int i = 0; i < l; i++)
			tmp[i] = mapping[tmp[i]];
		printf("Case #%d: %s\n", i + 1, tmp);
	}

	return false;
}

int main()
{
	prepare();
	while (solve());
	return 0;
}