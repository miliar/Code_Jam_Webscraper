#include <cstdio>
#include <cstdlib>

#include <algorithm>

using namespace std;

int n, num[1000];

void input() {
	scanf("%d", &n);
	for(int i = 0;i < n;i ++) scanf("%d", &num[i]);
}

void solve() {
	int sum = 0;
	for(int i = 0;i < n;i ++) sum ^= num[i];

	if(sum != 0) {
		printf("NO\n");
		return ;
	}

	sum = 0;
	int mmin = 100000000;
	for(int i = 0;i < n;i ++) {
		sum += num[i];
		if(num[i] < mmin) mmin = num[i];
	}

	printf("%d\n", sum - mmin);
}

int main() {
	freopen("C-large.in", "r", stdin);
	//freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int cas = 1;cas <= T;cas ++) {
		input();
		printf("Case #%d: ", cas);
		solve();
	}
	return 0;
}