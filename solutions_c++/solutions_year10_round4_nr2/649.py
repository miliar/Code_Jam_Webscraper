#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;
                           
int a[2048];
int b[2048];
int ans;

void solve(int l, int r){
	bool p = 0;
	for (int i=l; i<r; ++i){
		if (a[i] > 0)
			p = 1;
	}
	if (p){
		ans++;
		for (int i=l; i<r; ++i){
			if (a[i]>0) --a[i];
		}                 
		solve(l, (l+r)/2);
		solve((l+r)/2, r);	
	}                     
}


int main(){
#ifndef ONLINE_JUDGE
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	int ntest;
	scanf("%d", &ntest);

	for (int itest=0; itest<ntest; ++itest){
		printf("Case #%d: ", itest+1);
		int n;
		scanf("%d", &n);
		int m = 1 << n;
		for (int i=0; i<m; ++i){
			scanf("%d", &a[i]);
			a[i] = n - a[i];
		}

		for (int i=0; i<m-1; ++i){
			scanf("%d", &b[i]);
		}
		ans = 0;

		solve(0, m);

        printf("%d\n", ans);
	}

	return 0;
}
