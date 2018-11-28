#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <string>
#include <map>
#include <set>
#include <numeric>
#include <algorithm>

#include <cmath>
#include <ctime>
#include <cstring>
using namespace std;

struct Node
{
	map<string, int> next;
};

vector<Node> nodes;

void add(string path)
{
	replace(path.begin(), path.end(), '/', ' ');
	stringstream in(path);
	string s;
	int v = 0;
	while (in >> s) {
		if (nodes[v].next.find(s) == nodes[v].next.end()) {
			nodes.push_back(Node());
			nodes[v].next[s] = nodes.size() - 1;
		}
		v = nodes[v].next[s];
	}
}

int main() {
	int T;
	cin >> T;
	for (int cas = 1; cas <= T; ++cas) {
		int n, m;
		cin >> n >> m;

		nodes.clear();
		nodes.push_back(Node());

		for (int i = 0; i < n; ++i) {
			string path;
			cin >> path;
			add(path);
		}
		int n0 = nodes.size();

		for (int i = 0; i < m; ++i) {
			string path;
			cin >> path;
			add(path);
		}
		int n1 = nodes.size();

		int y = n1 - n0;

		cout << "Case #" << cas << ": " << y << endl;
	}
	return 0;
}
