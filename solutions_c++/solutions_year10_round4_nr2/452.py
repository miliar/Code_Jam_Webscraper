#include <cstdio>
using namespace std;

int a[2000];
int v[1000][1000];

int getans(int l,int r) {
	bool z=true;
	for (int i=l;i<=r;i++) {
		if (a[i]!=0) {
			z=false;
			break;
		}
	}
//	printf("%d %d %d\n",l,r,z);
	if (!z) {
		for (int i=l;i<=r;i++) {
			if (a[i]!=0) a[i]--;
		}
		int mid=(l+r)/2;
		return getans(l,mid)+getans(mid+1,r)+1;
	} else {
		return 0;
	}
}

int main() {
	int cases;
	scanf("%d",&cases);
	for (int cc=1;cc<=cases;cc++) {
		int n,x;
		scanf("%d",&x);
		n=1<<x;
		for (int i=1;i<=n;i++) {
			scanf("%d",&a[i]);
			a[i]=x-a[i];
		}
		int tmp=n;
		for (int i=1;i<=x;i++) {
			tmp=tmp/2;
			for (int j=1;j<=tmp;j++) scanf("%d",&v[i][j]);
		}
		printf("Case %d: %d\n",cc,getans(1,n));
	}
}
