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
#define _bpc __builtin_popcount
#define pb push_back
#define MP make_pair
#define For(a,b,c) for(typeof(b)a=(b); a<(c); ++a)
#define ALL(a) a.begin(),a.end()
#define DBG(a) cout << #a << ": " << a << endl
#define FORE(i, v) for(typeof(v.begin()) i = v.begin(); i != v.end(); ++i)

int main()
{
	ifstream fin("B.in");
	ofstream fout("B2.out");
	
	int C;
	fin >> C;
	For (lol, 1, C+1)
	{
		int N, M;
		fin >> N >> M;
		vector<pii> likes[2011];
		
		vi wantnot[2011];
		int type[2011] = {0};
		
		int poss[2011] = {0};
		int malt[2011] = {0};
		memset(malt, -1, sizeof(malt));
	
		bool ok = true, ch = true;
		For (i, 0, M)
		{
			int T; fin >> T; poss[i] = T;
			For (j, 0, T)
			{ int a, b; fin >> a >> b; a--; likes[i].pb(MP(a,b)); if (b == 1) poss[i]--, malt[i] = a; else wantnot[a].pb(i); }
			if (poss[i] == 0 && malt[i] == -1) goto done;
		}
	
		do
		{
			ch = false;
			For (j, 0, M)
				if (poss[j] == 0) { //malt for him!
					poss[j] = -1;
					ch = true;
					if (malt[j] == -1)  { ok = false; goto done; }
					if (type[malt[j]] == 1) continue;
					type[malt[j]] = 1;
					FORE(k, wantnot[malt[j]]) {
						poss[*k]--;
						if (poss[*k] < 0) { ok = false; goto done; }
					}
				}
		}
		while (ch);

		done:;
		
		fout << "Case #" << lol << ":";
		
		if (!ok) fout << " IMPOSSIBLE";
		else  {
			For (i, 0, M) {
				bool ok = false;
				FORE(p, likes[i])
					if (type[p->first] == p->second)
						{ ok = true; break; }
				if (!ok) throw;
			}
			For (i, 0, N)
				fout << " " << type[i]; 
		}
				
		fout << endl;
	}
}
