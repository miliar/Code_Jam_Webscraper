#include <vector>
#include <map>
#include <string> 
#include <iostream> 
#include <sstream> 

using namespace std; 

typedef vector<int> VI;

#define SZ(c) ((int) (c).size())

const int INF = 1000000000;

int minEngines(const VI &q, int m) {
	int n = SZ(q);
	if (n == 0)
		return 0;
	int res = INF;
	vector<VI> best(n, m);
	best[0][q[0]] = INF;
	for (int i = 1; i < n; ++i)
		for (int j = 0; j < m; ++j) {
			best[i][j] = INF;
			if (j == q[i])
				continue;
			for (int k = 0; k < m; ++k)
				best[i][j] = min(best[i][j], best[i - 1][k] + (k != j));
			if (i == n - 1)
				res = min(res, best[i][j]);
		}
	return res;
}

char buf[256];

int readInt() {
	cin.getline(buf, 256);
	int x;
	istringstream(string(buf)) >> x;
	return x;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int numCases = readInt();
	istringstream(string(buf)) >> numCases;
	for (int c = 1; c <= numCases; ++c) {
		char buf[256];
		int m = readInt();
		map<string, int> engines;
		for (int i = 0; i < m; ++i) {
			cin.getline(buf, 256);
			engines[string(buf)] = i;
		}
		int n = readInt();
		VI queries(n);
		for (int i = 0; i < n; ++i) {
			cin.getline(buf, 256);
			queries[i] = engines[string(buf)];
		}
		printf("Case #%d: %d\n", c, minEngines(queries, m));
	}
	return 0;
}