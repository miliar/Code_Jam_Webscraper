#include <iostream>

using namespace std;

int p,n;
int m[1<<10];
int g[10][1024];

int dp[11][1024][11];

int solve(int r, int id, int k) {
	if (dp[r][id][k]!=-1) return dp[r][id][k];
	int rez=-2, ok=1;
	int range=(1<<(p-r));
	int left=id*range, right=left+range-1;
	for (int i=left;i<=right;i++) {
		if (k>m[i]) { ok=0; break; }
	}
	if (ok) {
		if (r<p) {
			//buy ticket
			int c1=0, c2=0;
			c1=solve(r+1,id*2,k);
			c2=solve(r+1,id*2+1,k);
			if (c1!=-2 && c2!=-2) {
				if (rez==-2 || c1+c2+g[r][id]<rez) rez=c1+c2+g[r][id];
			}
			//skip this game
			c1=solve(r+1,id*2,k+1);
			c2=solve(r+1,id*2+1,k+1);
			if (c1!=-2 && c2!=-2) {
				if (rez==-2 || c1+c2<rez) rez=c1+c2;
			}
		} else {
			rez=0;
		}
	}
	dp[r][id][k]=rez;
	return rez;
}

int main() {
	//freopen("football.in","r",stdin);
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int tests;
	scanf("%d",&tests);
	for (int test=1;test<=tests;test++) {
		cerr << test << endl;
		scanf("%d",&p);
		n=1<<p;
		for (int i=0;i<n;i++) scanf("%d",&m[i]);
		for (int i=p-1;i>=0;i--) {
			for (int j=0;j<(1<<i);j++) {
				scanf("%d",&g[i][j]);
			}
		}
		memset(dp,-1,sizeof(dp));
		printf("Case #%d: %d\n",test,solve(0,0,0));
	}
    return 0;
}
