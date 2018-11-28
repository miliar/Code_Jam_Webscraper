#include <cstdio>
#include <cstring>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <cctype>
#include <bitset>
#include <sstream>
#include <set>
#include <map>

using namespace std;
template <class T> T sqr(T a) { return a * a; }
#define memfill(a, b) memset(a, b, sizeof(a))
#define pb push_back
#define vi vector<int>
#define vii vector<vector<int> >
#define vs vector<string>
#define pii pair<int, int>
#define dist(a, b) sqrt(sqr(a.x - b.x) + sqr(a.y - b.y))
#define bound(x, y, n, m) x >= 0 && y >= 0 && x < n && y < m
#define maxn 12000

int k, len;
char s[maxn];
char t[maxn];

int best;

void update()
{
	int cur = 1;
	for (int i = 1; i < len; i++)
		if (t[i] != t[i - 1])
			cur++;
	best = min(cur, best);
}

int p[maxn];
int used[maxn];

void change()
{
	for (int i = 0; i < len / k; i++)
		for (int j = 0; j < k; j++)
			t[i * k + j] = s[i * k + p[j]];
}

void find(int v)
{
	if (v == k)
	{
		change();
		update();
		return;
	}
	for (int i = 0; i < k; i++)
		if (!used[i])
		{
			p[v] = i;
			used[i] = 1;
			find(v + 1);
			used[i] = 0;
		}
}

void solve()
{
	len = strlen(s);	
	best = 100000;
	memfill(used, 0);
	find(0);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test_num;
	scanf("%d", &test_num);
	for (int test_count = 0; test_count < test_num; test_count++)
	{
		scanf("%d%s", &k, s);
		solve();
		printf("Case #%d: %d\n", test_count + 1, best);
	}
	return 0;
}