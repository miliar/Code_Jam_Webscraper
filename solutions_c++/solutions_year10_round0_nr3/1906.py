#include <cstdio>

int main(){
	int t, data[2010], next[1009];
	unsigned long long sum[1009], result;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i){
		int r, k, n;
		scanf("%d %d %d", &r, &k, &n);
		for(int j = 0; j < n; ++j){
			scanf("%d", &data[j]);
			data[j + n] = data[j];
			sum[j] = 0;
		}
		for(int j = 0, l; j < n; ++j){
			for(l = j; l < j + n; ++l){
				if(sum[j] + data[l] > k) break;
				sum[j] += data[l];
			}
			next[j] = l < n ? l : l - n;
		}
		result = 0;
		int j = 0;
		while(r--){
			result += sum[j];
			j = next[j];
		}
		printf("Case #%d: %llu\n", i, result);
	}
}
