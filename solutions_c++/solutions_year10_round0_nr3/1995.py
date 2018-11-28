#include <cstdio>
#include <string.h>

int main(){
	int T, ca = 0;
	scanf("%d", &T);
	while (T--){
		int r, k, n, a[1010], val[1010], next[1010];
		bool vis[1010];
		memset(next, 0, sizeof(next));
		scanf("%d%d%d", &r, &k, &n);
		for (int i=0; i<n; i++)
			scanf("%d", &a[i]);

		for (int i=0; i<n; i++){
			int sum = 0;
			int j=i;
			memset(vis, 0, sizeof(vis));
			while (!vis[j] && sum+a[j] <= k){
				vis[j] = true;
				sum += a[j];
				j = (j+1) % n;
			}
			next[i] = j;
			val[i] = sum;
//			printf("%d: %d %d\n", i, next[i], val[i]);
		}

		int t=0;
		memset(vis, 0, sizeof(vis));
		while (!vis[t]){
			vis[t] = true;
			t = next[t];
		}

		int time = 1, o = next[t];
		long long sum=val[t];
		while (o != t){
			sum += val[o];
			o = next[o];
			time++;
		}

	//	printf("time %d, t %d, sum %d\n", time, t, sum);

		long long ans = 0;
		o = 0;
		while (o != t){
			ans += val[o];
			o = next[o];
			if (--r == 0) break;
		}
		//printf("before %d %d\n", ans, r);
		
		if (r){
			ans += (long long)(r/time) * sum;
			r %= time;
			if (r){
				o = t;
				while (r--){
					ans += val[o];
					o = next[o];
				}
			}
		}

		printf("Case #%d: %lld\n", ++ca, ans);
	}
	return 0;
}

