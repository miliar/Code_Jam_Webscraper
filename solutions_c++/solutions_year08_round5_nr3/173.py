#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <list>
#include <string>
#include <algorithm>
#include <functional>
#include <utility>
#include <cassert>
#include <cmath>
#include <cstdlib>
#include <cstdio>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
#define pb push_back
#define MP make_pair
#define For(a,b,c) for(typeof(b)a=(b); a<(c); ++a)
#define ALL(a) (a).begin(),(a).end()
#define DBG(a) cout << #a << ": " << a << endl
#define FORE(i, v) for(typeof(v.begin()) i = v.begin(); i != v.end(); ++i)

int main()
{
	freopen("C.in", "r", stdin);
	
	int T;
	cin >> T;
	For (LOL, 1, T+1)
	{
		char grid[10][10];
		int mask[10];
	
		int R, C;
		cin >> R >> C;
		For (i, 0, R)
		{
			int m = 0;
			For (j, 0, C) {
				cin >> grid[i][j];
				if (grid[i][j] != '.')
					m |= (1<<j);
			}
			mask[i] = m;
		}
		
		bool ok[1<<10] = {0};
		For (i, 0, (1<<C)) {
			For (j, 0, C)
				if ((i&(1<<j)) && ((j && (i&(1<<(j-1)))) || ((j+1)<C && (i&(1<<(j+1))))))
					goto fail;
			ok[i] = true;
			continue;
			fail:;
		}
		
		int next[1<<10];
		For (i, 0, (1<<C)) {
			next[i] = 0;
			For (j, 0, C)
				if (i & (1<<j))
				{
					if (j) next[i] |= (1<<(j-1));
					if ((j+1)<C) next[i] |= (1<<(j+1));
				}
		}
		
		int best[1<<10][11];
		
		memset(best, -1, sizeof(best));		
		best[mask[0]][0] = 0;
		For (i, 0, R)
			For (j, 0, (1<<C))
				if (best[j][i] >= 0)
					For (k, 0, (1<<C))
						if (!(k&j) && !(k&mask[i]) && ok[k])
							best[next[k]][i+1] >?= __builtin_popcount(k) + best[j][i];

		int res = 0;
		For (i, 0, (1<<C))
			res >?= best[i][R];
		
		printf("Case #%d: ", LOL);
		cout << res << endl;
		
	}
	
	return 0;
}