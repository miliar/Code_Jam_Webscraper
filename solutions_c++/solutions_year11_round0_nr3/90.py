#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

int main () {
	int T, t = 1;
	
	scanf("%d",&T);
	while (T--) {
		int v[1005], n, sum = 0, sum_x = 0;
		
		scanf("%d",&n);
		
		for (int i=0; i < n; i++) {
			scanf("%d",&v[i]);
			sum_x ^= v[i];
			sum += v[i];
		}
		
		printf("Case #%d: ",t++);
		
		if (sum_x != 0) {
			puts("NO");
			continue;
		}
		
		printf("%d\n",sum - *min_element(v,v+n));
	}
	
	return 0;
}
