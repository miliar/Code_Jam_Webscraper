#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cassert>
#include <queue>
#include <set>
#include <map>
#include <string>
using namespace std;
typedef vector<int> vint;
typedef long long lint;
typedef pair<int, int> pii;
#define pb push_back
#define mp make_pair
#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size()

struct Node {
	string name;
	vector<Node *> nodes;
	Node(string name) : name(name) {}
};

vector<string> V;
int Ans = 0;

void addPath(int ix, Node *node) {
	if(ix == sz(V))
		return;
	for(int i = 0; i < sz(node->nodes); ++i) {
		if(node->nodes[i]->name == V[ix]) {
			addPath(ix + 1, node->nodes[i]);
			return;
		}
	}
	Node *nnode = new Node(V[ix]);
	node->nodes.pb(nnode);
	addPath(ix + 1, nnode);
	Ans++;
}

void read() {
	string s;
	V.clear();
	while(1) {
		char c = getchar();
		if(c == '/') {
			if(!s.empty())
				V.pb(s);
			s = "";
			continue;
		}
		if(c == '\n' || c == EOF)
			break;
		s += c;
	}
	if(!s.empty()) {
		V.pb(s);
	}
}

void del(Node *node) {
	for(int i = 0; i < sz(node->nodes); ++i) {
		del(node->nodes[i]);
	}
	delete node;
}

void Solve(int test) {
	int N, M;
	scanf("%d %d", &N, &M);
	char buf[3];
	gets(buf);
	Node *root = new Node("");
	for(int i = 0; i < N; ++i) {
		read();
		addPath(0, root);
	}
	Ans = 0;
	for(int i = 0; i < M; ++i) {
		read();
		addPath(0, root);
	}
	del(root);
	printf("Case #%d: %d\n", test, Ans);
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i) {
		Solve(i);
	}
	return 0;
}