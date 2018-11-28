#include <stdio.h>
#include <algorithm>
#include <memory.h>
#include <queue>
#include <math.h>
#include <vector>
#include <map>
#include <stack>
#include <string.h>
#include <string>
#include <iostream>
#include <deque>
#include <stdlib.h>
#include <stack>
using namespace std;
int _T;

int main() {
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	scanf("%d",&_T);
	for (int _t=1;_t<=_T;_t++) {
		int n; cin >> n;
		int xr=0,sum=0,mn=1e9;
		while (n--) {
			int x; cin >> x;
			xr ^= x;
			sum += x;
			mn = min(mn,x);
		}
		
		printf("Case #%d: ",_t);
		if (xr == 0) cout << sum - mn << endl;
		else cout << "NO" << endl;
	}
	
	return 0;
}
