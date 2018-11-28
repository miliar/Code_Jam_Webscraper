#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

struct tree {
	string feature;
	double val;
	tree *l, *r;
	tree() : l(0), r(0) {}
	~tree() { delete l, delete r; }
	bool is_leaf() { return l==0 && r==0; }
};
tree* root;

double solve(const set<string>& f) {
	tree* cur = root;
	double p = 1.0 * root->val;
	while (!cur->is_leaf()) {
		if (f.count(cur->feature)) cur = cur->l;
		else cur = cur->r;
		p *= cur->val;
	}
	return p;
}

vector<string> tokens;
int at;

void parse(tree* node) {
	assert(tokens[at]=="(");
	++at;
	istringstream is(tokens[at]);
	assert(is >> node->val);
	++at;
	if (tokens[at]==")") {
		++at;
		return;
	}
	node->feature = tokens[at];
	++at;

	node->l = new tree();
	parse(node->l);
	node->r = new tree();
	parse(node->r);
	assert(tokens[at]==")");
	++at;
}

int main() {
	int NCASES;
	cin >> NCASES;
	for (int z=1;z<=NCASES;++z) {
		int L;
		cin >> L;
		string s;
		getline(cin,s);
		root = new tree();
		string t;
		for (int i=0;i<L;++i) {
			getline(cin,s);
			string x ="";
			for (int j=0;j<s.length();++j) {
				if (s[j]=='(') x += " ( ";
				else if (s[j]==')') x += " ) ";
				else x += s[j];
			}
			t += x + " ";
		}
		tokens.clear();
		istringstream is2(t);
		for (string x;is2>>x;tokens.push_back(x));
		at=0;
		parse(root);

		int A;
		cin >> A;
		getline(cin,s);
		printf("Case #%d:\n", z);
		for (int i=0;i<A;++i) {
			set<string> features;
			getline(cin,s);
			istringstream is(s);
			for (string x;is >> x; features.insert(x));
			printf("%.10lf\n", solve(features)+1e-12);
		}
		delete root;
	}
}
