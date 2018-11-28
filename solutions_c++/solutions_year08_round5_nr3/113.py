#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int b[12];
int a[12][(1<<12)];
int n, m, ans;

int cnt(int z) {
	int ret=0;
	while (z) {
		if (z&1)
			ret++;
		z>>=1;
	}
	return ret;
}

int can1(int i) {
	while (i) {
		if ((i&1) && (i&2))
			return 0;
		i>>=1;
	}
	return 1;
}

int can2(int i,int j) {
	int k;
	for (k=1; k<m; k++)
		if (((j>>k)&1) && ((i>>(k-1))&1))
			return 0;

	for (k=0; k<m-1; k++)
		if (((j>>k)&1) && ((i>>(k+1))&1))
			return 0;
	return 1;
}

int main () {
	int t, c;
	int i, j, k;
	char tmp[16];
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	for (scanf("%d",&t), c=1; c<=t; c++) {
		printf("Case #%d: ",c);
		scanf("%d%d", &n, &m);
		memset(b,0,sizeof(b));
		for (i=1; i<=n; i++) {			
			scanf("%s", &tmp);
			for (j=0;j<m;j++)
				if (tmp[j]=='x')
					b[i]^=(1<<j);				
		}
		
		memset(a,0,sizeof(a));
		for (i=1;i<=n;i++)
			for (k=0; k<(1<<m); k++)
				if (can1(k) && (b[i]&k)==0)
					for (j=0; j<(1<<m); j++)
						if (can1(j) && can2(j,k))					
							a[i][k]=max(a[i][k],a[i-1][j]+cnt(k));
		ans=0;
		for (i=0; i<(1<<m); i++)
			ans=max(ans,a[n][i]);
		printf("%d\n", ans);
	}
	return 0;
}