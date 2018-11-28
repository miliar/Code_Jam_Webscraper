#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <fstream>
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
template<class T> void out(T A[],int n, int m) {for(int i=0;i<n;++i) out(A[i],m); cout<<endl;}\
template<class T> void out(vector<T> A,int n=-1) {if (n<0 || n>SIZE(A)) n=SIZE(A);cout<<"{";for (int i=0;i<n;i++) {cout<<A[i];if (i==n-1) cout<<"}"; else cout<<",";} cout<<endl;}

const int maxn = 128;
const int inf = 1000000000;
const double eps = 1e-8;
const double pi = acos(-1.0);


long long dp[31];

int main()
{
 	freopen("A-large.in", "r", stdin);
 	freopen("output.txt", "w", stdout);
	dp[1] = 1;
	dp[2] = 3;
	for (int i = 3; i <= 30; ++i)
		dp[i] = 2 * dp[i - 1] + 1;
	int T, n;
	long long k;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas) {
		scanf("%d %lld", &n, &k);
		printf("Case #%d: ", cas);
		if (k < dp[n]) {
			puts("OFF");
			continue;
		}
		int l = 1, r = 100000000, m;
		while (l + 1 < r) {
			m = (l + r) / 2;
			long long cur = dp[n] * m + m - 1;
			if (cur <= k)
				l = m;
			else
				r = m;
		}
		if (dp[n] * l + l - 1 == k) {
			puts("ON");
		}
		else
			puts("OFF");
	}
	return 0;
}
