#include<cstdio>
#include<string>
#include<iostream>

using namespace std;

string S = "welcome to code jam";
int dp[505][21];
string I;
int n, m;
int mod = 10000;

int memo(int u, int v) {
	if( v == m ) return 1;
	if( u == n ) return 0;
	if( dp[u][v] != -1 ) return dp[u][v];
	int i;
	int res = 0;

	for(i=u;i<n;i++)
	  if( I[i] == S[v] ) {
		 res += memo(i+1, v+1);
		 res %= mod;
	  }

	return dp[u][v] = res;
}

int main() {
	int test, cases;
	char str[1000];
	gets(str);
	sscanf(str, "%d", &test);
	for( cases = 1; cases <= test; cases++) {
	   gets(str);
	   I = str;
	   n = I.size();
	   m = S.size();

	   int i, j;
	   for(i=0;i<n;i++)
	    for(j=0;j<m;j++)
	      dp[i][j] = -1;

	   int res = memo(0, 0);
	   printf("Case #%d: %04d\n", cases, res);

	}
}