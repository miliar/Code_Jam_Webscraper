#include <cstdio>
#include <algorithm>

using namespace std;

#define nmax 800

int a[nmax],b[nmax];

int main()
{

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t,n,i,j,T;
	long long s;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++) scanf("%d",&a[i]);
		for(i=0;i<n;i++) scanf("%d",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		s=0;
		for(i=0,j=n-1;i<n;i++,j--) s+=(long long)a[i]*b[j];
		printf("Case #%d: %lld\n",t,s);
	}
	return 0;
}