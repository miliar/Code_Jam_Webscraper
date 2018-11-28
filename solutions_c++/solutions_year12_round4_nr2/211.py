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
const int MAXN = 5000;

int n, W, L, t;
int r[MAXN], p[MAXN];
int spis[MAXN];
int x[MAXN], y[MAXN];

bool cmp(const int i, const int j)
{
	return p[i] > p[j];
}

bool dfs(int uk, int sy)
{
//	cerr << "HEre uk = " << uk << endl;
	if (uk == n) return 1;

	int u = p[uk];

	if (sy > L)
	{
		if (sy == 0) return 0;
		return dfs(uk, 0);
	}

	int curx = 0;

	for (int i = 0; i < t; i++)
	{
	 	int l = y[spis[i]]-::r[spis[i]], r = y[spis[i]]+::r[spis[i]];
	 	int L = sy - ::r[u], R = sy + ::r[u];

	 	if (max(L, l) < min(R, r))
	 		curx = max(curx, x[spis[i]]+::r[spis[i]]+::r[u]);
	}

	if (curx > W)
	{
		if (sy == 0) return 0;

		return dfs(uk, 0);
	}
	else
	{
		x[u] = curx; y[u] = sy;
		spis[t++] = u;

//		cerr << "UK + " << uk << endl;
		int ret = dfs(uk+1, sy + r[u] + r[p[uk+1]]);
//		cerr << "returning uk = " << uk << " " << ret << endl;
		return ret;
	}

	return 0;
}

void main2()
{
//	cerr << "Enter\n";
	scanf("%d%d%d", &n, &W, &L);
//	cerr << n << endl;
	for (int i = 0; i < n; i++)
		scanf("%d", r+i),
		p[i] = i;
//	cerr << "Here " << n << " " << W << " " << L << endl;
//	sort(p, p+n, cmp);
//	cerr << "Here " << n << " " << W << " " << L << endl;

	int iter = 0;
	while(true)
	{
		t = 0;
		if (dfs(0, 0)) break;
		cerr << "Here\n";

		if (iter++ < 10) next_permutation(p, p+n);
		else random_shuffle(p, p+n);

		cerr << "OUT\n";
	}

	cerr << "Here\n";
	gout;
	for (int i = 0; i < n; i++)
		printf("%.1lf %.1lf%c", 1.*x[i], 1.*y[i], " \n"[i+1==n]);
	cerr << "Ended\n";
}

int main()
{
	srand(13513518);
	scanf("%d", &test_num);

	for (int i = 0; i < test_num; i++)
		main2();

	return 0;
}
