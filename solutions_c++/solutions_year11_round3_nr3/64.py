#include <cstdio>
using namespace std;

int T,n,l,r;
int a[10010];

int main() {
	bool ck=false;
	scanf("%d",&T);
	for (int I=1;I<=T;I++) {
		scanf("%d%d%d",&n,&l,&r);
		for (int i=1;i<=n;i++) scanf("%d",&a[i]);
		for (int i=l;i<=r;i++) {
			ck=true;
			for (int j=1;j<=n;j++) {
				int tmp=a[j];
				if (tmp!=0 && (i%tmp!=0 && tmp%i!=0)) {
					ck=false;
					break;
				}
			}
			if (ck) {
				printf("Case #%d: %d\n",I,i);
				break;
			}
		}
		if (!ck)
			printf("Case #%d: NO\n",I);
	}
}
