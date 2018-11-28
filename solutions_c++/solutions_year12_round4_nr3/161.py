


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

int T, n, x[2005], ans[2005];
bool flag;

void f(int l, int r, int ll, int rr) {
printf("%d %d\n", l, r);
	if (l==r) {
		if (x[l]!=rr) flag = false;
		else ans[l] = 0;
	}
	else if (l<r) {
	
	
	
		if (x[l]>r+1) {
			flag = false;
		}
		else if (x[l]==r+1) {
			ans[l] = ans[l-1] - 1;
			f(l+1, r, l, rr); 
			if (!flag) return ;
		}
		else {
			if (ll==0) {
				ans[l] = 1000000000;
				ans[x[l]] = 1000000000;
				f(l+1, x[l]-1, l, x[l]);
				if (!flag) return ;
				f(x[l]+1, r, l, rr);
				if (!flag) return ;
			}
			else {
				ans[l] = ans[ll]/10;
				ans[x[l]] = (int)((ans[rr]-ans[l])/(double)(rr-l) *(double)(x[l]-l) + ans[l] + 2 );
				f(l+1, x[l]-1, l, x[l]);
				if (!flag) return ;
				f(x[l]+1, r, l, rr);
				if (!flag) return ;
			}
		}

	}	
	
}

int main() {

	scanf("%d",&T);
	for (int tt=1; tt<=T; tt++) {
		scanf("%d",&n);
		for (int i=1; i<n; i++) scanf("%d",&x[i]);
		flag = true;
		ans[0] = ans[n+1] = 1000000000 + 1;
		f(1, n, 0, n+1);
		if (flag) {
			printf("Case #%d:",tt);
			for (int i=1; i<=n; i++) {
				printf(" %d", ans[i]);
			}
			printf("\n");
			
		}
		else {
				printf("Case #%d: Impossible\n",tt);
		}
	
	
	
	}
	
	return 0;
}


