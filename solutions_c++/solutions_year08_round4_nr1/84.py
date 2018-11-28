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

#define FORALL(var,x) for (typeof(x.begin()) var=x.begin(); var!=x.end(); var++)
#define FOR(var,lo,hi) for (int var=(lo); var<(hi); var++)
#define SORT(x) sort(x.begin(), x.end())
#define ALL(x) x.begin(), x.end()
#define UNIQUE(x) x.erase(unique(x.begin(),x.end()),x.end()) 

#define mp make_pair
#define pb push_back

typedef long long ll;
typedef vector<int> vi;

int dp[10001][2], change[10001], gate[10001], val[10001];

int M, V;

int main(void)	{
	int numTestCases;
	cin >> numTestCases;
	
	for (int nc = 1; nc <= numTestCases; nc++)	{
		memset(dp, 31, sizeof dp);

		int INF = dp[0][0];
		
		memset(change, 0, sizeof change);
		memset(gate, 0, sizeof gate);
		memset(val, 0, sizeof val);

		cin >> M >> V;
		for (int i = 1; i <= (M-1)/2; i++)	{
			cin >> gate[i] >> change[i];
		}
		for (int i = 1 + (M-1)/2; i <= M; i++)	{
			cin >> val[i];
			dp[i][val[i]] = 0;
		}
	
		for (int i = (M-1)/2; i >= 1; i--)	{
			if (gate[i] == 1)	{
				for (int x = 0; x < 2; x++)	for (int y = 0; y < 2; y++)	{
					dp[i][x & y] = min(dp[i][x & y], dp[i*2][x] + dp[i*2+1][y]);
				}
			}
			else	{
				for (int x = 0; x < 2; x++)	for (int y = 0; y < 2; y++)	{
					dp[i][x | y] = min(dp[i][x | y], dp[i*2][x] + dp[i*2+1][y]);
				}
			}

			if (change[i] == 1)	{
				if (gate[i] == 1)	{
					for (int x = 0; x < 2; x++)	for (int y = 0; y < 2; y++)	{
						//dp[i][x & y] = min(dp[i][x & y], dp[i*2][x] + dp[i*2+1][y]);
						dp[i][x | y] = min(dp[i][x | y], 1 + dp[i*2][x] + dp[i*2+1][y]);
					}
				}
				else	{
					for (int x = 0; x < 2; x++)	for (int y = 0; y < 2; y++)	{
						//dp[i][x | y] = min(dp[i][x | y], dp[i*2][x] + dp[i*2+1][y]);
						dp[i][x & y] = min(dp[i][x & y], 1 + dp[i*2][x] + dp[i*2+1][y]);
					}
				}
			}
		}
		cout << "Case #" << nc << ": ";
		if (dp[1][V] >= INF)	cout << "IMPOSSIBLE" << endl;
		else	cout << dp[1][V] << endl;

	}
}
