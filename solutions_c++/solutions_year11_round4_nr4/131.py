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
#include <ctime>

using namespace std;

#define REP(i, n) for(int i=0;i<int(n);i++)
#define PB push_back
#define MP(X,Y) make_pair(X,Y)
#define SZ(X) ((int)(X.size()))
#define ALL(x)   (x).begin(),(x).end()
#define foreach(it, c)  for(typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
#define F first
#define S second
#define CLEAR(A, V) memset(A, V, sizeof(A))

typedef  long long   ll;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> II;
typedef vector<II> VII;

template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
template<class T> inline T gcd(T a, T b){ return b?gcd(b, a%b):a;}
const double EPS = 1e-9;
const double PI = acos(-1.0);

int board[150][150],R,C;

VI ady[510];
bool amenazado[510];
bool bestpath[510];
int dist[510];
VI parent[510];

int dijkstra(int f, int t){
	set<II> S;
	memset(bestpath,false,sizeof(bestpath));
	memset(amenazado,false,sizeof(amenazado));
	for(int i = 0; i < 500; i++) dist[i] = 10000;
	for(int i = 0; i < 500; i++) parent[i].clear();
	S.insert(II(0,f));
	dist[f] = 0;
	while(S.size())
	{
		int u = S.begin()->S;
		int t = S.begin()->F;
		S.erase(S.begin());
		if(u == 1) continue;
		for(int i = 0; i < ady[u].size(); i++)
		{
			int v = ady[u][i];
			if(dist[u]+1<dist[v])
			{
				if(S.find(II(dist[v],v))!=S.end()) S.erase(S.find(II(dist[v],v)));
				S.insert(II(dist[u]+1,v));
				dist[v] = dist[u]+1;
				parent[v].clear();
				parent[v].PB(u);
			}else if(dist[u]+1==dist[v]) parent[v].PB(u);
		}
	}
	queue<int> Q;
	for(int i = 0; i < parent[1].size(); i++) Q.push(parent[1][i]);
	while(Q.size())
	{
		int u = Q.front();
		bestpath[u] = true;
		Q.pop();
		for(int i = 0; i < parent[u].size(); i++)
		{
			Q.push(parent[u][i]);
		}
	}
	bestpath[1] = true;
	return dist[1];
}



int bt(int u)
{
	int r = 0, best = 0;
	if(u == 1) return 1;
	amenazado[u] = true;
	int used[500], usedc = 0;
	for(int i = 0; i < ady[u].size(); i++)
	{
		r = 0;
		if(bestpath[ady[u][i]] and dist[ady[u][i]] == dist[u]+1)
		{
			for(int j = 0; j < ady[u].size(); j++)
			{
				if(!amenazado[ady[u][j]] and j!=i)
				{
					used[usedc++] = ady[u][j];
					amenazado[ady[u][j]] = true;
					r++;
				}
			}
			r += bt(ady[u][i]);
			for(int j = 0; j < usedc; j++)
				amenazado[used[j]] = false;
			best = max(r,best);
		}
	}
	amenazado[u] = false;
	return best;
}

int main() {
	int T;
	cin >> T;
	for(int caso = 1; caso <= T; caso++)
	{
		int P,W;
		cin >> P >> W;
		for(int i = 0; i < 500; i++) ady[i].clear();
		for(int i = 0; i < W; i++)
		{
			int u,v;
			char c;
			cin >> u >> c >> v;
			ady[v].PB(u);
			ady[u].PB(v);
		}
		int dist = dijkstra(0,1);
/*		for(int i = 0; i < P; i++)
		{
			if(bestpath[i]) cout << "bestpath : " << i << endl;
		}*/
		int best = bt(0);
		printf("Case #%d: %d %d\n", caso, dist-1, best);
	}
	return 0;
}

