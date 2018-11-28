#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <set>
#include <map>
#include <string>
#include <vector>

using namespace std;

int x[64];
int v[64];

int main(){	
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	
	int ntest;
	
	scanf("%d", &ntest);
	
	for (int itest=0; itest<ntest; ++itest){
	
		int n, k, b, t;
		scanf("%d%d%d%d", &n, &k, &b, &t);
		
		for (int i=0; i<n; ++i)
			scanf("%d", &x[i]);
		for (int i=0; i<n; ++i)
			scanf("%d", &v[i]);
			
		int m = 0;
		int ans = 0;
		for (int i=n-1; i>=0; --i){
			if (t*v[i] >= b-x[i]){
				++m;
				if (m >= k)
					break;
			}
			else{
				ans += k-m;				
			}		
		}
		printf("Case #%d: ", itest+1);
		
		if (m < k) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}

    return 0;
}

