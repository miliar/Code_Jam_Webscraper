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

int b[2][400][400], R;

int main(void)	{
	int C;
	cin >> C;
	FOR (nc, 1, C+1)	{
		memset(b, 0, sizeof b);
		int cur = 0, prev = 1;
		int my = 0, mx = 0;
		
		cin >> R;		
		FOR (k, 0, R)	{
			int x1, y1, x2, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			FOR (i, y1, y2 + 1)	FOR (j, x1, x2 + 1)	{
				b[cur][i][j] = 1;
				my = max(i, my);
				mx = max(j, mx);
			}
		}
		
		int ans = 0;
		while (true)	{
			ans++;
			prev ^= 1;
			cur ^= 1;
			int nmx = mx, nmy = my;
			//mx = 300, my = 300;
			bool alive = false;
			FOR (i, 1, my + 2)	FOR (j, 1, mx + 2)	{
				if (b[prev][i-1][j] == 1 && b[prev][i][j-1] == 1)	{
					b[cur][i][j] = 1;
				}
				else if (b[prev][i-1][j] == 0 && b[prev][i][j-1] == 0)	{
					b[cur][i][j] = 0;
				}
				else	{
					b[cur][i][j] = b[prev][i][j];
				}
				if (b[cur][i][j] == 1)	{
					alive = true;
					nmx = max(nmx, j);
					nmy = max(nmy, i);
				}
			}
			mx = nmx, my = nmy;
			if (!alive)	break;
		}
		//cout << my << "\t" << mx << endl;		
		cout << "Case #" << nc << ": " << ans << endl;
	}
	
	
}
