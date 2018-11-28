#include <iostream> 
#include <sstream> 
#include <cstdlib> 
#include <cstdio> 
#include <cmath> 
#include <memory.h> 
#include <cstring> 
#include <string> 
#include <vector> 
#include <list> 
#include <stack> 
#include <queue> 
#include <map> 
#include <algorithm> 
#include <functional> 
using namespace std; 

template<class T> 
inline T MAX(const T& a, const T& b) {return (a>=b)?a:b;} 
template<class T> 
inline T MIN(const T& a, const T& b) {return (a<=b)?a:b;} 


int A[101][101];
int B[100001];
int C[16];
int N;
bool go(int num, int ind)
{
	if (ind == N) return true;	
	for (int i = 0; i < num; i++) {
		int prevbit = C[i];
		int nextbit = (C[i] | (1 << ind));
		if (B[nextbit] == 1) {
			C[i] = nextbit;
			if (go(num, ind+1) == true) return true;
			C[i] = prevbit;
		}
		if (prevbit == 0) break;
	}
	return false;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int n, k;
		scanf("%d%d", &n, &k);

		N = n;
		memset(A, 0x00, sizeof(A));
		memset(B, 0x00, sizeof(B));
		vector<vector<int> > prc(n, vector<int>(k, 0));

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < k; j++) {
				scanf("%d", &prc[i][j]);
			}
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				bool ok = true;
				for (int p = 0; p < k; p++) {
					if (prc[i][p] <= prc[j][p]) {
						ok = false;
						break;
					}
				}
				if (ok) A[j][i] = A[i][j] = 1;
			}
		}
		for (int i = 0; i < (1<<n); i++) {
			bool ok = true;
			for (int j = 0; j < n; j++) {
				if (i & (1<<j)) {
					for (int k = j+1; k < n; k++) {
						if (i & (1<<k)) {
							if (A[j][k] != 1) {
								ok = false;
								break;
							}
						}
					}
					if (ok == false) break;
				}
			}
			if (ok) B[i] = 1;
		}
		int res = 16;
		for (int i = 1; i <= 15; i++) {
			memset(C, 0x00, sizeof(C));
			bool ok = go(i, 0);
			if (ok) {
				res = i;
				break;
			}
		}
		fprintf(stderr, "%d\n", t);
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}

/*

const int INF = 1000000000;


template<class T>
class FlowGraph
{
public:
	enum {WHITE,GRAY,BLACK};
	vector<vector<T> > flow, cap, resCap;
	vector<int> parent, color, que;
	vector<T> minCap;
	int size, source, sink;
	T maxFlow;

	T MaxFlow_EK(const vector<vector<T> >& _cap, int _source, int _sink)
	{
		size = _cap.size();
		cap = resCap = _cap;
		flow.assign(size, vector<T>(size, 0));
		minCap.assign(size, 0);
		parent.assign(size, 0);
		color.assign(size, 0);
		que.assign(size, 0);
		source = _source;
		sink = _sink;
		maxFlow = 0;

		while (BFS_EK(source)) {
			maxFlow += minCap[sink];
			int u, v = sink;
			while (v != source) {
				u = parent[v];
				flow[u][v] += minCap[sink];
				flow[v][u] -= minCap[sink];
				resCap[u][v] -= minCap[sink];
				resCap[v][u] += minCap[sink];
				v = u;
			}
		}

		return maxFlow;
	}
	bool BFS_EK(int source) 
	{
		for (int i = 0; i < size; i++) {
			color[i] = WHITE;
			minCap[i] = INF;
		}
		int first = 0;
		int last = 0;
		que[last++] = source;
		color[source] = GRAY;

		while (first != last) {
			int v = que[first++];
			for (int u = 0; u < size; u++) {
				if (color[u] == WHITE && resCap[v][u] > 0) {
					minCap[u] = MIN(minCap[v], resCap[v][u]);
					parent[u] = v;
					color[u] = GRAY;
					if (u == sink) return true;
					que[last++] = u;
				}
			}
		}
		return false;
	}


	T VertexConnectivity(const vector<vector<T> >& _G, int _source, int _sink)
	{
		int i, j, k;
		int n = _G.size();
		vector<vector<T> > cap(n*2+2, vector<T>(n*2+2, 0));

		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				if (_G[i][j] == 1) 
					cap[i+n][j] = INF;
			}
			cap[i][i+n] = 1;
		}
		cap[n*2][_source+n] = INF;
		cap[_sink][n*2+1] = INF;

		return MaxFlow_EK(cap, n*2, n*2+1);
	}
};

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int n, k;
		scanf("%d%d", &n, &k);

		vector<vector<int> > prc(n, vector<int>(k, 0));		

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < k; j++) {
				scanf("%d", &prc[i][j]);
			}
		}

		vector<vector<int> > G(n+2, vector<int>(n+2, 0));
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				bool ok = true;
				for (int p = 0; p < k; p++) {
					if (prc[i][p] >= prc[j][p]) {
						ok = false;
						break;
					}
				}
				if (ok) G[i][j] = 1;
			}
		}
		for (int i = 0; i < n; i++) {
			bool start = true;
			bool end = true;
			for (int j = 0; j < n; j++) {
				if (G[i][j] == 1) end = false;
				if (G[j][i] == 1) start = false;
			}
			end = true;
			if (start) G[n][i] = 1;
			if (end) G[i][n+1] = 1;
		}

		FlowGraph<int> fg;
		int res = fg.VertexConnectivity(G, n, n+1);
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
*/
/*

*/
