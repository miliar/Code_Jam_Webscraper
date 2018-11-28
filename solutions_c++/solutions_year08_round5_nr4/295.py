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

ll MOD = 10007;

ll ans[128][128];
int H, W, R;
set<pair<int, int> > rooks;

int main(void)	{
	int numTestCases;
	cin >> numTestCases;
	
	for (int nc = 1; nc <= numTestCases; nc++)	{
		cin >> H >> W >> R;
		rooks.clear();

		FOR (i, 0, R)	{
			int a, b;
			cin >> a >> b;
			rooks.insert(mp(a, b));
		}
		
		
		memset(ans, 0, sizeof ans);
		ans[1][1] = 1;

		FOR (i, 1, H+1)	{
			FOR (j, 1, W+1)	if (rooks.find(mp(i,j)) == rooks.end())	{
				FOR (pi, max(1, i-2), i)	FOR (pj, max(1, j-2), j)	if ((i - pi)*(i - pi) + (j - pj)*(j - pj) == 5)	{
					ans[i][j] = (ans[i][j] + ans[pi][pj]) % MOD;
				}
				//dbg (i);
				//dbg (j);
				//dbge(ans[i][j]);
			}
		}


	

		cout << "Case #" << nc << ": " << ans[H][W] << endl;	
	}
}
