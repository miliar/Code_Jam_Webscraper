#include <stdio.h>
#include <string.h>
#include <map>
#include <algorithm>
using namespace std;

map< pair<int,int> ,int> dp;

int dfs(int a, int b) {
	if (a==b) return 0;
	if (a<b) {
		int t = a;
		a = b;
		b = t;
	}
	if ((a%b)==0) return 1;
	pair<int, int> tmp;
	tmp.first = a;
	tmp.second = b;
	if (dp.find(tmp)!=dp.end()) {
		return dp[tmp];
	}
	while (a>b) {
		if (!dfs(a-b, b)) {
			dp[tmp] = 1;
			return 1;
		}
		a-=b;
	}
	dp[tmp] = 0;
	return 0;
}

int a1, a2, b1, b2;
int main() {
	int ca, cases = 0, count;
	int i, j;
	scanf("%d", &ca);
	while (ca--) {
		printf("Case #%d: ", ++cases);
		scanf("%d%d%d%d", &a1, &a2, &b1, &b2);
		count = 0;
		dp.clear();
		for (i=a1;i<=a2;++i) {
			for (j=b1;j<=b2;++j) {
				if (dfs(i,j)) ++count;
			}
		}
		printf("%d\n", count);
	}
	return 0;
}
