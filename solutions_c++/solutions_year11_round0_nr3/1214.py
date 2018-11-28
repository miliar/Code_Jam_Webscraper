#include <cstdio>

int n, a[20], ans = -1;

void solve(int index, int sum1, int sum2, int xor1, int xor2, int a1){
	if (index == n){
		if (xor1 == xor2 && ans < sum1 && a1 != 0 && a1 != n)
			ans = sum1;
		return;
	}
	solve(index + 1, sum1 + a[index], sum2, xor1 xor a[index], xor2, a1 + 1);
	solve(index + 1, sum1, sum2 + a[index], xor1, xor2 xor a[index], a1);
}

int main(){
	int t;
	scanf("%d", &t);
	for (int j = 1; j <= t; j++){
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%d", &a[i]);
		
		ans = -1;
		
		solve(0, 0, 0, 0, 0, 0);
		
		if (ans == -1)
			printf("Case #%d: NO\n", j);
		else
			printf("Case #%d: %d\n", j, ans);
	}
}
