#include<cstdio>
#include<string.h>
#include<algorithm>
using namespace std;

int main(){
	int T, c;
	scanf("%d", &T);
	c = 0;
	while (T--){
		int n;
		long long int ans, a[1000], b[1000];
		ans = 0;
		scanf("%d", &n);
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		for (int i=0; i<n; i++) scanf("%lld", &a[i]);
		for (int i=0; i<n; i++) scanf("%lld", &b[i]);
		sort(a, a+n);
		sort(b, b+n);
		int k = n-1;
		int l=-1;
		for (int i=0; i<n; i++)
			if (a[i] <= 0){
//				printf("%lld %lld\n", a[i], b[k]);
				ans += a[i] * b[k];
				k--;
			}else {
				l = i;
				break;
			}
		if (l!=-1){
			int p = 0;
			for (int j=n-1; j>=l; j--){
//				printf("%lld %lld\n", a[j], b[p]);
				ans += a[j] * b[p];
				p++;
			}
		}
		printf("Case #%d: %lld\n", ++c, ans);
	}
	return 0;
}
