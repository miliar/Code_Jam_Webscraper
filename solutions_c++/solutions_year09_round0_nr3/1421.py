#include<stdio.h>
#include<string.h>
#include<string>
using namespace std;

#define MAXL 500
#define rep(i,n) for(i=0;i<(n);i++)

int dp[MAXL+5][25];
string st = "welcome to code jam";
string s;
int n;
int L = st.size();

int main() {
	int T,kase=1;
	char tmp[MAXL+5];
	int i,j;

	gets(tmp);
	sscanf(tmp,"%d",&T);
	while(T--) {
		gets(tmp);
		s = tmp;
		n = s.size();

		memset(dp,0,sizeof(dp));
		rep(i,n) {
			if(i == 0) dp[i][0] = (s[i] == st[0]);
			else dp[i][0] = dp[i-1][0] + (s[i] == st[0]);
		}

		for(i=1;i<L;i++) {
			rep(j,n) {
				if(j > 0) dp[j][i] = dp[j-1][i];
				if(i > 0 && j > 0 && st[i] == s[j]) dp[j][i] += dp[j-1][i-1];
				if(dp[j][i] >= 10000) dp[j][i] %= 10000;
			}
		}
		printf("Case #%d: %04d\n",kase++,dp[n-1][L-1]);
	}
	return 0;
}