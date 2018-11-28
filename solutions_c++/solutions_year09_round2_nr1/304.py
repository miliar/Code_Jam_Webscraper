#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <set>

using namespace std;

struct node {
	string feature;
	double weight;
	node *left;
	node *right;

	double get(set<string> &s) {
		if (left) {
			if (s.find(feature) == s.end())
				return weight * right->get(s);
			else
				return weight * left->get(s);
		}
		return weight;
	}
};

node* tree(char **s) {
	while ((*s)[0] != '(') {
		(*s)++;
	}
	(*s)++;
	node *res = new node;
	sscanf(*s, "%lf", &res->weight);
	while ((*s)[0] == ' ' || (*s)[0] == '.' || isdigit((*s)[0]))
		++(*s);
	if ((*s)[0] == ')') {
		res->left = NULL;
		res->right = NULL;
		++(*s);
	} else {
		char ff[1000];
		sscanf((*s), "%s", ff);
		while ((*s)[0] != '(')
			++(*s);
		res->feature = ff;
		res->left = tree(s);
		res->right = tree(s);
	}
	return res;
}

node *parse(string &s) {
	char *ss = const_cast<char*>(s.c_str());
	return tree(&ss);
}

void solve(int test) {
	/*string s, t, ans = "99999999999999999999999999";
	cin >> s;*/
	
	int n;
	cin >> n;
	char str[1000];
	cin.getline(str, 1000);
	string text;
	for (int i = 0; i < n; ++i) {
		cin.getline(str, 1000);
		text += string(" ") + string(str);
	}
	node *root = parse(text);
	int m;
	cin >> m;
	set<string> f;
	string an;
	cout.precision(7);
	cout.setf(ios::fixed);
	cout << "Case #" << test << ":\n";
	for (int i = 0; i < m; ++i) {
		cin >> an;
		f.clear();
		int k;
		cin >> k;
		string fe;
		for (int j = 0; j < k; ++j) {
			cin >> fe;
			f.insert(fe);
		}
		cout << root->get(f) << endl;
	}
}

int main() {
	//freopen("A-small.in", "r", stdin);
	//freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	//freopen("B-small.in", "r", stdin);
	//freopen("B-small.out", "w", stdout);
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);

	//freopen("C-small.in", "r", stdin);
	//freopen("C-small.out", "w", stdout);
	//freopen("C-large.in", "r", stdin);
	//freopen("C-large.out", "w", stdout);

	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; ++i) {
		solve(i + 1);
	}

	return 0;
}

