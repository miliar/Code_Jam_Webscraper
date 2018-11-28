#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <cmath>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef long long LL;

template<typename T> inline int sz(const T& x) { return (int)x.size(); }


struct Node {
	map<string,Node*> children;
	~Node() {
		for(map<string,Node*>::iterator it = children.begin(); it!=children.end(); ++it) {
			delete it->second;
		}
	}
};

int addDir(stringstream& ss, Node* root) {
	string name;
	getline(ss, name, '/');

	if(!sz(name))
		return 0;

	map<string,Node*>::iterator it = root->children.find(name);

	if( it == root->children.end() ) {
		root->children.insert( pair<string,Node*>(name, new Node() ) );
		return addDir(ss, root->children[name]) + 1;
	} else {
		return addDir(ss, root->children[name]);
	}
}

int main() {
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);

	int TC; cin >> TC;
	for(int tc = 1; tc <= TC; ++tc) {
		cout << "Case #" << tc << ": ";

		int N, M;
		cin >> N >> M;

		Node *root = new Node();
		char eat;

		for(int i = 0; i < N; ++i) {
			string s; cin >> s;
			stringstream ss(s);
			ss >> eat;
			addDir(ss, root);
		}

		int am = 0;

		for(int i = 0; i < M; ++i) {
			string s; cin >> s;
			stringstream ss(s);
			ss >> eat;
			am += addDir(ss, root);
		}

		cout << am << "\n";

		delete root;
	}

	return 0;
}
