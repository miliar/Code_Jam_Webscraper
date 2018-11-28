#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cassert>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iterator>

using namespace std;

inline void openFiles() {
#ifndef ONLINE_JUDGE
	freopen("D:/Download/A-large.in", "rt", stdin);
	freopen("D:/Download/test.out", "wt", stdout);
#endif
}

void solve();

int main() {
	openFiles();
	int t; scanf("%d\n", &t);
	while (t--) solve();
	return 0;
}

struct Node {
	//std::string name;
	std::map<std::string, Node*> subnodes;
};

void solve() {
	int n, m; scanf("%d %d\n", &n, &m);
	Node root;
	for (int i = 0; i < n; ++i) {
		char buf[110]; gets(buf);
		Node* dir = &root;
		char* name = strtok(buf, "/");
		while (name)	{
			std::map<std::string, Node*>::iterator it = dir->subnodes.find(name);
			if (it == dir->subnodes.end()) {
				dir->subnodes[name] = new Node();
				dir = dir->subnodes[name];
			} else {
				dir = it->second;
			}
			name = strtok(NULL, "/");
		}
	}
	int ret = 0;
	for (int i = 0; i < m; ++i) {
		char buf[110]; gets(buf);
		Node* dir = &root;
		char* name = strtok(buf, "/");
		while (name)	{
			std::map<std::string, Node*>::iterator it = dir->subnodes.find(name);
			if (it == dir->subnodes.end()) {
				dir->subnodes[name] = new Node();
				dir = dir->subnodes[name];
				++ret;
			} else {
				dir = it->second;
			}
			name = strtok(NULL, "/");
		}
	}
	static int ntest = 0;
	printf("Case #%d: %d\n", ++ntest, ret);
}
