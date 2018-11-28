#include<cstdio>
#include<cstring>
#include<string>
#include<queue>
#include<set>
#include<cmath>
#include<iostream>
using namespace std;
int gcd(int a, int b) {
	if (b == 0)
		return a;
	return gcd(b, a%b);
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, t, i, j, k;
	scanf("%d", &T);
	for(t = 1; t <= T; t++){
		__int64 n;
		int pd, pg;
		scanf("%I64d %d %d", &n, &pd, &pg);
		if (pd != 0 && pg == 0) {
			printf("Case #%d: Broken\n", t);
			continue;
		}
		else if (pd != 100 && pg == 100) {
			printf("Case #%d: Broken\n", t);
			continue;
		}
		else if (pd == 0) {
			printf("Case #%d: Possible\n", t);
			continue;
		}
		int g = gcd(pd, 100);
		int d = 100 / g, todayWin = pd / g;
		if (d > n) {
			printf("Case #%d: Broken\n", t);
			continue;
		}
		printf("Case #%d: Possible\n", t);
	}
	return 0;
}
