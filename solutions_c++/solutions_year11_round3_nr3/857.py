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
	int T;
	scanf("%d", &T);
	
	for(int tc = 1; tc <= T; ++tc) {
		int n, l, h;
		scanf("%d%d%d", &n, &l, &h);
		
		int a[10005];
		for(int i = 0; i < n; ++i) scanf("%d", &a[i]);
		
		int ans = -1;
		for(int i = l; i <= h; ++i) {
			bool valid = 1;
			for(int j = 0; j < n; ++j)
				if((i%a[j] != 0) && (a[j]%i != 0)) {
					valid = 0;
					break;
				}
			
			if(valid) { ans = i; break; }
		}
		
		printf("Case #%d: ", tc);
		if(ans > -1) printf("%d\n", ans);
		else printf("NO\n");
	}
	
	return 0;
	}
