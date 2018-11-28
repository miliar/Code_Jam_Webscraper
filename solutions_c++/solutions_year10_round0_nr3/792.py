#include <cstdio>

const int MAXN = 1001;

int ncas, cas = 0, r, k, n;
long long total;
long long queue[MAXN], sum[MAXN], go[MAXN];

int main(){
	scanf("%d", &ncas);
	while (ncas--){
		scanf("%d %d %d", &r, &k, &n);
		for (int i = 0; i < n; ++i)
			scanf("%lld", &queue[i]);
		for (int i = 0, j; i < n; ++i){
			sum[i] = queue[i];
			j = (i+1)%n;
			go[i] = j;
			while (j != i && sum[i] + queue[j] <= k){
				sum[i] += queue[j];
				j = (j+1)%n;
				go[i] = j;
			}
		}
		total = 0;
		int pos = 0;
		while (r--){
			total += sum[pos];
			pos = go[pos];
		}
		printf("Case #%d: %lld\n", ++cas, total);
	}
	return 0;
}
