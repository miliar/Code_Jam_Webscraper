#include <algorithm>
#include <iostream>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#include <map>
#include <set>

#define SIZE(A) ((int)A.size())
#define LENGTH(A) ((int)A.length())
#define MP(A,B) make_pair(A,B)
#define PB(A) push_back(A)

typedef long long ll;
typedef double ld;

int	fx[] = {-1, 0, +1, 0}, fy[] = {0, +1, 0, -1},
	ex[] = {-1, -1, 0, +1, +1, +1, 0, -1}, ey[] = {0, +1, +1, +1, 0, -1, -1, -1};

using namespace std;

int test_num, case_number;

#define gout case_number++, printf("Case #%d: ",case_number), cout
#define MAXN 70000

int n;
int d[MAXN], l[MAXN], x[MAXN];

bool dfs(int u)
{
 	if (u == n) return 1;

 	int p = lower_bound(x, x+n+1, x[u]+d[u]+1)-x-1;

 	for (; p > u; p--)
 	{
		if (min(x[p]-x[u], l[p]) > d[p])
		{
			d[p] = min(x[p]-x[u], l[p]);
			if (dfs(p)) return 1;
		}
 	}

 	return 0;
}

void main2()
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d%d", x+i, l+i);
	scanf("%d", x+n);

	d[0] = min(x[0], l[0]);
	for (int i = 1; i <= n; i++)
		d[i] = -1;

	gout << (dfs(0)?"YES":"NO") << endl;
}

int main()
{
	scanf("%d", &test_num);

	for (int i = 0; i < test_num; i++)
		main2();

	return 0;
}
