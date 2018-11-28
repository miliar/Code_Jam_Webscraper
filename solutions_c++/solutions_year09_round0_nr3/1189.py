#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <list>
using namespace std;

int dp[19][600];
const int mod=10000;
char str[600];
string s="welcome to code jam";

int main(){
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int n,len;
	gets(str);
	sscanf(str, "%d", &n);
	for(int x=1;x<=n;x++){
		gets(str);
		len=(int)strlen(str);
		memset(dp,0,sizeof(dp));
		if(str[0]==s[0])dp[0][0]=1;
		for(int j=1;j<len;j++){
			if(str[j]==s[0])dp[0][j]=dp[0][j-1]+1;
			else dp[0][j]=dp[0][j-1];
		}
		for(int i=1;i<19;i++){
			for(int j=i;j<len;j++){
				if(str[j]==s[i]){
					dp[i][j]=(dp[i][j-1]+dp[i-1][j-1])%mod;
				}
				else dp[i][j]=dp[i][j-1];
			}
		}
		printf("Case #%d: %04d\n", x, dp[18][len-1]);
	}
	
	return 0;
}