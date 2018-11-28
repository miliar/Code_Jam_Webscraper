#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <fstream>
using namespace std;

#ifdef WIN32
//ifstream in("A-small.in");
ifstream in("A-large.in");
#define cin in
//ofstream out("A-small.out");
ofstream out("A-large.out");
#define cout out
#endif

struct node{
	string name;
	double v;
	node *left, *right;
	node(){
		left = right = 0;
	}
	node(string n, double vv, node* l=NULL, node* r=NULL) {
		name = n;
		v = vv;
		left = l;
		right = r;
	}
};

vector<node*> buf;
node* newnode() {
	node* nn = new node();
	buf.push_back(nn);
	return nn;
}

char name[20];
node* parse(string& input){
	int i, j, k;
	for (i = 0; i < input.size() && input[i] != '('; ++i);
	node* root = newnode();
	sscanf(input.substr(0, i).data(), "%lf", &(root->v));

	if (i < input.size()) {
		sscanf(input.substr(0, i).data(), "%lf%s", &(root->v), name);
		root->name = string(name);
		for (k = ++i, j = 1; k < input.size() && j > 0; ++k) {
			if (input[k] == '(') ++j;
			else if (input[k] == ')') --j;
		}
		root->left = parse(input.substr(i, k - 1 - i));

		while (k < input.size() && input[k] != '(') ++k;
		for (i = ++k, j = 1; k < input.size() &&  j > 0; ++k) {
			if (input[k] == '(') ++j;
			else if (input[k] == ')') --j;
		}
		root->right = parse(input.substr(i, k - 1 - i));
	}

	return root;
}

double compute(node* root, set<string>& features) {
	if (!root) return 1;

	if (features.find(root->name) != features.end()) {
		return root->v * compute(root->left, features);
	} else {
		return root->v * compute(root->right, features);
	}
}

int main()
{
	int T,ca=0;
	for (cin >> T; T; --T) {
		int n;
		cin >> n >> ws;
		string input = "", line;
		for (int i = 0; i < n; ++i) {
			getline(cin, line);
			input += line;
		}

		for (int i = 0; i < buf.size(); ++i) {
			delete buf[i];
		}
		buf.clear();
		node* root = parse(input.substr(1, input.size() - 1));

		cout << "Case #" << ++ca << ":" << endl;
		int m;
		cin >> m;
		for (int i = 0; i < m; ++i) {
			cin >> line >> n;
			set <string> features;
			for (int j = 0; j < n; ++j) {
				cin >> line;
				features.insert(line);
			}

			cout << compute(root, features) << endl;
		}
	}
	return 0;
}
