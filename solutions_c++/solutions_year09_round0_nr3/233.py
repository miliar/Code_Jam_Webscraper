#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define eps 1e-10
#define inf 0x3f3f3f3f

#define fr(x,y,z)	for(int x = (y); x < (z); x++)

#define dbg(x) cout << #x << " == " << x << endl
#define print(x) cout << x << endl

const char *str = "welcome to code jam";
const int MOD = 10000;
char seq[1000];

int dp[1000][1000];
int casos = 1;

void process() {
	// base case
	dp[0][0] = (str[0] == seq[0] ? 1 : 0);
	for(int i = 1; seq[i]; i++) {
		dp[0][i] = dp[0][i-1];
		if(seq[i] == str[0]) dp[0][i]++,dp[0][i]%=MOD;
	}
	for(int i = 1; str[i]; i++) {
		dp[i][0] = 0;
		for(int j = 1; seq[j]; j++) {
			dp[i][j] = dp[i][j-1];
			if(seq[j] == str[i]) {
				dp[i][j] += dp[i-1][j-1];
				dp[i][j] %= MOD;
			}
		}
	}
	printf("Case #%d: %.4d\n",casos++,dp[strlen(str)-1][strlen(seq)-1]);
}

int main() {

	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	
	int t;
	gets(seq);
	sscanf(seq,"%d",&t);
	while(t--) {
		gets(seq);
		process();
	}
	
	return 0;
	
}
