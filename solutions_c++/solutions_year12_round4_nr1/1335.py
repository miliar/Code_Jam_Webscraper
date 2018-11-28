#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <string>
#include <vector>
#define max(a, b) ((a) >= (b) ? (a) : (b))
#define min(a, b) ((a) <= (b) ? (a) : (b))
#define abs(a) ((a) >= 0 ? (a) : -(a))
using namespace std;
/*Template written by Mashimaru*/

int test, n, D, d[10005], l[10005];

bool solve(int i, int h)
{
	if (i == n) return true;
	for (int j = n; j >= i + 1; j--)
		if (h + d[i] >= d[j] && solve(j, min(d[j] - d[i], l[j]))) return true;
	return false;
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &test);
	for (int num = 1; num <= test; num++)
	{
		scanf("%d", &n);
		for (int i = 1; i <= n; i++) scanf("%d %d", &d[i], &l[i]);
		scanf("%d", &d[++n]);
		printf("Case #%d: ", num);
		printf(solve(1, d[1]) ? "YES\n" : "NO\n");
	}
	return 0;
}
