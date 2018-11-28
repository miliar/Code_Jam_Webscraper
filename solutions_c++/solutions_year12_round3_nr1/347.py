#include <iostream>
#include <cstring>
#include <map>
#include <vector>

#define MAX_N 1000

using namespace std;

map<int, vector<int> > graph;
bool visited[MAX_N + 1];

bool doDfs(int o);
bool dfs(int n);

bool doDfs(int o) {
	if (visited[o]) return true;
	
	visited[o] = true;
	for(size_t i = 0; i < graph[o].size(); i++) {
		bool finish = doDfs(graph[o][i]);
		
		if (finish) return true;
	}
	
	return false;
}

bool dfs(int n) {
	for(int i = 1; i <= n; i++) {
		memset(visited, 0, sizeof(visited));
		
		if(graph[i].size() > 1) {
			for(size_t j = 0; j < graph[i].size(); j++) {
				bool finish = doDfs(graph[i][j]);
				
				if (finish) return true;
			}
		}
	}
	
	return false;
}

int main(void) {
	int t, n, m, to;
	
	cin >> t;
	for(int numCase = 1; numCase <= t; numCase++) {
		graph.clear();
		
		cin >> n;
		for(int i = 1; i <= n; i++) {
			cin >> m;
			
			for(int j = 0; j < m; j++) {
				cin >> to;
				
				graph[i].push_back(to);
			}
		}
		
		bool diamond = dfs(n);
		
		if (diamond) cout << "Case #" << numCase << ": Yes" << endl;
		else cout << "Case #" << numCase << ": No" << endl;
	}
}
