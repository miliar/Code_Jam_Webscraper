#include<cstdio>
#include<algorithm>
#include<cstring>
#include<iostream>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

#define REP(i, n) for(int i=0, _n=(n); i<_n; ++i)

int n, k;

int main()
{
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	int tt=0, T;
	for(tt=0, scanf("%d", &T); tt<T; ) {
		scanf("%d%d", &n, &k);
		int p=1<<n;
		printf("Case #%d: ", ++tt);
		if ((k & (p-1))==(p-1)) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}
