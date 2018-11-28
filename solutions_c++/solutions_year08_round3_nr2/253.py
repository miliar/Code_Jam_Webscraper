#import <cstdio>
#import <string>
#import <algorithm>

using namespace std;
FILE* in, out;

#define MAX_LEN 42
#define THING (2*3*5*7)

int main() {
	in = fopen("b.in","r");
	int ncases;
	fscanf(in,"%d",&ncases);
	for (int casen = 1; casen <= ncases; casen++) {
		printf("Case #%d: ",casen);
		char buff[MAX_LEN];
		fscanf(in,"%s",&buff);
		long long dp[MAX_LEN][THING];
		for (int i =0; i < MAX_LEN;i++){for(int j = 0;j<THING;j++) {dp[i][j]=0;}}
		dp[0][0] = 1;
		for (int i = 0; i < strlen(buff); i++) {
			int total = 0;
			for (int j = i; j < strlen(buff); j++) {
				int x = buff[j]-'0';
				total = ((total*10) + x) % THING;
				int invtotal = THING - total;
				for (int k = 0; k < THING; k++) {
					dp[j+1][(k+total)%THING] += dp[i][k];
					if (i != 0) {dp[j+1][(k+invtotal)%THING] += dp[i][k];}
				}
			}
		}
		
		int total=0;
		for (int l = 0; l < THING; l++) {
			if ((l%2)*(l%3)*(l%5)*(l%7)==0) {total+=dp[strlen(buff)][l];}
		}printf("%d\n",total);
	}
}
