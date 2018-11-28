#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <cmath>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;

#define SIZE(X) ((int)X.size())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)

typedef long long LL;
typedef pair<int,int> PII;

template<class T> void out(T A[],int n) {cout<<"{"; for (int i=0;i<n;i++){ cout<<A[i];if (i==n-1) cout<<"}"; else cout<<",";} cout<<endl;}
template<class T> void out(T A[],int n, int m) {for(int i=0;i<n;++i) out(A[i],m);}\
template<class T> void out(vector<T> A,int n=-1) {if (n<0 || n>SIZE(A)) n=SIZE(A);cout<<"{";for (int i=0;i<n;i++) {cout<<A[i];if (i==n-1) cout<<"}"; else cout<<",";} cout<<endl;}

const int MAXN = 1024;
const int INF = 1000000000;

LL a[MAXN], A[MAXN], dp[MAXN], X, Y, Z;
int n, m;
void init() {
	for (int i = 0; i < n; ++i) {
		a[i] = A[i%m];
		A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z;
	}
}
int main()
{
	freopen("C-small-attempt2.in","r",stdin);
	freopen("C-small-attempt2.out","w",stdout);
	int N, mod = 1000000007;

	scanf("%d", &N);
	for (int cas = 1; cas <= N; ++cas) {
		scanf("%d %d %lld %lld %lld", &n, &m, &X, &Y, &Z);
		for (int i = 0; i < m; ++i)
			scanf("%d", &A[i]);
		init();
		dp[0] = 1;
		for (int i = 1; i < n; ++i) {
			dp[i] = 1;
			for (int j = 0; j < i; ++j) if (a[i] > a[j])
				dp[i] = (dp[i] + dp[j]) % mod;
		}
		//out(a,n);
		LL ans = 0;
		for (int i = 0; i < n; ++i)
			ans = (ans+dp[i])%mod;
		printf("Case #%d: %lld\n", cas, ans);
	}
	return 0;
}