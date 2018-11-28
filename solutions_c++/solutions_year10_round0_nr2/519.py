#include <stdio.h>

long long t,n,a[1000],d,d1,i;

int del(long long x,long long y) {
if (!y) return x; else return del(y,x%y);
}

int main() {

freopen("C.in","r",stdin);
freopen("C.out","w",stdout);


scanf("%I64d",&t);

for (int ct=1;ct<=t;ct++) {
	scanf("%I64d",&n);
	for (i=0;i<n;i++) scanf("%I64d",&a[i]);
	printf("Case #%d: ",ct);
	d=a[0]-a[1];
	if (d<0) d=-d;
	for (i=2;i<n;i++) {
		d1=a[i]-a[0];
		if (d1<0) d1=-d1;
		d=del(d,d1);
		}	
	d1=a[0]%d;
	d1=(d-d1)%d;
	printf("%I64d\n",d1);
	}



return 0;
}
