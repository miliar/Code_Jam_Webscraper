#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>

using namespace std;

struct Node {
	string name;
	vector<Node *> dirs;

	Node() {
		dirs.reserve(128);
	}
	~Node() {
		rem(this);
	}
	void rem(Node *r) {
		int i;
		for(i=0; i<r->dirs.size(); ++i) {
			rem(r->dirs[i]);
			delete r->dirs[i];
		}
		r->dirs.clear();
		r->dirs.reserve(128);
	}
} root;

vector<string> cutStr(char *str) {
	char temp;
	char *tp;
	++str;
	vector<string> res;
	while(tp = strchr(str, '/')) {
		temp = *tp;
		*tp = 0;
		res.push_back(str);
		*tp = temp;
		str = tp+1;
	}
	res.push_back(str);
	return res;
}

int mkdir(string str) {
	Node *cur = &root, *temp;
	int res = 0;
	int i, j;
	vector<string> d = cutStr(&str[0]);
	for(i=0; i<d.size(); ++i) {
		for(j=0; j<cur->dirs.size(); ++j) {
			if (cur->dirs[j]->name == d[i]) {
				break;
			}
		}
		if (j == cur->dirs.size()) {
			temp = new Node;
			temp->name = d[i];
			++res;
			cur->dirs.push_back(temp);
		}
		cur = cur->dirs[j];
	}
	return res;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int NT, T, i, j, k, n, m, res;
	cin>>NT;
	string r[128];
	string newd;
	for(T = 1; T <= NT; ++T) {
		root.rem(&root);
		cin>>n>>m;
		for(i=0; i<n; ++i) {
			cin>>r[i];
		}
		sort(r, r+n);
		for(i=0; i<n; ++i) {
			mkdir(r[i]);
		}
		res = 0;
		for(i=0; i<m; ++i) {
			cin>>newd;
			res += mkdir(newd);
		}
		cout<<"Case #"<<T<<": "<<res<<endl;
	}
	return 0;
}