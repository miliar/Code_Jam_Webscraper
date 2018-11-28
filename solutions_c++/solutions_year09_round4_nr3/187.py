/* Rajat Goel [C++] */
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<cassert>
#include<sstream>
#include<string>
#include<cmath>
#include<algorithm>
using namespace std;
const int    INF =     0x0FFFFFFF;
const double EPS =     1e-7;
typedef pair<int,int>  pii;
typedef long long      LL;
typedef long double    LD;
#define loop(i,n)      for(int i=0;i<n;i++)
#define foreach(i,a)   for(typeof((a).begin()) i=(a).begin();i!=(a).end();++i)
#define present(x,in)  (find((in).begin(),(in).end(),x) != (in).end())
#define all(a)         (a).begin(),(a).end()
#define cast(a,b)      { ostringstream myOut; myOut << a ; istringstream myIn ( myOut.str() ); myIn >> b; }
inline int fCMP(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

int n,k;
int val[105][105];

void bfs(int st, int end, vector<int> &parent, vector<vector<int> > &graph, vector<vector<int> > &flow) {
	fill(parent.begin(), parent.end(), -1);
	queue<int> q; q.push(st);
	while(!q.empty()) {
		int tmp = q.front();
		if (tmp == end) break;
		for (int i = 0; i < graph[tmp].size(); ++i) {
			if (parent[i] == -1 && flow[tmp][i] - flow[i][tmp] < graph[tmp][i]) {
				parent[i] = tmp;
				q.push(i);
			}
		}
		q.pop();
	}
	return;
}

int maxflow(vector<vector<int> > &graph, int st, int end) {
	
	int maxf = 0, n = graph.size();
	vector<vector<int> > flow(n, vector<int>(n, 0));
	vector<int> parent(graph.size());
	while(1) {
		bfs(st, end, parent, graph, flow);
		if (parent[end]==-1) {
			break;
		}

		int blockingFlow = 0x0FFFFFFF, vertex = end;
		while (vertex != st) {
			int tmp = parent[vertex];
			blockingFlow = min(blockingFlow, graph[tmp][vertex] - flow[tmp][vertex] + flow[vertex][tmp]);
			vertex = parent[vertex];
		}
		maxf+=blockingFlow;

		vertex = end;
		while (vertex != st) {
			flow[parent[vertex]][vertex]+=blockingFlow;
			flow[vertex][parent[vertex]]-=blockingFlow;
			vertex = parent[vertex];
		}
	}
	return maxf;
}

int main() {
	int T;cin >> T;
	for (int cas=1;cas<=T;cas++) {
		printf("Case #%d: ", cas);
		cin >> n >> k;
		vector<vector<int> > graph(2*n+2, vector<int>(2*n+2,0));
		loop(i,n)loop(j,k)cin >> val[i][j];
		loop(i,n)graph[0][i+1]=1;
		loop(i,n)graph[n+1+i][2*n+1]=1;
		loop(i,n)loop(j,n) {
			if (i==j) continue;
			int poss = 1;
			loop(l,k) {
				if (val[i][l] >= val[j][l]) poss=0;
			}
			graph[i+1][n+1+j] = poss;
		}
		cout << n - maxflow(graph, 0, 2*n+1) << endl;
	}
	return 0;
}
