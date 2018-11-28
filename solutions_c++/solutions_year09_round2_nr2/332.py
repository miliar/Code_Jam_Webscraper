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
	string s, t, ans = "99999999999999999999999999";
	cin >> s;
	if (!next_permutation(s.begin(), s.end()))
	{
		sort(s.begin(), s.end());
		int zc = 0;
		for (int i = 0; i < s.length(); ++i)
			if (s[i] == '0')
				++zc;
		s = s.substr(zc);
		string t;
		for (int i = 0; i <= zc; ++i)
			t += '0';
		s = s.substr(0,1) + t + s.substr(1);// + s;
		//next_permutation(s.begin(), s.end());
	}
	cout << "Case #" << test << ": " << s << endl;
}

int main() {
	//freopen("A-small.in", "r", stdin);
	//freopen("A-small.out", "w", stdout);
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);

	//freopen("B-small.in", "r", stdin);
	//freopen("B-small.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

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

