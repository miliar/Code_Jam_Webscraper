#include<iostream>
#include<algorithm>
using namespace std;

const int N = 1005;
long long num[N * 2], next[N];

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int T, K, R, n;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; ++cas){
		scanf("%d%d%d", &R, &K, &n);
		for(int i = 1; i <= n; ++i){
			scanf("%lld", &num[i]);
			num[i + n] = num[i];
		}
		num[0] = 0;
		for(int i = 1; i <= n * 2; ++i)
			num[i] += num[i - 1];
		for(int i = 1; i <= n; ++i){
			next[i] = upper_bound(num + i, num + i + n, K + num[i - 1]) - num;
		}
		int cur = 1;
		long long res = 0;
		for(int i = 0; i < R; ++i){
			res += num[next[cur] - 1] - num[cur - 1];
			cur = next[cur];
			if(cur > n) cur -= n;
		}
		printf("Case #%d: %lld\n", cas, res);
	}
	return 0;
}