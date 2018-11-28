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
#include <cstdio>
#include <cmath>
#include <cstdlib>
using namespace std;

#define FOR(i,a,b) for (int i=a; i<(int)(b); i++)
#define FORE(i,a,b) for (int i=a; i<=(int)(b); i++)

typedef long long ll;
typedef vector<int> vi;

int main(void)	{
	string s;
	map<string, int> smap;
	int dp[2][128], INF = 1000*1000;

	int ncases, S, Q;

	cin >> ncases;

	FORE(nc, 1, ncases)	{
		smap.clear();
		cin >> S;
		cin.ignore();

		FOR(i, 0, S)	{
			getline(cin, s);
			smap[s] = i;
		}

		cin >> Q;
		cin.ignore();

		int prev = 0, cur = 1;
		memset(dp[prev], 0, sizeof dp);
		FOR(i, 0, Q)	{
			getline(cin, s);
			memset(dp[cur], 127, sizeof dp[cur]);
			int c = -1;
			if (smap.count(s) != 0)	c = smap[s];

			FOR (j, 0, S)	if(j != c)	{
				FOR (k, 0, S)	{
					if (k==j)	dp[cur][j]=min(dp[cur][j], dp[prev][k]);
					else		dp[cur][j]=min(dp[cur][j], dp[prev][k]+1);
				}
			}

			cur ^= 1;
			prev ^= 1;
		}
		int mn = Q;
		FOR(i, 0, S)	{
			mn = min(mn, dp[prev][i]);
		}
		cout << "Case #" << nc << ": " << mn << endl;
	}
}
