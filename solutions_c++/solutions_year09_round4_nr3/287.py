#include <vector>
#include <algorithm>
using namespace std;
vector<int> match;
vector<bool> visited;
vector<vector<bool> > g;

bool find_match(int x) {
	if (x==-1)
		return true;
	for (unsigned int y = 0; y < match.size(); y++) {
		if (g[x][y]) {
			if (!visited[y]) {
				visited[y] = true;
				if (find_match(match[y])) {
					match[y] = x;
					return true;
				}
			}
		}
	}
	return false;
}

int maxMatch() { 
	int n = (int)g.size();
	visited.resize(n);
	match.resize(n);
	fill(match.begin(), match.end(), -1);
	int res = 0;
	for (unsigned int i=0; i<match.size(); i++) {
		fill(visited.begin(), visited.end(), false);
		if (find_match(i))
			res++;
	}
	return res;
}  

 bool less(const vector<int> &p1, const vector<int> &p2) {
	for (unsigned int i=0; i<p1.size(); i++)
		if (p2[i]>=p1[i])
			return false;
	return true;

}

int runTest() {
	int n, k, x;
	scanf("%d%d", &n, &k);
	vector<vector<int> > price(n);
	for (int i=0; i<n; i++) {
		price[i].resize(k);
		for (int j=0; j<k; j++) {
			scanf("%d", &x);
			price[i][j] = x;
		}
	}
	g.resize(n);
	for (int i=0; i<n; i++) {
		g[i].resize(n);
		fill(g[i].begin(), g[i].end(), false);
		for (int j=0; j<n; j++)
			if (less(price[i],price[j]))
				g[i][j] = true;
	}
	return n - maxMatch();
}

int main() {
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++)
		printf("Case #%d: %d\n", t, runTest());
	return 0;
}
