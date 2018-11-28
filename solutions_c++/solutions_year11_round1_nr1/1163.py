#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

using namespace std;

int main() {
	int t, c;
	scanf("%d", &t);
	c = 1;
	while(t--) {
		long long int n, pd, pg;
		cin >> n >> pd >> pg;
		if(pg == 100 && pd != 100) {
			printf("Case #%d: Broken\n", c);
			c++;
		}
		else if(pg == 0 && pd != 0) {
			printf("Case #%d: Broken\n", c);
			c++;
		}
		else if(n >= 100) {
			printf("Case #%d: Possible\n", c);
			c++;
		}
		else {
			bool a = false;
			for(long long int i = 1; i <= n; ++i) {
				if((i*pd) % 100 != 0) {
					continue;
				}
				else {
					a = true;
					break;
				}
			}
			if(a) {
				printf("Case #%d: Possible\n", c);
				c++;
			}
			else {
				printf("Case #%d: Broken\n", c);
				c++;
			}
		}
	}
	return 0;
}
