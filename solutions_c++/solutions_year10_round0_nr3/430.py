#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
#define maxn 2005
int Test,Case,l,n,m,r,a[maxn],p[maxn];
long long ret,sum[maxn];

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	for (scanf("%d",&Test);Test;--Test) {
		scanf("%d%d%d",&r,&m,&n);
		for (int i=0;i<n;i++)
			scanf("%d",&a[i]);
		for (int i=0;i<n;i++)
			a[n+i]=a[i];
		for (int i=0,j=0,s=0;i<n;s-=a[i++]) {
			for (;j<n+i && s+a[j]<=m;s+=a[j++]);
			p[i]=j%n;sum[i]=s;
		}
		ret=0;
		for (int i=0,j=0;i<r;i++,j=p[j])
			ret+=sum[j];
		printf("Case #%d: %I64d\n",++Case,ret);
	}
	return 0;
}
