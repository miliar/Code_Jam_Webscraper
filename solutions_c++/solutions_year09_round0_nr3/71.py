#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>

using namespace std;

#define FOR(i,a,b)	for(int i=(a); i<(b); ++i)
#define REP(iter,v) for(typeof((v).begin()) iter = (v).begin(); iter != (v).end(); ++iter)
#define MP make_pair
#define PB push_back
#define SZ size()
#define iss istringstream 

#define SORT(x) sort(x.begin(), x.end())
#define ALL(x) x.begin(), x.end()
#define UNIQUE(x) x.erase(unique(x.begin(),x.end()),x.end()) 
#define dbg(x) cerr << #x << " -> '" << (x) << "'\t"
#define dbge(x) cerr << #x << " -> '" << (x) << "'\n"

typedef long long ll, int64;
typedef vector<int> VI;

int64 INF = 1000*1000*1001;
int MOD = 10000;

int dp[512][32];
int main(void)	{
	int C;
	cin >> C;
	cin.ignore();
	string t = "welcome to code jam";
	int n = t.SZ;
	
	FOR (nc, 1, C+1)	{
		string s;
		getline(cin, s);
		//cout << s << endl;

		int L = s.SZ;		
		memset(dp, 0, sizeof dp);
		
		FOR (i, 0, L)	FOR (j, 0, n)	if (s[i] == t[j])	{
			//cout << i << " " << j << endl;
			if (j == 0)	dp[i][j] = 1;
			else	{
				FOR (k, 0, i)	if (s[k] == t[j-1])	dp[i][j] += dp[k][j-1];
			}		
			dp[i][j] %= MOD;
		}
		
		int ans = 0;
		FOR (i, 0, L)	ans += dp[i][n-1];
		ans %= MOD;
		
		cout << "Case #" << nc << ": ";
		printf("%04d\n", ans);
	}
	
	
}
