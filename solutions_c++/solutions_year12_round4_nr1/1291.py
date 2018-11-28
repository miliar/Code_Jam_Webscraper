#include <iostream>
using namespace std;

#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <cstdio>
#include <cassert>
#include <vector>
#include <map>
#include <string>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <set>
using namespace std;

#define REP(i,n) for(int i = 0; i < n; i++)

void openFiles() {
	freopen("test5.in", "rt", stdin);
	freopen("test5.out", "wt", stdout);	
}

void solve()
{
	int n; scanf("%d ", &n);
	vector<int> d(n), l(n);
	for (int i = 0; i < n; i++) {
		scanf("%d %d ", &d[i], &l[i]);
	}
	int D; scanf("%d ", &D);


	static int ntest = 0;
	printf("Case #%d: ", ++ntest);

	vector<int> lowest(n, 0);
	lowest[0] = d[0];
	for (int i = 0; i < n; i++) {
		int r = lowest[i];
		for (int j = i + 1; j < n; j++) {
			int dd = d[j] - d[i];
			if (r == 0 || dd > r) {
				break;
			}
			int lw = min(dd, l[j]);

			if (lowest[j] < lw) {
				lowest[j] = lw;
			}
		}
		if (r >= D - d[i]) {
			printf("YES\n");
			return;
		}
	}

	printf("NO\n");

}

int main()
{
	openFiles();

	int n; scanf("%d ", &n);
	// make sure output directory exists MY_SOLUTION/output
	for (int i = 0; i < n; i++) {		
		solve();
	}
	
	return 0;
}