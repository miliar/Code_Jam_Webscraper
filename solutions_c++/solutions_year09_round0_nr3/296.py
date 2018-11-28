#include <cmath>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <list>
#include <climits>
#include <ctime>
using namespace std;

#define NIL INT_MAX/2
#define inf 1e20
#define eps 1e-10

#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,a,b) for(int i=a; i<(b); ++i)
#define clr(x) memset(x,0,sizeof(x)) 

const int N = 1000;
string nb = "welcome to code jam";

int dp[600];
int cnt[600];

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int n;
	int cases = 1;
	cin >> n;
	getchar();
	string inp;

	while(n--) {
		memset(dp, 0, sizeof(dp));
		memset(cnt, -1, sizeof(cnt));
		getline(cin, inp);
		printf("Case #%d: ", cases++);
		//cout << inp << endl;
		for(int j = 0; j < inp.size(); j++) {
			if(inp[j] == nb[0])dp[j] = 1, cnt[j] = 0;
		}

		for(int i = 1; i < nb.size(); i++) {
			for(int j = 0; j < inp.size(); j++) {
				if(inp[j] == nb[i]) {
					int tmp = 0;
					for(int k = 0; k < j; k++) {
						if(inp[k] == nb[i-1] && cnt[k] == i-1)
							tmp += dp[k], cnt[j] = i;
					}
					tmp %= 10000;
					if(cnt[j] == i)dp[j] = tmp;
				}
			}
		}
		int ans = 0;
		for(int j = 0; j < inp.size(); j++) {
			if(inp[j] == nb[nb.size() - 1] && cnt[j] == nb.size() - 1)
				ans += dp[j];
		}
		ans %= 10000;
		if(ans < 10)printf("000%d\n", ans);
		else if(ans < 100)printf("00%d\n", ans);
		else if(ans < 1000)printf("0%d\n", ans);
		else printf("%d\n", ans);
	}

	return 0;
}

/*Powered By Lynn-Beta1*/