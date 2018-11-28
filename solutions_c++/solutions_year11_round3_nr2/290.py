#include <cstdio>
#include <algorithm>
using namespace std;
#define NN 1000008
typedef __int64 I64;
I64 t,a[NN],sum[NN],total;

int main()
{
	int n,c,i,test,j,l;

	freopen("b.in","r",stdin);
	freopen("b3.out","w",stdout);
	scanf("%d",&test);
	for (int cas=1; cas<=test; cas++)
	{
		scanf("%d%I64d%d%d",&l,&t,&n,&c);
		for (i=0; i<c; i++) scanf("%d",&a[i]);
		for (j=c; j<n; j++) a[j]=a[j-c];
 
		sum[0]=a[0]*2;
		for (i=1; i<n; i++) sum[i]=a[i]*2+sum[i-1];
 
		if (n>0) sum[n]=sum[n-1];
 
		for (i=0; i<n; i++) if (sum[i]>=t) break;
		if (i>=n) {
			printf("Case #%d: %I64d\n",cas,sum[n-1]);
			continue;
		}
		total=t;
		a[i]=(sum[i]-t)/2;
 
		sort(a+i,a+n);
 
		for (j=n-1; j>=i && j>=n-l; j--) total+=a[j];
		for (; j>=i; j--) total+=a[j]*2;
 
		printf("Case #%d: %I64d\n",cas,total);
	}
	return 0;
}
