#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;
#define	out(x)	(cout << #x << ": " << x << endl)
template<class T>void show(T a, int l){for(int i = 0; i < l; ++i)cout << a[i] << ' '; cout << endl;}
template<class T>void show(T a, int l, int r){for(int i = 0; i < l; ++i)show(a[i], r); cout << endl;}
typedef long long LL;
const int MAXN = 1010;
int T, R, K, N, g[MAXN], vis[MAXN];
LL sum[MAXN*10];

LL solve(){
	int i, j, p;
	LL ans = 0, tot = 0;
	fill(vis, vis+N, -1);
	for(i = p = 0; i < R; ++i){	
		if(vis[p] != -1){
		//	out(vis[p]);
			int t = i-vis[p];
			int a = (R-1-i+1)%t, b = (R-1-i+1)/t;
		//	printf("(i=%d, %d,%d,%d)\n", i, t, a, b);
			tot = 0;
			if(b > 0){
				for(j = vis[p]; j < i; ++j)
					tot += sum[j];
				tot *= b;
		//		printf("b>0 tot=%I64d\n", tot);
			}
			for(j = vis[p]; j < vis[p]+a; ++j)
				tot += sum[j];
		//	printf("tot=%I64d\n", tot);
			ans += tot;
			return ans;
		}
		sum[i] = 0;
		vis[p] = i;			
		while(sum[i]+g[p] <= K){
			sum[i] += g[p];
			p = (p+1)%N; 
		}
		ans += sum[i];
	}
	return ans;
}

int main(){
	freopen("C-large.in", "r" , stdin);	freopen("outlarge.txt", "w", stdout);
	scanf("%d", &T);
	for(int ks = 1; ks <= T; ++ks){
		scanf("%d%d%d", &R, &K, &N);
		int i, j;
		LL sum = 0;
		for(i = 0; i < N; ++i){
			scanf("%d", &g[i]);
			sum += g[i];
		}
		printf("Case #%d: ", ks);
		if(sum <= K){
			printf("%I64d\n", sum*R);
			continue;
		}
		printf("%I64d\n", solve());
	}
	return 0;
}
