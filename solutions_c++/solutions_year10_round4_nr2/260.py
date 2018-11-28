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

ll c[2048];
ll dp[2048][12];
int P;

int main(void)	{
	int C;
	cin >> C;
	FOR (nc, 1, C+1)	{
		cin >> P;
		FOR (i, 0, 1<<(P+1))	{
			FOR (j, 0, P + 1)	{
				dp[i][j] = INF;
			}
		}
		
		FOR (i, 0, 1<<P)	{
			int t;
			cin >> t;
			dp[(1<<P) + i][P - t] = 0;
		}
		//cout << "here" << endl;
		for (int i = P - 1; i >= 0; i--)	{
			FOR (j, 0, 1<<i)	{
				cin >> c[(1<<i) + j];
			}
		}
		//cout << "here2" << endl;
		
		for (int i = (1<<P) - 1; i >= 1; i--)	{
			//cout << i << endl;
			FOR (l, 0, P+1)	FOR (r, 0, P+1)	{
				int rem = max(l, r);
				dp[i][max(rem - 1, 0)] = min(dp[i][max(rem - 1, 0)], dp[2*i][l] + dp[2*i+1][r] + c[i]);	//buy
				dp[i][rem] = min(dp[i][rem], dp[2*i][l] + dp[2*i+1][r]);	//don't buy
			}
		}
		
		cout << "Case #" << nc << ": " << dp[1][0] << endl;
	}
	
	
}
