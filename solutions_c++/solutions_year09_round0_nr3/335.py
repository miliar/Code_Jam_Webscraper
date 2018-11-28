#include<cstdio>
#include<string>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<vector>
#include<list>
#include<map>
#include<queue>

#define FOR(i,a,b) for(int i=(int)(a); i<(int)(b); ++i)

using namespace std;

char S[1000];
string GCJ = "welcome to code jam";
int dp[2][20];

void testcase(int testNr) {
	gets(S);
	int len = strlen(S);
	
	FOR(i,0,20)
		dp[0][i] = dp[1][i] = 0;
	dp[0][0] = 1;
	
	FOR(i,0,len) {
		FOR(j,0,20)
			dp[1][j] = dp[0][j];
			
		FOR(j,0,20) if(S[i] == GCJ[j])
			dp[1][j+1] += dp[0][j];
	
		FOR(j,0,20)
			dp[0][j] = dp[1][j]%10000;
	}

	printf("Case #%d: %04d\n",testNr,dp[0][19]);
}

int main() {
	int t;
	gets(S);
	sscanf(S,"%d",&t);
	FOR(i,0,t)
		testcase(i+1);
}
