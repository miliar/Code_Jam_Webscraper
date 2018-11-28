#define maxn 55
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

struct Ttx{
	int cnt;
	bool crs;
};

int n, k, b, t;


int x[maxn], v[maxn];
Ttx tx[maxn];

void init(){
	scanf("%d%d%d%d", &n, &k, &b, &t);
	for (int i=0; i<n; i++) scanf("%d", &x[i]);
	for (int i=0; i<n; i++) scanf("%d", &v[i]); 
}

bool cmp(const Ttx &a, const Ttx &b){
	return (a.cnt < b.cnt);
}

void solve(){
	memset(tx, 0, sizeof tx);
	for (int i=0; i<n; i++) if (x[i]+t*v[i] >= b) tx[i].crs = true;
	for (int i=0; i<n; i++){
		for (int j=0; j<n; j++){
			if (tx[j].crs) continue;
			if (x[j] < x[i]) continue;
			if (v[j] > v[i]) continue;
			if (x[j]-x[i]>=t*(v[i]-v[j])) continue;
			tx[i].cnt++;
		}
	}
	sort(tx, tx+n, cmp);
	int ans = 0;
	for (int i=0; i<n&&(k!=0); i++){
		if (!tx[i].crs) continue;
		ans+=tx[i].cnt;
		k--;
	}
	if (k!=0) printf("IMPOSSIBLE\n");
	else printf("%d\n", ans);
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
