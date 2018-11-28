#define _CRT_SECURE_nO_WARnInGS
#pragma comment (linker, "/STACK:16777216")
#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <fstream>
#include <math.h>
#include <limits>
#include <set>
#include <map>
#include <sstream>
#include <stdio.h>
#include <time.h>
#include <memory.h>
#include <cassert>
#include <complex>
using namespace std;

///////////////// macros and typedefs ///////////////////
#define rep(i, n) for (int i = 0, _n = (n); i < _n; ++i)
#define repd(i, n) for (int i = (n)-1; i >= 0; --i)
#define _fill(a, x) memset((a), (x), sizeof((a)))
#define DEB(k) cerr<<"debug: "#k<<"="<<k<<endl;
#define all(c) (c).begin(), (c).end()
#define mp(a, b) make_pair(a, b)
#define l(c) (int)((c).size())
#define sqr(a) ((a)*(a))
#define inf 0x7f7f7f7f
#define pb push_back
#define ppb pop_back
#define x first
#define y second
typedef long long ll;
typedef vector<int> vi;
typedef vector<double> vd;
typedef pair<int,int> pi;

int n;
int lo;
int dp[10007];
pi CC[10000];

void solveCase(int tc) {
    printf("Case #%d: ", tc+1);
	scanf("%d", &n);
    rep(i, n)
        scanf("%d %d", &CC[i].x, &CC[i].y);
    scanf("%d", &lo);
	sort(CC, CC+n);
    rep(i, 10007) dp[i] = -1;
	dp[0] = CC[0].x;
    rep(i, n)
		for (int j = i+1; j < n; j++)
			if (dp[i]+CC[i].x >= CC[j].x)
				dp[j] = max(dp[j], min(CC[j].y, CC[j].x-CC[i].x));
	rep(i, n)
        if (CC[i].x+dp[i] >= lo) {
			puts("YES");
			return;
        }
    puts("NO");
}

void solution()
{
    int tc;
    scanf("%d", &tc);
    rep(i, tc)
        solveCase(i);
}

int main()
{
#ifdef MY_JUDGE
    freopen("A-large.in", "rt", stdin);
    freopen("A-large.out", "wt", stdout);
#endif
    solution();
#ifdef MY_JUDGE
    double time = clock()*1./CLOCKS_PER_SEC;
    fprintf(stderr, "Time: %.2lf sec\n", time);
#endif
    return 0;
} 