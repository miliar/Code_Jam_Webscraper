#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <queue>
#include <map>
#include <set>
using namespace std;

void calc(int no)
{
	int n, m, a;
	int x1, y1, x2, y2;
	
	cin >> n >> m >> a;
	
	for (x1 = 1; x1 <= n; x1++) {
		for (y2 = a / x1; y2 <= m; y2++) {
			for (y1 = 1; y1 <= m; y1++) {
				x2 = (x1 * y2 - a) / y1;
				if (x2 > n || x2 < 0) continue;
				if (x1 * y2 - y1 * x2 == a) {
					printf("Case #%d: 0 0 %d %d %d %d\n", no, x1, y1, x2, y2);
					return;
				}
			}
		}
	}
	
	printf("Case #%d: IMPOSSIBLE\n", no);
	
	return;
}

int main()
{
	int n;
	int i;
	
	cin >> n;
	
	for (i = 0; i < n; i++) {
		calc(i + 1);
	}
	
	return 0;
}
