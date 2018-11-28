#include<cstdio>
#include<cstdlib>

#define AND 1
#define OR 0

#define MAXM 10005

#define INFTY 99999

using namespace std;

struct node {
	bool leaf;
	bool gate;
	bool val;
	bool change;
};

int main() {
	FILE* fin = fopen("A.in","r"), *fout = fopen("A.out","w");
	node nodes[MAXM];
	int dp[MAXM][2];
	int N, M, V;
	fscanf(fin,"%d",&N);
	for(int k = 1; k<=N; k++) {
		fscanf(fin,"%d %d",&M,&V);
		for(int i = 1; i<=(M-1)/2; i++) {
			nodes[i].leaf = 0;
			int G, C;
			fscanf(fin,"%d%d",&G,&C);
			nodes[i].gate=G;
			nodes[i].change=C;
		}
		for(int i = (M+1)/2; i<=M; i++) {
			nodes[i].leaf = 1;
			int V;
			fscanf(fin,"%d",&V);
			nodes[i].val=V;
			dp[i][V]=0;
			dp[i][1-V]=INFTY;
		}
		for(int i = (M-1)/2; i>0; i--) {
			if(nodes[i].gate==AND) {
				dp[i][0] = dp[2*i][0];
				if(dp[2*i+1][0] < dp[i][0]) dp[i][0]=dp[2*i+1][0];
				dp[i][1] = dp[2*i][1] + dp[2*i+1][1];
				if(nodes[i].change) {
					if(dp[2*i][1] + 1 < dp[i][1]) {
						dp[i][1] = dp[2*i][1] + 1;
					}
					if(dp[2*i+1][1] + 1 < dp[i][1]) {
						dp[i][1] = dp[2*i+1][1] + 1;
					}
				}
			} else {
				dp[i][0] = dp[2*i][0] + dp[2*i+1][0];
				dp[i][1] = dp[2*i][1];
				if(dp[2*i+1][1] < dp[i][1]) {
					dp[i][1] = dp[2*i+1][1];
				}
				if(nodes[i].change) {
					if(dp[2*i][0] + 1 < dp[i][0]) {
						dp[i][0] = dp[2*i][0] + 1;
					}
					if(dp[2*i+1][0] + 1 < dp[i][0]) {
						dp[i][0] = dp[2*i+1][0] + 1;
					}
				}
			}
		}
		if(dp[1][V] >= INFTY) {
			fprintf(fout,"Case #%d: IMPOSSIBLE\n",k);
		} else {
			fprintf(fout,"Case #%d: %d\n",k,dp[1][V]);
		}
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
