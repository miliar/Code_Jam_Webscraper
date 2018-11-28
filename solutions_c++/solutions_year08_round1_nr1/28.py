#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<iostream>
using namespace std;

typedef long long int64;
int64 const oo = 2000000000;
int const maxN = 1000;
int totCases;
int64 a[maxN], b[maxN], c[maxN];
int n;
int64 ans;

bool MyCmp(int const &t1, int const &t2)
{
	return t1 > t2;
}
int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	scanf("%d", &totCases);
	for (int cases(0); cases != totCases; ++cases) {
		printf("Case #%d: ", cases + 1);
		ans = 0;
		scanf("%d", &n);
		for (int i(0); i < n; ++i) scanf("%I64d", &a[i]);
		sort(a, a + n);
		for (int i(0); i < n; ++i) scanf("%I64d", &b[i]);
		sort(b, b + n, MyCmp);
		for (int i(0); i < n; ++i) ans += a[i] * b[i];
		printf("%I64d\n", ans);
	}
}
