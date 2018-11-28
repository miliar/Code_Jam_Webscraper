#include <stdio.h>
#include <string.h>

int a[2000];
int next[1000];
int money[1000];
int v[1000];
long long e[1000];

int main(){
	int T;
	scanf("%d", &T);
	for(int TT = 1; TT <= T; TT++){
		int r,k,n;
		scanf("%d%d%d", &r, &k, &n);
		for(int i = 0; i < n; i++){
			scanf("%d", &a[i]);
			a[i+n] = a[i];
		}
		for(int i = 0; i < n; i++){
			int sum = 0, j;
			for(j=i;j<n+i;j++){
				sum += a[j];
				if(sum > k){
					sum -= a[j];
					break;
				}
			}
			next[i] = j % n;
			money[i] = sum;
		}
		memset(v,-1,sizeof(v));
		int now = 0;
		long long ret = 0;
		for(int i=0;i<r;i++){
			if(v[now] == -1){
				v[now] = i;
				ret += money[now];
				now = next[now];
				if(i<1000)
					e[i] = ret;
			}else{
				long long node = e[i-1] - e[v[now]] + money[now];
				long long times = (r-i) / (i-v[now]);
				ret += node * times;
				i = i + times * (i-v[now])-1;
				memset(v,-1,sizeof(v));
			}
		}
		printf("Case #%d: %lld\n", TT, ret);
	}
}