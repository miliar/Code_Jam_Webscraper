#include <cstdio>
#include <algorithm>



void solve(int caseNumber) {
	int n;
	scanf("%d", &n);
	int x, r = 0;
	for(int i = 1; i <= n; i++)  {
		scanf("%d", &x);
		if(x != i) r++;
	}

	printf("Case #%d: %d\n", caseNumber, r);
	
}
int main() {
	//freopen("in.txt", "r", stdin);
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) solve(i);

}