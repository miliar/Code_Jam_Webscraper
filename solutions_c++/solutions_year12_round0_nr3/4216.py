#include <cstdio>
int tt,ii;
int a,b;
bool ok(int a, int b) {
	int k=0;
	int aa=a;
	int st=1;
	int i;
	while (aa>0) {
		k++;
		st*=10;
		aa/=10;
	}
	for (i=1; i<=k; ++i) {
		a=a/10+a%10*(st/10);
		if (a==b) return 1;
	}
	return 0;
}
int main() {
	scanf("%d",&tt);
	int i,j;
	int ans;
	for (ii=1; ii<=tt; ++ii) {
		scanf("%d%d",&a,&b);
		ans=0;
		for (i=a; i<=b; ++i)
			for (j=i+1; j<=b; ++j)
				if (ok(i,j)) ++ans;
		printf("Case #%d: %d\n",ii,ans);
	}
	return 0;
}
