#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <set>
#include <map>
#include <algorithm>

#define FOR(i, a, b) for(int i = int(a); i < int(b); i++)
#define INF 2000000000
#define EPS 1e-9
#define PB push_back
#define MP make_pair
#define F first
#define S second
using namespace std;

typedef long long ll;
typedef pair <int, int> ii;

int main() {
//	freopen("candy.in", "r", stdin);
//	freopen("candy.out", "w", stdout);
	
	int T, tc = 0;
	scanf("%d", &T);
	
	while(T--) {
		int n;
		scanf("%d", &n);
		
		int a[105];
		for(int i = 0; i < n; ++i) scanf("%d", &a[i]);
		
		int ans = -1;
		for(int i = 0; i < (1 << n); ++i) {
			int lsum = 0, rsum = 0, lsor = 0, rsor = 0;
			for(int j = 0; j < n; ++j)
				if(i & (1 << j)) {
					lsum += a[j];
					lsor ^= a[j];
				}
				else {
					rsum += a[j];
					rsor ^= a[j];
				}
			
			if(lsum == 0 || rsum == 0) continue;	
			if(lsor == rsor) {
				ans = max(max(ans, lsum), rsum);
//				printf("lsum=%d rsum=%d\n", lsum, rsum);
			}
		}
		
		printf("Case #%d: ", ++tc);
		if(ans == -1) printf("NO\n");
		else printf("%d\n", ans);
	}
	
	return 0;
	}
