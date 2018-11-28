#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int c=110;
const int inf=1000000000;
int ii,t,p,q;
int ans;
int m[c];
int a[c][c];
int main() {
	int i,j,len;
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&t);
	for (ii=1; ii<=t; ++ii) {
		scanf("%d%d",&p,&q);
		for (i=1; i<=q; ++i) scanf("%d",&m[i]);
		m[0]=0;
		m[q+1]=p+1;
		for (i=0; i<=q; ++i) a[i][i+1]=0;
		for (len=2; len<=q+1; ++len) {
			for (i=0; i+len<=q+1; ++i) {
				a[i][i+len]=inf;
				for (j=i+1; j<=i+len-1; ++j)
					if (a[i][j]+a[j][i+len]<a[i][i+len])
						a[i][i+len]=a[i][j]+a[j][i+len];
				a[i][i+len]+=m[i+len]-m[i]-2;
			}
		}
		ans=a[0][q+1];
		printf("Case #%d: %d\n",ii,ans);
	}
	return 0;
}