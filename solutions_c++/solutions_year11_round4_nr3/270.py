#include<cstdio>
int T;
long long N, prm[100001];
int pc, isp[1000001], now[100001];
void pre(){
	for(int i = 2; i <= 1000; i++)
		if(!isp[i]){
			prm[pc++] = i;
			for(int j = i * i; j <= 1000000; j += i)
			    isp[j] = 1;
		}
	for(int i = 1001; i <= 1000000; i++)
		if(!isp[i])
		    prm[pc++] = i;
	return;
}
int main(){
	//freopen("C-small-2.in", "r", stdin);
	//freopen("C-small02.out", "w", stdout);
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	scanf("%d", &T);
	pre();
	for(int t = 1; t <= T; t++){
		scanf("%I64d", &N);
		if(N == 1){
			printf("Case #%d: %d\n", t, 0);
			continue;
		}else if(N <= 3){
			printf("Case #%d: %d\n", t, 1);
			continue;
		}
		long long ans = 0;
		for(int i = 0; i < pc && prm[i] * prm[i] <= N; i++){
			long long tmp = prm[i] * prm[i];
			while(tmp <= N){
				ans++;
				tmp *= prm[i];
			}
		//	printf("%I64d\n", ans);
		}
		printf("Case #%d: %I64d\n", t, ans + 1);
	}
}

