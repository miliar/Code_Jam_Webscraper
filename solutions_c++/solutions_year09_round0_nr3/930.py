#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>

using namespace std;

const int MAXN		= 512;
const char* JAM		= "welcome to code jam";
const int JAM_LENGTH	= 19;
const int MOD			= 10000;

int dp[JAM_LENGTH+1][MAXN];
int N;

int main () {
	
	scanf("%d\n", &N);
	
	char *line = new char[MAXN];
	
	for (int i = 0; i < N; ++i) {
		string a;
		getline(cin, a);
		line = (char*) a.c_str();
		//gets(line);
		int len  = strlen(line);
		
		for (int k = 0; k <= JAM_LENGTH; ++k)
			for (int j = 0; j < MAXN; ++j) dp[k][j] = 0;
		
		for (int k = 0; k <= len; ++k) dp[0][k] = 1;
		//for (int k = 0; k <= JAM_LENGTH; ++k) dp[k][0] = 1;
		
		for (int j1 = 1; j1 <= JAM_LENGTH; ++j1)
			for (int i1 = 1; i1 <= len; ++i1) {				
				if ( line[i1-1] == JAM[j1-1] )
					dp[j1][i1] = (dp[j1-1][i1-1] + dp[j1][i1-1])%MOD;
				else
					dp[j1][i1] = dp[j1][i1-1]%MOD;
			}
		
/*		for (int j1 = 0; j1 <= JAM_LENGTH; ++j1) {
			for (int i1 = 0; i1 <= len; ++i1) 
				printf ("%d ", dp[j1][i1]);
			puts("");
		}
*/		
		int r = dp[JAM_LENGTH][len];
		printf("Case #%d: %d%d%d%d\n", i+1, r/1000, r/100%10, r/10%10, r%10);

	}
	
	
	return 0;
}