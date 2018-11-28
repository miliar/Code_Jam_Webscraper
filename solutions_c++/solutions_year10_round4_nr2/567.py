#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;
typedef long long ll;
typedef long double ld;

int N;
#define MAXN 5000
#define MAXEDG 20000
#define oo 1<<30

struct minCostMaxFlowStruct {
	int nEdge, nNodes, parent[MAXN], cost[MAXN], flow[MAXN];
	struct Edge {
		int from, to, cost, flow;
		Edge() {
		}
		Edge(int f, int t, int c, int fl) :
			from(f), to(t), cost(c), flow(fl) {
		}
	} edges[MAXEDG];
	void addEdge(int f, int t, int c, int fl) {
		edges[nEdge++] = Edge(f, t, c, fl);
		edges[nEdge++] = Edge(t, f, -c, 0);
	}
	void getPathBellman(int src, int sink) {
		fill(cost, cost + nNodes, oo);
		memset(flow, 0, sizeof(flow));
		flow[src] = oo;
		cost[src] = 0;
		for (int i = 0; i < nNodes - 1; i++) {
			bool finished = true;
			for (int j = 0; j < nEdge; j++) {
				Edge& e = edges[j];
				if (cost[e.from] + e.cost < cost[e.to] && e.flow) {
					cost[e.to] = cost[e.from] + e.cost;
					finished = false;
					flow[e.to] = min(flow[e.from], e.flow);
					parent[e.to] = j;
				}
			}
			if (finished)
				break;
		}
	}
	pair<int, int> minCostMaxFlow(int src, int sink) { // first->cost , second -> flow
		if (src == sink)
			return make_pair(0, oo);
		int totc = 0, totf = 0;
		while (true) {
			getPathBellman(src, sink);
			if (!flow[sink])
				break;
			for (int cur = sink; cur != src; cur = edges[parent[cur]].from) {
				edges[parent[cur]].flow -= flow[sink];
				edges[parent[cur] ^ 1].flow += flow[sink];
			}
			totf += flow[sink];
			totc += cost[sink] * flow[sink];
		}
		return make_pair(totc, totf);
	}
};
map<pair<int,int> ,int > cost;
vector<int> allT;
map< pair<pair<int,int>,int > , ll > dp;
ll getMin(int st, int en , int bef){
	pair<pair<int,int>,int > cur =make_pair(make_pair(st,en),bef);
	if( dp.count(cur) )
		return dp[cur];
	if( st == en ){ //last lvl
		if( allT[st] <= bef )
			return dp[cur] = 0;
		else
			return dp[cur] = 1ll<<40;
	}
	int mid = (en-st+1)/2;
	dp[cur] = min(getMin(st,st+mid-1,bef)+getMin(st+mid,en,bef),getMin(st,st+mid-1,bef+1)+getMin(st+mid,en,bef+1)+cost[make_pair(st,en)]);

//	cerr << st << " " << en << " " << bef << " " << dp[cur] << endl;
//	cerr << getMin(st,st+mid-1,bef)+getMin(st+mid,en,bef) << endl;
//	cerr << getMin(st,st+mid-1,bef+1)+getMin(st+mid,en,bef+1) << " " << cost[make_pair(st,en)] << endl;
	return dp[cur];
}
#define SMALL
#define LARGE
int main() {
	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("1B-small.out", "wt", stdout);
#endif
#ifdef LARGE
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
#endif

	cin >> N;
	for (int ii = 1; ii <= N; ii++) {
		//cin>>c>>n;
		//for(int i = 0 ; i < n; i++)
		//	cin>>arr[i];
		int p, x;
		cin >> p;
//		minCostMaxFlowStruct m;
//		m.nNodes = (1<<(p+1))+2;
//		m.nEdge = 0 ;
//		int src = m.nNodes-2;
//		int snk = m.nNodes-1;
		allT.clear();
		allT.resize(1<<p);
//		vector<pair<int, int> > allT(1 << p);
		for (int i = 0; i < 1 << p; ++i) {
			cin >> x;
//			m.addEdge(src,i,0,p-x);
			allT[i] = (p-x);
//			allT[i].second = i;
		}
//		vector<vector<int> > costs(p);
//		sort(allT.begin(), allT.end());
		dp.clear();
		cost.clear();
		int ind = (1<<p);
		int pow = 2;
		for (int i = 0; i < p; ++i) {
			for (int j = 0; j < (1 << (p - i - 1)); ++j) {
				cin >> x;
				cost[make_pair(j*pow,(j+1)*pow-1)] = x;
//				m.addEdge(ind,snk,x,1);
//				for(int k = j*pow ; k < (j+1)*pow ; ++k )
//					m.addEdge(k,ind,0,1);
//				ind++;
//				costs[i].push_back(0);

			}
			pow *= 2;
		}
//		int res = m.minCostMaxFlow(src,snk).first;
		int res = getMin(0,(1<<p)-1,0);
//		for (int i = 0; i < allT.size(); ++i) {
//			int notAttending = 0;
//			int pow = 2;
//			for (int j = 0; j < p; ++j) {
//				if (notAttending < allT[i].first) {
//					if (costs[j][allT[i].second / pow] == 0) { //not baught
//						notAttending++;
//					}
//				} else {
//					if (costs[j][allT[i].second / pow] == 0) { //not baught
//						res++;
//						costs[j][allT[i].second / pow] = 1;
//					}
//				}
//				pow *= 2;
//			}
//		}
		printf("Case #%d: ", ii);
		printf("%d", res);
		printf("\n");
	}
	return 0;
}
