#include<cstdio>
#include<cstdlib>

#define MAXH 200
#define MAXW 200
#define MODULUS 10007

using namespace std;

int main() {
	FILE *fin = fopen("D.in","r"), *fout = fopen("D.out","w");
	int N,R,H,W;
	int dp[MAXH][MAXW], rock[MAXH][MAXW];
	fscanf(fin,"%d",&N);
	for(int k = 1; k<=N; k++) {
		fscanf(fin,"%d%d%d",&H,&W,&R);
		for(int i = 0; i<MAXH; i++)
			for(int j = 0; j<MAXW; j++)
				rock[i][j]=dp[i][j]=0;
		dp[0][0]=1;
		H--; W--;
		for(int i = 0; i<R; i++) {
			int r, c;
			fscanf(fin,"%d%d",&r,&c);
			r--;
			c--;
			rock[r][c] = 1;
		}
		for(int i = 0; i<=H; i++) {
			for(int j = 0; j<=W; j++) {
				if(i>=2 && j>=1 && !rock[i-2][j-1]) dp[i][j]+=dp[i-2][j-1];
				if(i>=1 && j>=2 && !rock[i-1][j-2]) dp[i][j]+=dp[i-1][j-2];
				dp[i][j]%=MODULUS;
			}
		}
		fprintf(fout,"Case #%d: %d\n",k,dp[H][W]);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
