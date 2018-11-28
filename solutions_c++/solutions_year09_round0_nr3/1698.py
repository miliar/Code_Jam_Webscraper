#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include <map>
#include <vector>
using namespace std;
#define BASE 10000
char s[1024];
char *wel = "welcome to code jam";
int dp[1024][20];
int N;

int go(char *s, int slength, int pos, int wlen){
	if( wlen == 19)
		return dp[pos][wlen] = 1;
	if( pos == slength){
		return 0;
	}
	if( dp[pos][wlen] != -1)
		return dp[pos][wlen];
	dp[pos][wlen] = 0;
	for(int i = pos; i < slength; i++){
		if( s[i] == wel[wlen]){
			dp[pos][wlen] = (dp[pos][wlen] + go(s, slength, i, wlen + 1)) % BASE;
		}
	}
	return dp[pos][wlen];
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	gets(s);
	sscanf(s, "%d", &N);
	for(int t = 1; t <= N; t++){
		int res = 0;

		gets(s);
		memset(dp, -1, sizeof(dp));
		int slength = strlen(s);
		go(s, slength, 0, 0);
		for(int i = 0; i < slength; i++){
			if( dp[i][0] >= 0){
				res = (res + dp[i][0]) % BASE;
			}
		}


		char s[5];
		string out = "";
		while( out.size() < 4){
			out = char (res % 10 + '0') + out;
			res /= 10;
		}
		printf("Case #%d: %s\n",t, out.c_str());
	}
}