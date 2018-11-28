#include<iostream>
#include<cstring>
#include<map>
#include<algorithm>
#include<stack>
#include<queue>
#include<cmath>
#include<string>
#include<cstdlib>
#include<vector>
#include<cstdio>
#include<set>
#include<list>
#include<numeric>
#include<cassert>
#include<ctime>
#include<bitset>

using namespace std;

const int MAXN = 1024;

double D[MAXN], F[MAXN], E[MAXN];
double p[MAXN][MAXN], dp[MAXN][MAXN];

void init() 
{
	D[0] = 1.0;
	D[1] = 0.0;
	F[0] = 1.0;
	F[1] = 1.0;
	for (int i = 2; i < MAXN; i ++) {
		D[i] = (i-1) * (D[i-1] + D[i-2]);
		F[i] = F[i-1] * i;
	}
	E[0] = 0;
	E[1] = 0;
	for (int n = 2; n < MAXN; n++) {
		E[n] = 1.0;
		double p = 0;
		for (int i = 0; i <= n; i++) {
			dp[n][i] = D[n-i]/F[i]/F[n-i];
			if(i) {
				E[n] += dp[n][i]*E[n-i];
				p += dp[n][i];
			}
			//cout<<"dp[n][i] "<<n<<" "<<i<<" "<<dp[n][i]<<" "<<E[n-i]<<endl;
		}
		E[n] /= p;
		cout<<n<<" "<<E[n]<<" "<<p<<endl;
	}
}

int a[MAXN];
bool vi[MAXN];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("in","r",stdin);
	freopen("out","w",stdout);
#endif

	//init();
	//E[n] = n
	//E[1] = 0
	int T, n, t = 1;
	for (scanf("%d", &T); T--; ) {
		scanf("%d", &n);
		for (int i = 1; i <= n; i ++) {
			scanf("%d", &a[i]);
		}
		fill(vi+1, vi+1+n, false);
		double ans = 0;
		for (int i = 1; i <= n; i++) {
			int p = i, cnt = 0;
			while (!vi[p]) {
				vi[p] = true;
				cnt ++;
				p = a[p];
			}
			if(cnt > 1) {
				ans += cnt;
			}
			//cout<<cnt<<endl;
		}
		printf("Case #%d: %.6f\n", t++, ans);
	}
	
	return 0;
}