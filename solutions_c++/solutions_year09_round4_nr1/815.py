#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int a[50], n;
char s[1000];
int main() {
	int T; scanf("%d", &T);
	for (int cas=1;cas<=T;cas++) {
		memset(a,0,sizeof(a));
		scanf("%d", &n);
		for (int i=0;i<n;i++) {
			scanf("%s", s);
			for (int j=n-1;j>=0;j--) if (s[j]=='1') {a[i]=j; break;}
		}
		//for (int i=0;i<n;i++) printf("%d\n", a[i]);
		int ret=0;
		for (int i=0;i<n;i++) {
			//for (int x=0;x<n;x++) printf("%d\n", a[x]);
			if (a[i]>i) {
				int k;
				for (int j=i+1;j<n;j++) if (a[j]<=i) {k=j; break;}
				for (int j=k;j>i;j--) {swap(a[j], a[j-1]); ret++;}
			}
		}
		printf("Case #%d: %d\n", cas, ret);
	}
	return 0;
}
