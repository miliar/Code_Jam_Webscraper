#define ll long long
#define maxn 1010
#include <iostream>
#include <stdio.h>
using namespace std;

int r, k, n;
int g[maxn], ans[maxn];
ll sum=0, ansi[maxn];

void init(){
	scanf("%d%d%d", &r, &k, &n);
	sum = 0;
	for (int i=0; i<n; i++) {
		scanf("%d", &g[i]);
		sum += g[i];
	}
}

void solve(){
	int p=0;
	ll res = 0;
	if (sum <= k){
		printf("%lld\n", sum*r);
		return;
	}
	memset(ans, 0xff, sizeof ans);
	ans[0] = 0; ansi[0] = 0;
	for (int i=1; i<=r; i++){
		int tmp = 0;
		while (1){
			if (tmp+g[p]>k) break;
			tmp+=g[p++];
			p%=n; 
		}
//		cout<<"times:"<<i<<"  pos:"<<p<<"  cost:"<<tmp<<endl;
		if (ans[p] == -1){
			ans[p] = i;
			ansi[i] = ansi[i-1] + tmp;
		} else {
			ansi[i] = ansi[i-1] + tmp;
			res = ansi[ans[p]];
			r -= ans[p];
			int t = r/(i - ans[p]);
			res += (ll)(ansi[i]-ansi[ans[p]]) * t;
			int rem = r%(i - ans[p]);
			res += ansi[ans[p]+rem] - ansi[ans[p]];
			printf("%lld\n", res);
			return;
		}
	}
	printf("%lld\n", ansi[r]);
}

int main(){
	int test; scanf("%d", &test);
	for (int cas=1; cas<=test; cas++){
		init();
		printf("Case #%d: ", cas);
		solve();
	}
	return 0;
}
