#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <string>
#include <iostream>
#include <functional>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>

using namespace std;

#define	COUNT(a)	(sizeof(a) / sizeof((a)[0]))

long long gcd(long long a, long long b)
{
	while (a) { long long tmp = b % a; b = a; a = tmp; }
	return b;
}

int main(int argc, char *argv[])
{
	int nc, ci;
	
	scanf("%d", &nc);
	for (ci = 1; ci <= nc; ci++) {
		long long n, d, g;
		scanf("%lld %lld %lld", &n, &d, &g);
		bool ans = false;
		long long x = gcd(d, 100);
		if (100 / x <= n) {
			if (d == 0) {
				if (g >= 0 && g < 100) ans = true;
			} else if (d == 100) {
				if (g > 0) ans = true;
			} else {
				if (g > 0 && g < 100) ans = true;
			}
		}
		
		printf("Case #%d: %s\n", ci, ans ? "Possible" : "Broken");
	}
	
	return 0;
}
