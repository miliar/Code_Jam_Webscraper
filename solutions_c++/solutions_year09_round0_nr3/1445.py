#include <iostream>
#include <vector>

using namespace std;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long long ll;

char *astr = "welcome to code jam";

inline bool solve(int tc){
	char line[512];
	fgets(line, 512, stdin);
	int len = strlen(line);
	int alen = strlen(astr);
	vvi dp(alen, vi(len, 0));	
	for(int j = 0; j<len; ++j){
		if(astr[0] == line[j]){
			dp[0][j] = 1;
		}
	}
	for(int i = 1; i<alen; ++i){
		for(int j = 0; j<len; ++j){
			if(astr[i] == line[j]){
				for(int k = 0; k<j; ++k)
					dp[i][j] += dp[i-1][k];
				dp[i][j]%=10000;
			}
		}
	}
	int ans = 0;
	for(int i = 0; i<len; ++i){
		ans += dp[alen-1][i];
	}
	printf("Case #%d: %04d\n", tc, ans%10000);
	return true;
}

int main (int argc, char const *argv[]) {
	int n; scanf("%d ",&n);
	for(int k=1;solve(k)&&k<n;k++);
	return 0;
}