#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>

typedef long long LL;
const int MAXN = 1024;
int next[MAXN];
LL a[MAXN], sum[MAXN];

int main() {
	//freopen("C-small-attempt0.in","r",stdin);
	//freopen("C-small-attempt0.out","w",stdout);
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T, ca, i, j;
	int R, k, N;
	scanf("%d",&T);
	for (ca = 1 ; ca <= T ; ++ca) {
		scanf("%d%d%d",&R,&k,&N);
		for (i = 0 ; i < N ; i++)
			scanf("%I64d",&a[i]);
		for (i = 0 ; i < N ; i++) {
			LL tmp = a[i];
			for (j = (i+1)%N ; ; ) {
				if (j == i) break;
				if (tmp + a[j] > k) break;
				tmp += a[j];
				j = (j+1) % N;
			}
			next[i] = j;
			sum[i] = tmp;
		}
		//for (i = 0 ; i < N ; i++)
		//	printf("next[%d]:%d sum[%d]:%I64d\n",i,next[i],i,sum[i]);

		int cc = 0;
		LL ans = 0;
		while (R--) {
			ans += sum[cc];
			cc = next[cc];
		}
		printf("Case #%d: ",ca);
		printf("%I64d\n",ans);
	}
	return 0;
}
