


#include <iostream>
#include <iomanip>
#include <fstream>

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

#include <sstream>
#include <string>

#include <bitset>
#include <deque>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>

#include <algorithm>

#include <utility>

using namespace std;



const int inf = 2000000000;
const long long linf = 9000000000000000000LL;
const double finf = 1.0e18;
const double eps = 1.0e-8;

int T, n, d[10005], l[10005], D, a[10005];
bool ans;

int main() {

	scanf("%d",&T);
	for (int tt=1; tt<=T; tt++) {
		scanf("%d",&n);
		for (int i=1; i<=n; i++) {
			scanf("%d%d", &d[i], &l[i]);
		}
		scanf("%d",&D);
		if (n==1) {
			if (D-d[1]<=d[1]) {
				printf("Case #%d: YES\n",tt);
			}
			else {
				printf("Case #%d: NO\n",tt);
			}
		}
		else {
			memset(a, 0, sizeof(a));
			a[1] = d[1];
			for (int i=2; i<=n; i++) {
				for (int j=1; j<i; j++) {
					if (d[i]-d[j]<=a[j]) {
						a[i] = max(a[i], min(d[i]-d[j], l[i]));
					}
				}
			}
			ans = false;
			for (int i =1; i<=n; i++) {
				if (D-d[i]<=a[i]) {
					ans = true;
					break;
				}
			}
			if (ans) {
				printf("Case #%d: YES\n",tt);
			
			}
			else {
				printf("Case #%d: NO\n",tt);
			}
		}
	}
	
	return 0;
}


