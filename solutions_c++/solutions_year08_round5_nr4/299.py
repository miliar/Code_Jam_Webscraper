#include <cstdio>
#include <algorithm>

using namespace std;

const int MOD=10007;

int cases;

int dp[105][105];
bool bad[105][105];

int R,C,rock,a,b;

int main() {
	FILE * fin=fopen("D.in","r");
	FILE * fout=fopen("D.out","w");
	
	fscanf(fin,"%d ",&cases);
	for(int h=0;h<cases;h++) {
		memset(dp,0,sizeof(dp));
		memset(bad,0,sizeof(bad));
		fscanf(fin,"%d %d %d ",&R,&C,&rock);
		for(int i=0;i<rock;i++) {
			fscanf(fin,"%d %d ",&a,&b);
			bad[a][b]=true;
		}
		dp[1][1]=1;
		for(int i=1;i<=R;i++) {
			for(int j=1;j<=C;j++) {
				if (i==1 && j==1) {continue;}
				if (bad[i][j]) {continue;}
				if (i>=3 && j>=2) {dp[i][j]+=dp[i-2][j-1];}
				if (i>=2 && j>=3) {dp[i][j]+=dp[i-1][j-2];}
				dp[i][j]%=MOD;
			}
		}

		fprintf(fout,"Case #%d: %d\n",h+1,dp[R][C]);
	}

	return 0;
}
