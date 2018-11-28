#include <cmath>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cctype>
#include <stack>
using namespace std;

typedef long long int int64;

int64 mdc(int64 a, int64 b) {
	if (b == 0) return a;
	return mdc(b, a % b);	
}


int main()
{	
	int t;
	scanf("%d", &t);
	for (int k = 0; k < t; k++) {
		int64 n, pd, pg;
		scanf("%lld %lld %lld", &n, &pd, &pg);
		int64 d, a, g, b, m;
		m = mdc(pd, 100);
		d = 100 / m;
		if (d > n) {
			//printf("%lld\n", d);
			printf("Case #%d: Broken\n", k+1);
			continue;
		}
		a = pd / m;
		m = mdc(pg, 100);
		g = 100 / m;
		b = pg / m;
		
		if (g == 0 && d != 0) {
			printf("Case #%d: Broken\n", k+1);
			continue;
		}
		if (b == 0 && a != 0) {
			printf("Case #%d: Broken\n", k+1);
			continue;	
		} 
		if (g - b == 0 && d - a != 0) {
			printf("Case #%d: Broken\n", k+1);
			continue;
		}
		printf("Case #%d: Possible\n", k+1);
	}
	return 0;
}