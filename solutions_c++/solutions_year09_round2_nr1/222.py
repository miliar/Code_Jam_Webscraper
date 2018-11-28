#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <vector>
#include <list>
#include <set>
#include <algorithm>
#include <string>
#include <sstream>
#include <functional>
#include <numeric>
#include <iterator>

using namespace std;

class Node {
	public:
		Node* l;
		Node* r;
		Node* par;
		string s;
		double p;
		Node() { r = l = par = NULL; s=""; p = 1.0;}
	
};


Node* recRead() {
	Node* res = new Node();
	char c;
	cin >> ws;
	c = cin.get();
	assert(c == '(');
	cin >> res->p >> ws;
	c = cin.get();
	if (c != ')') {
		cin.unget();
		cin >> res->s;
		res->l = recRead();
		res->r = recRead();
		cin >> ws >> c; // ')'
	}
	return res;	
}

int main() {
	freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int N;
	cin >> N;
	for (int i = 0; i < N; ++i) {
		printf("Case #%d:\n", i+1);
		int l;
		cin >> l >> ws;
		Node* root = new Node();
		root->s = "vyahhi239"; // :)
		root->r = recRead();
		int a;
		cin >> a;
		for (int j = 0; j < a; ++j) {
			string name;
			int n;
			cin >> name >> n;
			set<string> fs;
			for (int k = 0; k < n; ++k) {
				string prop;
				cin >> prop;
				fs.insert(prop);
			}
			Node* cur = root;
			double ans = 1.0;
			cout.flush();
			while (true) {
				if (cur->s == "") {
					break;
				}
				else {
					if (fs.find(cur->s) != fs.end()) {
						cur = cur->l;
					}
					else {
						cur = cur->r;
					}
					ans *= cur->p;
				}
			}
			printf("%.7lf\n", ans);
		}		
	}
	
	return 0;
}
