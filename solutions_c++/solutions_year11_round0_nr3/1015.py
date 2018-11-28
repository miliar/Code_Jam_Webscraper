#include <cstdio>
#include <algorithm>

using namespace std;

void solve(int caseNumber) {
	int n;
	scanf("%d", &n);

	int sum = 0;
	int xorSum = 0;
	int small = 1<<29;

	for(int i = 0; i < n; i++) {
		int x;
		scanf("%d", &x);

		small = min(small, x);
		sum += x;
		xorSum ^= x;
	}

	if(xorSum) printf("Case #%d: NO\n", caseNumber);
	else printf("Case #%d: %d\n", caseNumber, sum-small);
}

int main() {
	//freopen("in.txt", "r", stdin);
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) solve(i);

}