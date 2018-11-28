#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <map>
#include <set>

using namespace std;

#define MAXN 5000000

long long T, m, X, Y, Z, n;
long long seka[MAXN];
long long A[MAXN];
long long dp[MAXN];

int main() {
	freopen("csmall.in", "r", stdin);
	freopen("csmall.out", "w", stdout);
	scanf("%d", &T);
	for (int e = 0; e < T; e++) {
		scanf("%lld %lld %lld %lld %lld", &n, &m, &X, &Y, &Z);
		for (int j = 0; j < m; j++)  
			scanf("%lld", &A[j]);
		for (long long i = 0; i < n; i++)	{
			seka[i] = A[i % m];
			A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z;
// 			cout << seka[i] << " ";
			dp[i] = 0;
		}
// 		cout << endl;
		long long suma = 0;
		for (int x = 0; x < n; x++) {
			dp[x]++;
			for (int y = 0; y < x; y++)
				if (seka[y] < seka[x]) dp[x] = (dp[x] + dp[y]) % 1000000007;
			suma = (suma + dp[x]) % 1000000007;
		}	
		printf("Case #%d: %lld\n", e + 1, suma);	
	}
	return 0;
}