// GCJ 2011 R1B
// wookayin


#include <cassert>
#include <set>
#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>

#define infile "input.txt"
#define outfile "output.txt"

#define REP(i, n) for(int i=0; i<(int)(n); ++i)

using namespace std;

int n, m;
vector<int> U, V;

vector< vector<int> > room;

int color[2001];
int MAX_COLOR, COLORS ;

bool recur(int v)
{
	if(v >= n) {
		for(int q = 0; q < room.size(); ++ q)
		{
			vector<bool> seen(COLORS, false);
			for(int w=0; w<room[q].size(); ++w)
				seen[ color[room[q][w]] ] = true;
			REP(w, seen.size())
				if(seen[w] == false)
					return false;
		}
		return true;
	}

	for(int i = 0; i < COLORS; ++ i)
	{
		color[v] = i;
		if( recur(v + 1) )
			return true;
	}
	return false;
}

void coloring()
{
	MAX_COLOR = n;
	REP(i, room.size()) MAX_COLOR = min(MAX_COLOR, (int)room[i].size());

	vector<int> goodColor(n);
	for(COLORS = 1; COLORS <= MAX_COLOR; ++ COLORS)
	{
		if( recur(0) )
		{
			REP(i, n) goodColor[i] = color[i];
		}
		else
		{
			break;
		}
	}
	printf("%d : ", COLORS - 1);
	for(int i = 0; i < n; ++ i)
		printf("%d ", goodColor[i] + 1);
}

void groom()
{
	room.clear();

	vector<int> PREV(n), NEXT(n);
	REP(i, n) {
		PREV[i] = (i+n-1) % n;
		NEXT[i] = (i+1) % n;
	}

	vector<int> lst;
	for(int i=0; i<n; ++i) lst.push_back(i);

	for(int rep = 0; rep < m; ++ rep)
	{
		int min_r = 987654321;
		int min_i;

		for(int i = 0; i < U.size(); ++i)
		{
			int t1 = find(lst.begin(), lst.end(), U[i]) - lst.begin();
			int t2 = find(lst.begin(), lst.end(), V[i]) - lst.begin();
			if(t1 > t2) swap(t1, t2);

			int r = min(t2 - t1, t1 + (int)lst.size() - t2);
			if(min_r > r) {
				min_i = i;
				min_r = r;
			}
		}
		int u = U[min_i];
		int v = V[min_i];
		U.erase(U.begin() + min_i);
		V.erase(V.begin() + min_i);

		int x = u, l = 0;
		vector<int> vis;
		vis.push_back(x);
		while(x != v)
		{
			x = NEXT[x];
			vis.push_back(x);
			l ++;
		}
		if(l == min_r)
		{
			NEXT[u] = v;
			PREV[v] = u;
			REP(q, vis.size()) if(vis[q] != u && vis[q] != v) {
				lst.erase( find(lst.begin(), lst.end(), vis[q]) );
			}
			room.push_back(vis);
		}
		else
		{
			x = u; l = 0;
			vis.clear();
			vis.push_back(x);
			while(x != v)
			{
				x = PREV[x];
				vis.push_back(x);
				l ++;
			}
			assert(l == min_r);
			PREV[u] = v;
			NEXT[v] = u;
			REP(q, vis.size()) if(vis[q] != u && vis[q] != v) {
				lst.erase( find(lst.begin(), lst.end(), vis[q]) );
			}
			room.push_back(vis);
		}
	}
	room.push_back(lst);
}

int main(int argc, char **argv)
{

//	freopen(infile, "r", stdin);
//	freopen(outfile, "w", stdout);

	int T;
	scanf("%d", &T);
	for(int tt=1; tt<=T; ++tt)
	{
		fprintf(stderr, "%d\n", tt);
		scanf("%d %d", &n, &m);
		U.resize(m); V.resize(m);
		REP(i, m) {
			scanf("%d", &U[i]);
			--U[i];
		}
		REP(i, m) {
			scanf("%d", &V[i]);
			--V[i];
		}
		
		groom();

		printf("Case #%d: ", tt);
		coloring();
		printf("\n");
	}
	return 0;
}