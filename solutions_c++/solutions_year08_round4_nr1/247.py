#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN=10005,INF=10000000;
int cases;
int n,root;

bool cheat[MAXN];int cht;
int tree[MAXN];
int dp[MAXN][2];

void solve(int v) {
	if (4*v<n+1) {solve(2*v);}
	if (4*v+2<n+1) {solve(2*v+1);}
	
	if (tree[v]==1) {
		dp[v][1]<?=(dp[2*v][1]+dp[2*v+1][1]);
		dp[v][0]<?=(dp[2*v][1]+dp[2*v+1][0]);
		dp[v][0]<?=(dp[2*v][0]+dp[2*v+1][0]);
		dp[v][0]<?=(dp[2*v][0]+dp[2*v+1][1]);
	}
	else {
		dp[v][1]<?=(dp[2*v][1]+dp[2*v+1][1]);
		dp[v][1]<?=(dp[2*v][1]+dp[2*v+1][0]);
		dp[v][0]<?=(dp[2*v][0]+dp[2*v+1][0]);
		dp[v][1]<?=(dp[2*v][0]+dp[2*v+1][1]);			
	}		
	
	if (cheat[v]) {
		if (tree[v]==0) {
			dp[v][1]<?=(dp[2*v][1]+dp[2*v+1][1]+1);
			dp[v][0]<?=(dp[2*v][1]+dp[2*v+1][0]+1);
			dp[v][0]<?=(dp[2*v][0]+dp[2*v+1][0]+1);
			dp[v][0]<?=(dp[2*v][0]+dp[2*v+1][1]+1);
		}
		else {
			dp[v][1]<?=(dp[2*v][1]+dp[2*v+1][1]+1);
			dp[v][1]<?=(dp[2*v][1]+dp[2*v+1][0]+1);
			dp[v][0]<?=(dp[2*v][0]+dp[2*v+1][0]+1);
			dp[v][1]<?=(dp[2*v][0]+dp[2*v+1][1]+1);			
		}		
	}
}

int main() {
	FILE * fin=fopen("A.in","r");
	FILE * fout=fopen("A.out","w");
	
	fscanf(fin,"%d ",&cases);
	for(int h=0;h<cases;h++) {
		memset(cheat,0,sizeof(cheat));
		fill(dp[0],dp[MAXN-1]+2,INF);
		fscanf(fin,"%d %d ",&n,&root);
		for(int i=1;i<=(n-1)/2;i++) {
			fscanf(fin,"%d %d ",&tree[i],&cht);
			if (cht==1) {cheat[i]=true;}
		}
		for(int i=(n+1)/2;i<=n;i++) {
			fscanf(fin,"%d ",&tree[i]);
			dp[i][tree[i]]=0;
		}
		solve(1);	
		fprintf(fout,"Case #%d: ",h+1);
		if (dp[1][root]>=INF) {
			fprintf(fout,"IMPOSSIBLE\n");
		}
		else {
			fprintf(fout,"%d\n",dp[1][root]);
		}
	}

	return 0;
}
