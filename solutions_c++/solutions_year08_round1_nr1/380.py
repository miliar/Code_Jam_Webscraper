#include<stdio.h>
#include<algorithm>
#include<functional>
using namespace std;

int l1[800], l2[800];
int main() {
	int T;
	scanf("%d", &T);
	for(int cas=1;cas<=T;cas++) {
		int n;
		scanf("%d", &n);
		for(int i=0;i<n;i++) scanf("%d", l1+i);
		for(int i=0;i<n;i++) scanf("%d", l2+i);
		sort(l1, l1+n);
		sort(l2, l2+n, greater<int>());
		long long res=0;
		for(int i=0;i<n;i++) res+=l1[i]*l2[i];
		printf("Case #%d: %lld\n", cas, res);
	}
	return 0;
}