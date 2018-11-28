#include <cstdlib>
#include <iostream>
#define base 100003
#define maxn 501

using namespace std;

int tt,n,ii,i,j,k,ans;
int c[maxn][maxn];
int f[maxn][maxn];

int p(int n,int m) {
	int i,cnt;
	if (n==1 || n==m) return 0;
	if (f[n][m]!=0) return f[n][m];
	if (m==1) return 1;
	cnt=0;
	for (i=max(1,2*m-n);i<m;++i)
		cnt=(cnt+p(m,i)*c[n-m-1][m-i-1] % base) % base;
	f[n][m]=cnt;
	return cnt;
}

int main() {
	freopen("pure.in","r",stdin);
	freopen("pure.out","w",stdout);

	memset(c,0,sizeof(c));
	for (i=0;i<maxn;++i) c[i][0]=1;
	for (i=1;i<maxn;++i)
		for (j=1;j<=i;++j)
			c[i][j]=(c[i-1][j-1]+c[i-1][j]) % base;
	scanf("%d\n",&tt);
	for (ii=1;ii<=tt;++ii) {
		scanf("%d\n",&n);
		ans=0;
		for (i=1;i<=n;++i)
			ans=(ans+p(n,i)) % base;
		printf("Case #%d: %d\n",ii,ans);
	}
}
