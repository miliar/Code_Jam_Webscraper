#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int gcd(int a, int b){
	if (a==0)
		return b;
	return gcd(b%a, a);
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large-out.txt", "w", stdout);
	int T; cin >> T;
	for (int cas = 1; cas <= T; cas++)
	{
		printf("Case #%d: ", cas);
		int pd, pg;
		long long N;
		scanf("%lld%d%d", &N, &pd, &pg);
		int d = gcd(pd, 100);
		int a = pd / d;
		int b = 100 / d;
		if (N < b){
			printf("Broken\n");
			continue;
		}
		if (pd != 0 && pg == 0)
			printf("Broken\n");
		else if (pd != 100 && pg == 100)
			printf("Broken\n");
		else printf("Possible\n");
	}
}