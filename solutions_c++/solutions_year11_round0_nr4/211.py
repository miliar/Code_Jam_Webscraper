// D.cpp : 定义控制台应用程序的入口点。
//
#include <stdio.h>
#include <algorithm>

using namespace std;

int a[1000], b[1000];

int Solve()
{
	int n, ans;
	scanf("%d", &n);
	for(int i = 0; i<n; ++i){
		scanf("%d", &a[i]);
		b[i] = a[i];
	}
	ans = 0;
	sort(a, a+n);
	for(int i = 0; i<n; ++i)
		if(a[i] != b[i])
			ans++;
	return ans;
}

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	int nCase;
	scanf("%d", &nCase);
	for(int i = 1; i<=nCase; ++i){
		printf("Case #%d: %d.000000\n", i, Solve());
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}

