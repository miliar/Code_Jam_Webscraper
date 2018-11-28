#include<cstdio>
#include<cstring>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include <list>
#include<queue>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int dp[10005][2];
int N,M,V,G[10005],C[10005],val[10005];

int rec(int a,int b) {
	if(dp[a][b] != -1) return dp[a][b];
	dp[a][b] = (1 << 29);
	int a1 = rec(2*a,1);
	int a0 = rec(2*a,0);
	int b1 = rec(2*a+1,1);
	int b0 = rec(2*a+1,0);
	if(G[a] == 1 && C[a] == 1) {
		if(b == 0) {
			if(a0 == (1<<29) && b0 == (1<<29)) dp[a][b] = (1 << 29);
			else {
				int c1 = (a0 + b1),c2 = (a0 + b0), c3 = (a1 + b0);
				dp[a][b] = min(dp[a][b],min(c1,min(c2,c3)));
			}
		}
		else {
			if(a1 == (1<<29) && b1 == (1<<29)) dp[a][b] = (1 << 29);
			else {
				int c1 = (a0 + b1)+1,c2 = (a1 + b1), c3 = (a1 + b0)+1;
				dp[a][b] = min(dp[a][b],min(c1,min(c2,c3)));
			}
		}
	}
	else if(G[a] == 1 && C[a] == 0) {
		if(b == 0) {
			if(a0 == (1<<29) && b0 == (1<<29)) dp[a][b] = (1 << 29);
			else {
				int c1 = (a0 + b1),c2 = (a0 + b0), c3 = (a1 + b0);
				dp[a][b] = min(dp[a][b],min(c1,min(c2,c3)));
			}
		}
		else {
			if(a1 == (1<<29) && b1 == (1<<29)) dp[a][b] = (1 << 29);
			else dp[a][b] = (a1 + b1);
		}
	}
	else if(G[a] == 0 && C[a] == 1) {
		if(b == 0) {
			if(a0 == (1<<29) && b0 == (1<<29)) dp[a][b] = (1 << 29);
			else {
				int c1 = (a0 + b1)+1,c2 = (a0 + b0), c3 = (a1 + b0)+1;
				dp[a][b] = min(dp[a][b],min(c1,min(c2,c3)));
			}
		}
		else {
			if(a1 == (1<<29) && b1 == (1<<29)) dp[a][b] = (1 << 29);
			else {
				int c1 = (a0 + b1),c2 = (a1 + b1), c3 = (a1 + b0);
				dp[a][b] = min(dp[a][b],min(c1,min(c2,c3)));
			}
		}
	}
	else if(G[a] == 0 && C[a] == 0) {
		if(b == 0) {
			if(a0 == (1<<29) && b0 == (1<<29)) dp[a][b] = (1 << 29);
			else dp[a][b] = (a0 + b0);
		}
		else {
			if(a1 == (1<<29) && b1 == (1<<29)) dp[a][b] = (1 << 29);
			else {
				int c1 = (a0 + b1),c2 = (a1 + b1), c3 = (a1 + b0);
				dp[a][b] = min(dp[a][b],min(c1,min(c2,c3)));
			}
		}
	}
	dp[a][b] = min(dp[a][b],(1<<29));
	return dp[a][b];
}

int main() {
	scanf("%d\n",&N);
	for(int ii=1;ii<=N;++ii) {
		scanf("%d %d\n",&M,&V);
		for(int i = 1;i<=(M-1)/2;++i) scanf("%d %d\n",G+i,C+i);
		for(int i=0;i<=M;++i) dp[i][0] = dp[i][1] = -1;
		for(int i = (M-1)/2+1;i<=M;++i) {
			scanf("%d\n",val+i);
			if(val[i] == 0) dp[i][0] = 0, dp[i][1] = (1 << 29);
			else dp[i][0] = (1 << 29), dp[i][1] = 0;
		}
		int ans = rec(1,V);
		if(ans == (1 << 29)) printf("Case #%d: IMPOSSIBLE\n",ii);
		else  printf("Case #%d: %d\n",ii,ans);
	}
	return 0;
}
