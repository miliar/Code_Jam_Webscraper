#include <cstdio>
#include <cstring>
#define h 50
#define M 100003

int T,t,n,a[h][h],i,j,k;

int C(int n, int m) {
	int p = 1;
	int j = 1;
	for(int i=n-m+1;i<=n;i++) {
		p *= i;
		p /= j;
		p %= M;
		j++;
	}
	return p;
}

int main() {
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	memset(a, 0, sizeof a);
	for(i=2;i<h;i++)
		a[i][1] = 1;
	for(i=2;i<h;i++)
		for(j=1;j<i;j++)
			for(k=i+1;k<h;k++)
				if(k - i >= i - j)
					a[k][i] = (int) ((long long) a[k][i] + (long long) a[i][j] * (long long) C(k - i - 1, i - j - 1)) % M;
	scanf("%d", &T);
	for(t=1;t<=T;t++) {
		scanf("%d", &n);
		k = 0;
		for(i=1;i<=n;i++)
			k = (k + a[n][i]) % M;
		printf("Case #%d: %d\n", t, k);
	}
	return 0;
}