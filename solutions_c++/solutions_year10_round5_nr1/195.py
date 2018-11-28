#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <valarray>
#include <algorithm>
#include <functional>
#include <numeric>
#include <complex>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
using namespace std;

int a[100];
int pa[5000000];
int plist[1000000];
int pcount = 0;
int n;

void initprime(int n)
{
	memset(pa, 0, sizeof(pa));
	for (int i = 2; i <= n; ++i) {
		if (!pa[i]) 
			plist[pcount++] = i;
		for (int j = 0; j < pcount && i * plist[j] <= n; ++j) {
			pa[i * plist[j]] = 1;
			if (i % plist[j] == 0)
				break;
		}
	}
}

int calca(int x1, int y1, int x2, int y2, int p)
{
	if (x1 < x2) {
		swap(x1, x2);
		swap(y1, y2);
	}
	x1 -= x2;
	y1 -= y2;
	if (x1 == 0)
		return 0;
	while (y1 <= 0 || y1 % x1 != 0)
		y1 += p;
	return y1 / x1;
}

int calcb(int A, int x, int y, int p)
{
	x *= A;
	while (y < x)
		y += p;
	return y - x;
}

int go(int p)
{
	int A = calca(a[0], a[1], a[1], a[2], p);
	int B = calcb(A, a[0], a[1], p);
	for (int i = 3; i < n; ++i) {
		if ((A * a[i - 1] + B) % p != a[i])
			return -1;
	}
	return (A * a[n - 1] + B) % p;
}

int main()
{
	initprime(1000000);
	freopen("A-small-attempt2.in", "r", stdin);
	freopen("A-small-attempt2.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int d;
		scanf("%d %d", &d, &n);
		for (int i = 0; i < n; ++i)
			scanf("%d", &a[i]);
		int maxn = 1;
		for (int i = 0; i < d; ++i)
			maxn *= 10;
		printf("Case #%d: ", t);
		if (n <= 2) {
			if (a[0] == a[1])
				printf("%d\n", a[0]);
			else
				puts("I don't know.");
			continue;
		}
		set<int> res;
		int minp = 0;
		for (int i = 0; i < n; ++i)
			minp = max(minp, a[i]);
		for (int i = 0; i < pcount && plist[i] < maxn; ++i) {
			if (plist[i] <= minp)
				continue;
			int tmp = go(plist[i]);
			if (tmp == -1)
				continue;
			res.insert(tmp);
		}
		if (res.size() == 1)
			printf("%d\n", *res.begin());
		else
			puts("I don't know.");
	}
	return 0;
}