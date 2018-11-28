#include<iostream>
using namespace std;

typedef long long ll;
ll l, n, t, c;
ll input[10010];
ll dis[10010];
ll sum[10010];

int main(){
	int cas;
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &cas);
	for(int tt = 0; tt < cas; tt++){
		scanf("%lld%lld%lld%lld", &l, &t, &n, &c);
		for(int i = 0; i < c; i++)
			scanf("%lld", &input[i]);
		for(int i = 0; i < n; i++){
			if(i >= c) dis[i] = dis[i - c];
			else dis[i] = input[i];
		}
		ll res = 0x3f3f3f3f;
		sum[0] = 0; sum[1] = dis[0];
		for(int i = 2; i < n + 1; i++){
			sum[i] = sum[i - 1] + dis[i - 1];
		}
		if(l >= 0){
			if(res > sum[n] * 2) res = sum[n] * 2;
		}
		if(l >= 1){
			for(int i = 0; i < n; i++){
				ll tp = 0;
				tp += (sum[i] - sum[0]) * 2;
				if(t <= tp) tp += (sum[i + 1] - sum[i]);
				else if(t <= tp + (sum[i + 1] - sum[i]) * 2)
					tp = t + sum[i + 1] - sum[0] - t / 2;
				else tp += (sum[i + 1] - sum[i]) * 2;
				tp += (sum[n] - sum[i + 1]) * 2;
				if(res > tp) res = tp;
			}
		}
		if(l >= 2){
			for(int i = 0; i < n; i++){
				for(int j = i + 1; j < n; j++){
					ll tp = 0;
					tp += (sum[i] - sum[0]) * 2;
					if(t <= tp) tp += (sum[i + 1] - sum[i]);
					else if(t <= tp + (sum[i + 1] - sum[i]) * 2)
						tp = t + sum[i + 1] - sum[0] - t / 2;
					else tp += (sum[i + 1] - sum[i]) * 2;
					tp += (sum[j] - sum[i + 1]) * 2;
					if(t <= tp) tp += (sum[j + 1] - sum[j]);
					else if(t <= tp + (sum[j + 1] - sum[j]) * 2)
						tp = t + sum[j + 1] - sum[0] - t / 2;
					else tp += (sum[j + 1] - sum[j]) * 2;
					tp += (sum[n] - sum[j + 1]) * 2;
					if(res > tp) res = tp;
				}
			}
		}
		printf("Case #%d: %lld\n", tt + 1, res);
	}
	return 0;
}