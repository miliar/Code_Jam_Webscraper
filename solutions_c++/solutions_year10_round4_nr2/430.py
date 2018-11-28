#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;

long long f[5000][50];
int a[5000];

void work()
{
	memset(a,0,sizeof(a));
	memset(f, 1, sizeof(f));
	int m;
	scanf("%d", &m);
	int n = 1 << m;
	while (n) {
		for (int i = 0; i < n; i++)
			scanf("%d", a + i + n);
		n /= 2;
	}
	n = 1 << m;
	for (int i = n; i < 2*n; i++)
		for (int j = 0; j <= min(m,a[i]); j++) 
			f[i][j] = 0;
	for (int i = n - 1; i >= 1; i--)
		for (int j = m; j >= 0; j--) {
			f[i][j] = f[i][j+1];
			f[i][j] = min(f[i][j], f[i*2][j] + f[i*2+1][j] + a[i]);
			f[i][j] = min(f[i][j], f[i*2][j+1] + f[i*2+1][j+1]);
		}
	printf("%d\n", f[1][0]);
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t, m = 0;
	scanf("%d", &t);
	while (t--) {
		printf("Case #%d: ", ++m);
		work();
	}
}
