// C.cpp : 定义控制台应用程序的入口点。
//

#include <stdio.h>

int Solve()
{
	int sum, m, n, xor, tmp;
	sum = xor = 0;
	m = 100000000;
	scanf("%d", &n);
	for(int i = 0; i<n; ++i){
		scanf("%d", &tmp);
		if(tmp < m)
			m = tmp;
		sum += tmp;
		xor ^= tmp;
	}
	if(xor != 0)
		return -1;
	else
		return sum-m;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int nCase;
	scanf("%d", &nCase);
	for(int i = 1; i<=nCase; ++i){
		int ret = Solve();
		if(ret >= 0)
			printf("Case #%d: %d\n", i, ret);
		else
			printf("Case #%d: NO\n", i);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}

