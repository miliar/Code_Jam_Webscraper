#include <stdio.h>
#include <algorithm>
using namespace std; 

int main(){
	const int size=1024;
	int T,c,n,a[size],b[size],i;
	long long r;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("a.txt","w",stdout);
	scanf("%d",&T);
	for(c=1; c<=T; c++){
		scanf("%d",&n);
		for(i=0; i<n; i++)
			scanf("%d",&a[i]);
		for(i=0; i<n; i++)
			scanf("%d",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		r=0;
		for(i=0; i<n; i++)
			r+=a[i]*b[n-i-1];
		printf("Case #%d: %I64d\n",c,r);
	}
	scanf("%*s");
	return 0;
}
