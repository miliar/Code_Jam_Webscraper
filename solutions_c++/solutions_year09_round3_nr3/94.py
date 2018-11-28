#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<map>
#include<cctype>
#include<cstdlib>
#include<queue>
#include<sstream>
#include<cmath>

using namespace std;

#define fo(a,b) for(a=0;a<b;a++)
#define re return
#define co continue
#define sf scanf
#define pf printf

int inf = 1000000000;
int P, Q;
vector<int> V;

int dp[104][104];
int n;

int memo(int a, int b) {
	if( a + 1 == b ) return 0;
	if( dp[a][b] != -1 ) return dp[a][b];

	int res = inf;
	int i;
	for(i=a+1;i<b;i++) {
	   int k = V[i] - V[a] - 1;
	   k += V[b] - V[i] - 1;
	   k += memo(a, i) + memo(i, b);
	   res <?= k;
	}
	re dp[a][b] = res;
}

int main() {
    freopen("c2.in","r",stdin);
    freopen("c2.out","w",stdout);
	int t, cases = 1;
	for( sf("%d", &t); t--; ) {
		cin >> P >> Q;
		int i, j;
		V.clear();
		fo(i, Q) {
		  int a; cin >> a;
		  V.push_back(a);
		}
		V.push_back(0);
		V.push_back(P+1);
		sort(V.begin(), V.end() );

		n = V.size();

		for(i=0;i<=n;i++)
		 for(j=0;j<=n;j++)
		  dp[i][j] = -1;

		int res = memo(0,n-1);


		pf("Case #%d: %d\n", cases++, res);
	}
	return 0;
}
