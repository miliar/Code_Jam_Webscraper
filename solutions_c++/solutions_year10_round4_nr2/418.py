#include <iostream>
#include <cstdlib>
#include <cstdio>
#define maxlong 1000000000

using namespace std;

int ii,tt,i,n,j,k,ans;
int f[12][1024][14];
int mini[12][1024];
int a[1024];
int cost[12][1024];

int main() {
	freopen("worldcup.in","r",stdin);
	freopen("worldcup.out","w",stdout);

	scanf("%d\n",&tt);
	for (ii=1;ii<=tt;++ii) {
		scanf("%d\n",&n);
		memset(f,0,sizeof(f));
		for (i=0;i<=(1 << n)-1;++i) scanf("%d",&mini[n][i]);
		for (i=n-1;i>=0;--i)
			for (j=0;j<=(1 << i)-1;++j)
				scanf("%d",&cost[i][j]);
		for (i=n-1;i>=0;--i)
			for (j=0;j<=(1 << i)-1;++j) mini[i][j]=min(mini[i+1][j*2],mini[i+1][j*2+1]);
		for (i=1;i<(1 << n);++i)
			for (k=mini[n][i]+1;k<=n+1;++k)
				f[n][i][k]=maxlong;
		for (i=n-1;i>=0;--i)
			for (j=0;j<=(1 << i)-1;++j) {
				for (k=0;k<mini[i][j];++k)
					f[i][j][k]=min(f[i+1][j*2][k+1]+f[i+1][j*2+1][k+1],f[i+1][j*2][k]+f[i+1][j*2+1][k]+cost[i][j]);
				f[i][j][k]=f[i+1][j*2][k]+f[i+1][j*2+1][k]+cost[i][j];
				for (k=mini[i][j]+1;k<=n+1;++k) f[i][j][k]=maxlong;
			}
		ans=min(f[0][0][1],f[0][0][0]);
		printf("Case #%d: %d\n",ii,ans);
	}
}
