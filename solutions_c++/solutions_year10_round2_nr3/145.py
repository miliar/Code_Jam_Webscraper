#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>
using namespace std;

ifstream fin("c.in");
ofstream fout("c.out");

typedef long long ll;

#define MOD 100003LL

ll dp[512][512];

ll ch[512][512];

ll f(int n, int fr) {
	if(dp[n][fr]!=-1LL)return dp[n][fr];
	if(n==1) {
		dp[n][fr] = 1LL;
		return 1LL;
	}
	int i,j;
	ll ret = 0LL;
	for(j=0;j<=fr;++j) {
		i = n - 1 - j;
		if(i>=1) {
			ret = ret + ch[fr][j]*f(i,n-i-1);
			ret %= MOD;
		}
	}
	dp[n][fr] = ret;
	return ret;
}

ll solve(int n) {
	ll ret=0;
	memset(dp,-1LL,sizeof dp);
	int i;
	for(i=1;i<n;++i) {
		//cout<<i<<" "<<n-i-1<<" "<<f(i,0)<<endl;
		ret += f(i,n-i-1);
		ret %= MOD;
	}
	return ret;
}

void init() {
	ch[0][0] = 1LL;
	int n,k;
	for(n=1;n<=500;++n) {
		ch[n][0] = 1LL;
		ch[n][n] = 1LL;
		for(k=1;k<n;++k) {
			ch[n][k] = (ch[n-1][k-1]+ch[n-1][k])%MOD;
		}
	}
}

int main() {
	int tests;
	fin>>tests;
	int testNum;
	int n;
	init();
	for(testNum=1;testNum<=tests;++testNum) {
		fin>>n;
		ll ret = solve(n);
		fout<<"Case #"<<testNum<<": "<<ret<<endl;
	}
	return 0;
}
