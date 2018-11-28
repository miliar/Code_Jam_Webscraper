#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <memory.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
int main() {
	//freopen ("C-small.in", "r", stdin);
	//freopen ("C-small.out", "w", stdout);
	int jtc;
	scanf("%d", &jtc);
	for (int tc = 0; tc < jtc; tc++) {
		int R, K, N;
		int i;
		scanf("%d %d %d", &R, &K, &N);
		vector <ll> data;
		ll tot = 0;
		for (i = 0; i < N; i++) {
			ll a;
			scanf("%lld", &a);
			data.pb(a);
			tot += a;
		}
		int pos = 0;
		ll hasil = 0;
		for (i = 0; i < R; i++) {
			ll sum = 0;
			while (sum + data[pos] <= tot && sum + data[pos] <= K) {
				sum += data[pos++];
				pos %= N;
			}
			hasil += sum;
		}
		printf("Case #%d: %lld\n", tc + 1, hasil);
	}
	//fclose(stdin);
	//fclose(stdout);
	return 0;
}
