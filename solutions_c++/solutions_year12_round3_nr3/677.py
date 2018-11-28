#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <ctime>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <sstream>
#include <iomanip>
#include <deque>
#include <algorithm>
#include <functional>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
#define all(v) v.begin(), v.end()

int n, m;
pair <ull, int> A[4], B[101];

ull bf(int i, int j)
{
	ull rez = 0;
	if (i >= n) return 0;
	if (j >= m) return 0;
	if (A[i].second == B[j].second)
	{
		ull tmp = min(A[i].first, B[j].first);
		rez += tmp;
		A[i].first -=  tmp;
		B[j].first -= tmp;
		rez += max(bf(i, j+1), bf(i+1, j));
		A[i].first += tmp;
		B[j].first += tmp;
		return rez;
	}
	else {
		rez += max(bf(i, j+1), bf(i+1, j));
		return rez;
	}
}

int main()
{
	int cases;
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	scanf("%d", &cases);
	for (int casei = 1; casei <= cases; ++casei)
	{
		printf("Case #%d: ", casei);
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; ++i)
		{
			scanf("%llu %d", &A[i].first, &A[i].second);
		}
		for (int i = 0; i < m; ++i)
		{
			scanf("%llu %d", &B[i].first, &B[i].second);
		}
		ull res = bf(0, 0);

		printf("%llu\n", res);
	}
	return 0;
}