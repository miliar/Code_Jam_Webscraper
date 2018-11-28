#include<cstdio>
#include<cstdlib>

using namespace std;

char goal[20] = "welcome to code jam";
int dp[20];

int main() {
	FILE *fin = fopen("C.in","r");
	FILE *fout = fopen("C.out","w");
	int K;
	fscanf(fin,"%d ",&K);
	for(int k = 0; k<K; k++) {
		char c;
		fscanf(fin,"%c",&c);
		for(int j = 0; j<20; j++) {
			dp[j] = 0;
		}
		dp[0] = 1;
		while(c != 10) {
			for(int j = 0; j<19; j++) {
				if(goal[j] == c) {
					dp[j+1] = (dp[j+1] + dp[j])%10000;
				}
			}
			fscanf(fin,"%c",&c);
		}
		fprintf(fout,"Case #%d: %04d\n",k+1,dp[19]);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
