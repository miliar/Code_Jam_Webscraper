#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <string>
#include <sstream>

using namespace std;

#define for0(i,n) for(int i = 0; i < (n); i ++)

int p;

vector<int> edges[450];



int depth[450];

int maxT[450];

int visited[450];

int getMax(int v) {
	// cout << "v = " << v << endl;
	if (v == 1) return 1;
	if (depth[v] >= depth[1]) return -99999;
	
	// if (maxT[v] >= 0) return maxT[v];
	
	int mm = 0;
	int numFresh = -1;
	for0(i, edges[v].size()) {
		int u = edges[v][i];
		if (visited[u] < 0)
			visited[u] = v;
	}
	
	for0(i, edges[v].size()) {
		int u = edges[v][i];
		// cout << "u = " << u;
		// if (depth[u] < depth[v]) continue;
		if (depth[u] <= depth[v]) {
			if (visited[u] == v) numFresh ++; 
			continue;
		}
		
		numFresh ++;
		int nmax = getMax(u);
		if (mm <= 0 || nmax > mm) mm = nmax;
	}
	for0(i, edges[v].size()) {
		int u = edges[v][i];
		if (visited[u] == v)
		visited[u] = -1;
	}
	
	// cout << "v = " << v << " val " << numFresh + mm << endl;
	// maxT[v] = numFresh + mm;
	return numFresh + mm;
}

int main() {
	
	int kases; cin >> kases;
	
	for0(kase, kases) {
		cin >> p;
		int w; cin >> w;
		for0(i, p) edges[i].clear();
		for0(i, w) {
			int i, j; char c; cin >> i >> c >> j;
			edges[i].push_back(j);
			edges[j].push_back(i);
		}
		
		for0(i, p) maxT[i] = -1;
		for0(i, p) depth[i] = -2;
		for0(i, p) visited[i] = -1;
		
		depth[0] = 0;
		
		queue<int> bfs;
		bfs.push(0);
		while (!bfs.empty()) {
			int v = bfs.front(); bfs.pop();
			for0(i, edges[v].size()) {
				int u = edges[v][i];
				if (depth[u] >= 0) continue;
				depth[u] = depth[v] + 1;
				bfs.push(u);
			}
		}
		
		visited[0] = 0;
		
		cout << "Case #" << (kase+1) << ": " << (depth[1]-1) << " " << getMax(0) << endl;
	}
}