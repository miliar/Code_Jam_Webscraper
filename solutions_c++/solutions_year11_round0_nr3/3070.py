#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
#define forn(i,n) for (int i = 0; i < (int)(n); i++)
#define forv(i,a) for (int i = 0; i < a.size(); i++)
#define sz size()
#define mp make_pair
#define pb push_back
#define VI vector< int >
#define PII pair< int, int>
#define inf (100000000)
#define all(a) a.begin(),a.end()
#define have(msk, i) (!!((1<<(i)) & msk))
#define pi 3.1415926535897932384626433832795
#define sqr(a) ((a) * (a))
#define eps 1e-9
using namespace std;

map< int, int > dp[2000];
int a[2000];
void solve(int testNumber) {
	forn(i,2000)dp[i].clear();

	int n;
	cin >> n;
	forn(i,n)cin >> a[i];
	
	int xor = 0;
	forn(i,n)xor^=a[i];


	if (xor) {
		printf("Case #%d: NO\n", testNumber);
		return;
	}

	dp[0][a[0]] = a[0];
	dp[0][0] = 0;

	for (int i = 1; i < n; i++) {
		for (map< int, int >::iterator it = dp[i-1].begin(); it != dp[i-1].end(); it++) {
			dp[i][it->first] = max(dp[i][it->first], it->second);
			dp[i][(it->first) ^ a[i]] = max(dp[i][(it->first) ^ a[i]], it->second + a[i]);
		}
	}
	int ans = 0;
	for (map< int, int >::iterator it = dp[n-1].begin(); it != dp[n-1].end(); it++) {
		if (it->first != 0)
			ans = max(ans, (int)it->second);
	}
	printf("Case #%d: %d\n", testNumber, ans);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t;
	scanf("%d", &t);

	forn(i, t) {
		solve(i+1);
	}

	return 0;
}
