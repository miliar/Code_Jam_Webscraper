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
typedef vector<vector<int> > VVI;

int64 INF = 1000*1000*1001;


struct state	{
	int y, x;
	VVI b;	//1 = empty, 0 = earth
	state(int _y, int _x, VVI& _b) :  y(_y), x(_x), b(_b) {};
	
/*	bool operator()	(const state &o)	const {
		cout << "calling eq" << endl;
		return (y == o.y && x == o.x && b == o.b);
	}
*/
	
	bool operator < (const state& o)	const {
		//cout << "less than" << endl;
		if (y > o.y)	return true;
		if (y < o.y)	return false;
		if (x > o.x)	return true;
		if (x < o.x)	return false;
		return b < o.b;
	}
};

int R, C, F;

void print(VVI& b)	{
	FOR (i, 0, R)	{
		FOR (j, 0, C)	cout << (b[i][j] == 1 ? '.' : '#');
		cout << endl;
	}
	cout << endl;
}

set<pair<int, state> > q;	//holes dug, board
map<state, int> best;

int main(void)	{
	int T;
	cin >> T;
	
	FOR (nc, 1, T+1)	{
		q.clear();
		best.clear();
		
		cin >> R >> C >> F;
		VVI b(R, vector<int>(C, 0));
		
		FOR (i, 0, R)	{
			string s;
			cin >> s;
			FOR (j, 0, C)	{
				if (s[j] == '#')	b[i][j] = 0;	else b[i][j] = 1;
			}
		}
		
		state cur(0, 0, b);
		best[cur] = 0;
		q.insert(MP(0, cur));
		
		
		int ans = -1;
		
		while (! q.empty())	{
			pair<int, state> pr = *(q.begin());
			q.erase(q.begin());
			
			int holes = pr.first;
			state cur = pr.second;

			if (best[cur] < holes)	continue;
			
			int y = cur.y, x = cur.x;
			VVI b = cur.b;
			
			
			//check bottom
			if (y == R-1)	{	ans = holes;	break;	}
			
			VVI nb = b;

			/*
			cout << "best.SZ = " << best.SZ << endl;
			cout << "h = " << holes << endl;
			cout << "y = " << y << ", x = " << x << endl;
			print(b);
			*/
			
			//dig hole
			for (int dx = -1; dx <= 1; dx+=2)	{
				if (x+dx >= 0 && x+dx < C && y < R-1 && b[y][x+dx] == 1 && b[y+1][x+dx] == 0)	{
					nb[y+1][x+dx] = 1;

					//fall
					int ny = y + 1;
					for (; ny < R && nb[ny][x+dx] == 1; ny++);
					ny--;
					if (ny - y <= F)	{
						state ns(ny, x+dx, nb);
						if (! best.count(ns) || best[ns] > holes + 1)	{
							best[ns] = holes + 1;
							q.insert(MP(holes + 1, ns));
						}
					}
					
					//don't fall
					state ns(y, x, nb);
					if (! best.count(ns) || best[ns] > holes + 1)	{
						//cout << "adding don't fall" << endl;
						//cout << q.SZ;
						best[ns] = holes + 1;
						q.insert(MP(holes+1, ns));
						//cout << ", " << q.SZ << endl;
					}
					
					nb[y+1][x+dx] = 0;
				}
			}
			
			//walk
			for (int dx = -1; dx <= 1; dx += 2)	{
				//cout << "checking " << x+dx << ", " << y << endl;

				if (x+dx >= 0 && x+dx < C && b[y][x+dx] == 1)	{
					//cout << "adding " << endl;
					int ny = y;
					for (; ny < R && nb[ny][x+dx] == 1; ny++);
					ny--;
					if (ny - y <= F)	{
						//cout << "adding " << endl;
						state ns(ny, x+dx, nb);
						if (! best.count(ns) || best[ns] > holes)	{
							//cout << "cnt = " << best.count(ns) << endl;
							best[ns] = holes;
							q.insert(MP(holes, ns));
						}
					}
				}
			}
		}
		
		cout << "Case #" << nc << ": ";
		if (ans == -1)	cout << "No" << endl;
		else	cout << "Yes " << ans << endl;
	}
	
	
}
