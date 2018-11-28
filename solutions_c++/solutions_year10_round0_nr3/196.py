#include <iostream>
#include <memory.h>
using namespace std;

long long R, K, N, G[1010];
long long tot[1010], nxt[1010];

long long vis[1010];
long long arr[1010];
long long A, B;

void input() {
	cin >> R >> K >> N;
	for(long long i = 0; i < N; i ++)	cin >> G[i];
}

void init() {
	for(long long i = 0; i < N; i ++) {
		long long sum = 0;
		long long j = i;
		for(; ; ) {
			if(sum + G[j] > K) {
				break;
			}
			sum += G[j];
			
			j = (j + 1) % N;
			if(j == i)	break;
		}
		tot[i] = sum;
		nxt[i] = j;
	}
	/*prlong longf("tot = ");
	for(long long i = 0; i < N; i ++) {
		prlong longf("%d ", tot[i]);
	}
	prlong longf("\n");
	prlong longf("nxt = ");
	for(long long i = 0; i < N; i ++) {
		prlong longf("%d ", nxt[i]);
	}
	prlong longf("\n");
	*/
}

void compute1() {
	memset(vis, 255, sizeof(vis));
	long long pos = 0, idx = 0;
	while(1) {
		if(vis[pos] != -1) {
			A = vis[pos];
			B = idx;
			break;
		}
		arr[idx] = pos;
		vis[pos] = idx;
		
		pos = nxt[pos];
		idx ++;
	}
	//prlong longf("A = %d, B = %d, arr = ", A, B);
	//for(long long i = 0; i < B; i ++)	prlong longf("%d ", arr[i]);
	//prlong longf("\n");
}

long long compute2() {
	long long ans = 0;
	if(R < A) {
		for(long long i = 0; i < R; i ++) {
			ans += tot[arr[i]];
		}
		return ans;
	}
	for(long long i = 0; i < A; i ++) {
		ans += tot[arr[i]];
	}
	
	long long half = 0, all = 0;
	
	R -= A;
	
	for(long long i = 0; i < B-A; i ++) {
		all += tot[arr[A+i]];
		if(i < R%(B-A)) {
			half += tot[arr[A+i]];
		}
	}
	//prlong longf("ans = %d, half = %d, all = %d\n", ans, half, all);
	ans += half;
	ans += R/(B-A) * all;
	return ans;
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	long long t;
	//scanf("%d", &t);
	cin >> t;
	for(long long idx = 1; idx <= t; idx ++) {
		input();
		init();
		compute1();
		long long ans = compute2();
		cout << "Case #" << idx << ": " << ans << endl;
	}
	return 0;
}
