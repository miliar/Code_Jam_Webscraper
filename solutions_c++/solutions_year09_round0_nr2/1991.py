#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <cmath>
#include <memory.h>

using namespace std;

#define FOR(i,a,b) for(int i=a; i<b; ++i)
#define RFOR(i, a, b) for(int i=b-1; i>=a; --i)
#define FILL(a, val) memset(a, val, sizeof(a))

#define pb push_back
#define sz(c) (int)c.size()
#define all(c) c.begin(),c.end()

#define mp make_pair
#define X first
#define Y second

typedef long int Int;
typedef vector<int> VI;
typedef pair<int, int> PII;

const int INF = 1000000000;
const double PI = acos(-1.0);

int h[102][102];
char res[102][102];
vector<PII> prev[102][102];
PII next[102][102];

void go(int i, int j, char c)
{
	res[i][j] = c;
	FOR(k, 0, sz(prev[i][j]))
		if (res[prev[i][j][k].X][prev[i][j][k].Y] == 0)
			go(prev[i][j][k].X, prev[i][j][k].Y, c);
}

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	FOR(t, 0, T)
	{
	
		FILL(h, -1);
		FOR(i, 0, 102)
			FOR(j, 0, 102)
		{
				prev[i][j].clear();	
				next[i][j] = mp(-1, -1);
		}
	int ttt=0;
	if (t == 92)
		ttt = 2;
	ttt=0;

		int m, n;
		scanf("%d%d", &m, &n);
		FOR(i, 1, m+1)
			FOR(j, 1, n+1)
				scanf("%d", &h[i][j]);
	
		FOR(i, 1, m+1)
			FOR(j, 1, n+1)
			{
				VI v;
				if (h[i-1][j] != -1)
					v.pb(h[i-1][j]);
				if (h[i+1][j] != -1)
					v.pb(h[i+1][j]);
				if (h[i][j-1] != -1)
					v.pb(h[i][j-1]);
				if (h[i][j+1] != -1)
					v.pb(h[i][j+1]);
				sort(all(v));
				if (sz(v)>0 && v[0]<h[i][j])
					if (v[0] == h[i-1][j]){
						prev[i-1][j].pb(mp(i, j));
						next[i][j] = mp(i-1, j);
					}
					else
						if (v[0] == h[i][j-1]){
							prev[i][j-1].pb(mp(i, j));
							next[i][j] = mp(i, j-1);
						}
						else
							if (v[0] == h[i][j+1]){
								prev[i][j+1].pb(mp(i, j));
								next[i][j] = mp(i, j+1);
							}
							else
								if (v[0] == h[i+1][j]){
									prev[i+1][j].pb(mp(i, j));
									next[i][j] = mp(i+1, j);
								}
			}
		FILL(res, 0);
		char c = 'a';
		FOR(i, 1, m+1)
			FOR(j, 1, n+1)
			if (res[i][j] == 0){
				PII sink = mp(i,j);
				for (; next[sink.X][sink.Y].X != -1; sink = next[sink.X][sink.Y]);
				go(sink.X, sink.Y, c);
				++c;
			}

		printf("Case #%d:\n", t+1);
		FOR(i, 1, m+1){
			FOR(j, 1, n)
				printf("%c ", res[i][j]);
			printf("%c\n", res[i][n]);
		}
	}

}