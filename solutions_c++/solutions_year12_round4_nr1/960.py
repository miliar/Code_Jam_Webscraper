#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cmath>
#include <cstring>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
using namespace std; 

#define f first
#define s second
#define mp make_pair
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define forit(it,S) for(__typeof(S.begin()) it = S.begin(); it != S.end(); ++it)

typedef pair <int, int> pi;

const double eps = 1e-9;
int d[111111], l[111111];
int dp[111111], n, target;

int main() {
	int tests;
	scanf("%d", &tests);
	for (int casenum = 1; casenum <= tests; ++casenum) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%d%d", &d[i], &l[i]);
		}
		scanf("%d", &target);
		
		for (int i = 1; i < n; ++i)
			dp[i] = 0;
		dp[0] = d[0];
		
		bool reach = false;
		for (int i = 0; i < n; ++i) {
			if (d[i] + dp[i] >= target) {
				reach = true;
				break;
			}			
			for (int j = i + 1; j < n; ++j) {
				if (d[i] + dp[i] < d[j]) break;
				dp[j] = max(dp[j], min(l[j], d[j] - d[i]));
			}	
		}
		printf("Case #%d: ", casenum);
		if (reach)
			puts("YES");
		else
			puts("NO");				
	}
	return 0;		
}

