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
#define dbg(x) cerr << #x << " -> '" << (x) << "'\t"
#define dbge(x) cerr << #x << " -> '" << (x) << "'\n"

#define mp make_pair
#define pb push_back

typedef long long ll;
typedef vector<int> vi;
string s[128];

int dp[128][1<<10];
int R, C;

int main(void)	{
	int numTestCases;
	cin >> numTestCases;
	

	for (int nc = 1; nc <= numTestCases; nc++)	{
		cin >> R >> C;
		FOR (i, 1, R+1)	{
			cin >> s[i];
		}
		
		memset(dp, 0, sizeof dp);

		FOR (i, 1, R+1)	{
			FOR (msk, 0, 1<<C)	{
				int trymsk = 0, bits = 0;
				bool flag = true;
				FOR (j, 0, C){
					if ((msk & (1<<j)) != 0 && s[i][j] != 'x')	{
						bits++;
						if (j>0)	trymsk |= 1<<(j-1);
						if (j<C-1)	trymsk |= 1<<(j+1);
						if ((j>0 && (msk&(1<<(j-1)))!=0) || (j<C-1 && (msk&(1<<(j+1)))!=0) )	{
							flag = false;
							break;
						}
					}
				}
				if (!flag)	continue;

				int val = 0;
				FOR (check, 0, 1<<C)	if ((check & trymsk) == 0)	{
					val = max(val, dp[i-1][check]);
				}
				dp[i][msk] = val + bits;
			}
		}
		int ans = 0;
		FOR (msk, 0, 1<<C)	{
			ans = max(ans, dp[R][msk]);
		}

		cout << "Case #" << nc << ": " << ans << endl;	
	}
}
