#include <iostream>
#include <list>
#include <queue>
using namespace std;

typedef list<int> li;
typedef queue<int> qi;

bool dfs_visit(const int &u, li *adj, qi &q, int *in, int *color) {
	color[u-1] = 1;
	
	for (li::iterator it = adj[u-1].begin(); it != adj[u-1].end(); it++) {
		int v = *it;
//		cout<<v<<" ";
		if (!color[v-1]) {
			in[v-1]--;
//			if (!in[v-1]) q.push(v);
			if (dfs_visit(v, adj, q, in, color)) return true;
		}
		else return true;
	}

	color[u-1] = 2;
	return false;
}

bool dfs(li *adj, const int &n, qi &q, int *in) {
	int *color = new int[n];
	for (int i=0; i<n; i++) {
		color[i] = 0;
	}

	while (!q.empty()) {
		int u = q.front();
		q.pop();
		if (dfs_visit(u, adj, q, in, color)) return true;
		for (int i=0; i<n; i++) color[i] = 0;
	}
	return false;
}

int main() {
	ios_base::sync_with_stdio(0);

	int t;
	cin>>t;
	for (int k=1; k<=t; k++) {
		int n;
		cin>>n;
		li *adj = new li[n];
		int *in = new int[n];
		for (int i=0; i<n; i++) in[i] = 0;
		for (int i=0; i<n; i++) {
			int m;
			cin>>m;
			for (int j=0; j<m; j++) {
				int tmp;
				cin>>tmp;
				adj[i].push_back(tmp);
				in[tmp-1]++;
			}
		}

		//wyświetlanie
/*		for (int i=0; i<n; i++) {
			cout<<i+1<<": ";
			for (li::iterator it = adj[i].begin(); it !=adj[i].end(); it++) {
				cout<<(*it)<<" ";
			}
			cout<<endl;
		}
*/
		qi q;
		for (int i=0; i<n; i++) {
			if(!in[i]) q.push(i+1);
		}
		
		cout<<"Case #"<<k<<": ";
		if (dfs(adj, n, q, in)) cout<<"Yes\n";
		else cout<<"No\n";
	}

	return 0;
}
