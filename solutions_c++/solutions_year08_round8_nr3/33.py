#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <queue>
#include <fstream>

using namespace std;

typedef vector <string> vs;
typedef vector <int> vi;
#define REP(a,b) for(long long a=0;a<(b);++a)
#define FOR(a,c,b) for(long long  a=c;a<(b);++a)

const long long mod = 1000000009;

vector <vi> g;
vi vis, vis2;
int usedcnt;

void dfs(int pos, int d)
{
	vis2[pos] = 1;
	if (d >= 2) return;
	REP(i,g[pos].size()) if (vis[g[pos][i]] && !vis2[g[pos][i]]) {
		++usedcnt;
		dfs(g[pos][i], d+1);
	}
}

int main()
{
	//ifstream fin("C-small.in");
	//ofstream fout("C-small.out");
	ifstream fin("C-large.in");
	ofstream fout("C-large.out");

	long long nc, n, c;

	fin >> nc;

	for (int tc = 1; tc <= nc; ++tc)
	{
		fout <<"Case #"<<tc<<": ";

		fin >> n >> c;

		g.clear();
		g.resize(n);

		REP(i,n-1) {
			int a, b;
			fin >> a >> b;
			g[a-1].push_back(b-1);
			g[b-1].push_back(a-1);
		}

		long long res = 1;
		vector <long long> next(n, -1);
		next[0] = c;

		int pos = 0, lev;
		queue <pair<int,int> > q;
		q.push(make_pair(0,0));
		vi lvl(n+10,0);
		vis.resize(n);
		fill(vis.begin(), vis.end(), 0);
		vis[0] = 1;

		while (!q.empty()) {
			pos = q.front().first; lev = q.front().second; q.pop();
			usedcnt = 0;
			vis2.resize(n);
			fill(vis2.begin(), vis2.end(), 0);
			dfs(pos, 0);
			int used = usedcnt;

			//for (int i = lev-1; i >= 0 && lev-i <= 2; --i) used += lvl[i];
			int counter = 0;
			REP(i,g[pos].size()) if (!vis[g[pos][i]]) {
				//cout << c << " " << used << " " << i << endl;
				res = (res*(c-used-counter))%mod;
				if (c-used-counter < 0) res = 0;
				lvl[lev]++;
				q.push(make_pair(g[pos][i], lev+1));
				vis[g[pos][i]] = 1;
				++counter;
			}
		}

		fout << res << endl;

	}

	fin.close();
	fout.close();

	return 0;
}

