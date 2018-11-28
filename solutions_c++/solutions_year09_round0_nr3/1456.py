#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
using namespace std;

int N;
string s, c;
int dp[512][32];

void solve (string s) {
	memset (dp,0,sizeof(dp));
	for(int i=0; i<s.size(); ++i) if( s[i] == 'w' ) dp[i][0] = 1;
	for(int i=1; i<19; ++i)
		for(int j=0; j<s.size(); ++j)
			if( s[j] == c[i] ){
				for(int k=0; k<j; ++k) dp[j][i] += dp[k][i-1];
				dp[j][i] %= 10000;
				}
	int res = 0;
	for(int i=0; i<s.size(); ++i){
		res += dp[i][18];
		if( res >= 10000 ) res -= 10000;
		}
	if( !res ){ printf ("0000\n"); return; }
	for(int i=0; i<3-log10(res); ++i) printf ("0");
	printf ("%d\n",res);
}

void input () {
	c = "welcome to code jam";
	scanf ("%d\n",&N);
	for(int i=0; i<N; ++i){
		getline (cin,s);
		printf ("Case #%d: ",i+1);
		solve (s);
		}
}

int main (void) {
	input ();
}
